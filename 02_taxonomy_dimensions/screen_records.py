"""
Systematic Screening Script — 02_taxonomy_dimensions
Sprint 001: Merge, Deduplicate, and Screen Scopus Results
Date: 2026-04-01
"""

import pandas as pd
import os
import re
import json
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
FOLDER = Path(__file__).parent
OUTPUT_CSV = FOLDER / "screened_results.csv"

# ── Search strings (from searchString.md) ─────────────────────────────────────
SEARCH_STRINGS = {
    "TITLE-ABS-KEY": (
        '( "meeting science" OR "Business meeting" OR "Workplace meeting" OR '
        '"Corporate meeting" OR "Professional meeting" ) '
        'AND ( Taxonomy OR Typology OR Classification OR Ontology OR Framework ) '
        'AND ( Dimension* OR Characteristic* OR "Task type*" OR "Meeting type*" )'
    ),
    "TITLE": (
        'TITLE ( ( "Business meeting*" OR "Workplace meeting*" ) '
        'AND ( Taxonomy OR Typology OR Classification OR Framework ) )'
    ),
}

# ── Inclusion / Exclusion Criteria ────────────────────────────────────────────
# For the paper: "Analyzing the structural dimensions and taxonomy of
# professional business meetings"
INCLUSION_CRITERIA = {
    "IC1": "Addresses professional, workplace, business, corporate, or organizational meetings as the primary context.",
    "IC2": "Proposes, reviews, or applies a taxonomy, typology, classification, ontology, or structural framework for meetings.",
    "IC3": "Examines structural dimensions, characteristics, task types, meeting types, or attributes of meetings.",
    "IC4": "Addresses meeting science, meeting effectiveness, or communication/collaboration in professional settings.",
    "IC5": "Published in English or German.",
}

EXCLUSION_CRITERIA = {
    "EC1": "Purely technical software/engineering papers (e.g., meeting scheduling algorithms, calendar tools) without structural or social analysis of meetings.",
    "EC2": "Non-professional social interaction without a meeting or organizational communication context.",
    "EC3": "Meeting tools, conferencing technology, or platforms addressed purely from a technical standpoint without meeting taxonomy or structural analysis.",
    "EC4": "Non-English and non-German publications.",
    "EC5": "Papers about meetings in a medical/clinical sense (e.g., patient-doctor encounters) without organizational communication relevance.",
}

# ── Keyword sets ───────────────────────────────────────────────────────────────
# IC1: must identify the paper as being ABOUT professional/workplace meetings
# (not just mentioning meetings in passing)
IC1_COMPOUND_KEYWORDS = [
    "business meeting", "workplace meeting", "professional meeting",
    "corporate meeting", "organizational meeting", "work meeting",
    "meeting science", "staff meeting", "multiteam meeting",
    "team meeting", "meeting attendance", "meeting participation",
    "meeting facilitation", "meeting effectiveness", "meeting purpose",
    "meeting activity", "meeting event", "meeting research",
    "meeting typology", "meeting taxonomy", "meeting type",
    "meeting function", "meeting outcome", "meeting management",
    "meeting design", "meeting structure", "meeting behavior",
    "meeting quality", "meeting process", "meeting culture",
    "meeting engagement",
]
# IC2: taxonomy/classification/framework specifically for meetings
IC2_KEYWORDS = [
    "meeting taxonomy", "meeting typology", "meeting classification",
    "meeting framework", "meeting ontology",
    "type of meeting", "types of meeting",
    "taxonomy of meeting", "typology of meeting",
    "taxonomy of workplace", "meeting categoriz",
]
# IC2 broad — taxonomy language in a paper that is IC1-confirmed
IC2_BROAD_KEYWORDS = [
    "taxonomy", "typology", "classification", "ontology",
    "categorization", "typological", "categorise", "categorize",
]
IC3_KEYWORDS = [
    "meeting purpose", "meeting dimension", "meeting structure",
    "meeting attribute", "meeting characteristic", "meeting format",
    "meeting agenda", "meeting modality", "meeting goal",
    "hybrid meeting", "synchronous meeting", "asynchronous meeting",
    "meeting outcome", "meeting effectiveness", "meeting productivity",
    "decision-making meeting", "information-sharing meeting",
    "task-based meeting", "meeting function",
    "meeting attendance", "meeting design feature", "meeting behavior",
    "group dynamics", "team creative", "dialogue orientation",
    "workplace communication", "turn-taking", "speech act",
    "meeting script", "meeting culture", "conversation analysis",
    "meeting summary", "meeting visualization",
]
IC4_KEYWORDS = [
    "meeting effectiveness", "meeting productivity",
    "collaboration in meetings", "communication in meetings",
    "meeting facilitation", "meeting management", "meeting quality",
]

# EC patterns
EC5_PATTERNS = [
    r"^the proceedings contain",
    r"^a calibration.{0,40}working group",
]

EC1_PATTERNS = [
    r"\bscheduling algorithm\b", r"\bcalendar tool\b",
    r"\bmeeting room booking\b", r"\broom reservation\b",
]
EC3_PATTERNS = [
    r"\bvideo conferencing platform\b(?!.*struct)",
    r"\bmeeting software\b(?!.*classif)",
]
# Off-topic title patterns — papers that name meetings in an unrelated context
OFFTOPIC_TITLE_PATTERNS = [
    r"forgery detection", r"disparity estimation", r"image classification",
    r"presentation slide", r"web event", r"bitemporal",
    r"cartilage", r"rhinoplasty", r"orthodontic",
    r"qualifications framework", r"health network", r"health aide",
    r"surface biology", r"geology", r"satellite",
    r"tourism perspective", r"brand image",
    r"learning acknowledgement", r"competenc",
]


def _text(row):
    """Title + Abstract + Author Keywords (Index Keywords excluded)."""
    parts = [
        str(row.get("Title", "") or ""),
        str(row.get("Abstract", "") or ""),
        str(row.get("Author Keywords", "") or ""),
    ]
    return " ".join(parts).lower()


def _match_any(text, keywords):
    return any(kw.lower() in text for kw in keywords)


def _match_pattern(text, patterns):
    return any(re.search(p, text, re.IGNORECASE) for p in patterns)


def screen_record(row):
    text = _text(row)
    title_text = str(row.get("Title", "") or "").lower()
    abstract_text = str(row.get("Abstract", "") or "").lower()

    # EC5: conference proceedings entry or clearly off-topic title
    if _match_pattern(abstract_text[:80], EC5_PATTERNS):
        return ("Excluded", "Excluded per EC5 (conference proceedings index entry or non-research "
                "document — no original empirical or conceptual contribution to meeting taxonomy).")

    # Off-topic title filter (paper primarily about an unrelated domain)
    if _match_pattern(title_text, OFFTOPIC_TITLE_PATTERNS):
        return ("Excluded", "Excluded: title indicates primary domain is unrelated to professional "
                "meeting taxonomy or structure (paper only mentions meetings incidentally).")

    has_ic1 = _match_any(text, IC1_COMPOUND_KEYWORDS)
    # IC2: specific meeting+taxonomy terms, or broad taxonomy when IC1 confirmed
    has_ic2_specific = _match_any(text, IC2_KEYWORDS)
    has_ic2_broad = _match_any(text, IC2_BROAD_KEYWORDS)
    has_ic2 = has_ic2_specific or (has_ic1 and has_ic2_broad)
    has_ic3 = _match_any(text, IC3_KEYWORDS)
    has_ic4 = _match_any(text, IC4_KEYWORDS)

    has_ec1 = _match_pattern(text, EC1_PATTERNS)

    if has_ec1:
        return ("Excluded", "Excluded per EC1 (purely technical scheduling/calendar tool without "
                "structural or social analysis of professional meetings).")

    if not has_ic1:
        return ("Excluded", "Excluded: does not satisfy IC1 (paper does not address professional/"
                "workplace/business meetings as a primary subject).")

    if not has_ic2 and not has_ic3:
        return ("Excluded", "Excluded: satisfies IC1 but does not meet IC2 or IC3 (no taxonomy, "
                "typology, classification, or structural/dimensional meeting analysis identified).")

    all_met = ["IC1"]
    details = []
    if has_ic2:
        all_met.append("IC2")
        details.append("proposes or applies a taxonomy/classification framework for meetings")
    if has_ic3:
        all_met.append("IC3")
        details.append("analyzes structural dimensions, purposes, or attributes of meetings")
    if has_ic4:
        all_met.append("IC4")
        details.append("addresses meeting effectiveness or professional collaboration")

    return ("Included", f"Included: satisfies {', '.join(all_met)} — "
            f"{'; '.join(details)}.")


# ── Step 1: Load & Merge ───────────────────────────────────────────────────────
csv_files = [f for f in FOLDER.glob("*.csv") if f.name != "screened_results.csv"]
frames = []
for f in csv_files:
    df = pd.read_csv(f, encoding="utf-8-sig")
    df["_source_file"] = f.name
    frames.append(df)

merged = pd.concat(frames, ignore_index=True)
total_raw = len(merged)

# ── Step 1: Deduplicate ────────────────────────────────────────────────────────
merged_eid = merged[merged["EID"].notna() & (merged["EID"].astype(str).str.strip() != "")].copy()
merged_no_eid = merged[merged["EID"].isna() | (merged["EID"].astype(str).str.strip() == "")].copy()
dedup_eid = merged_eid.drop_duplicates(subset=["EID"])

merged_doi = merged_no_eid[merged_no_eid["DOI"].notna() & (merged_no_eid["DOI"].astype(str).str.strip() != "")].copy()
merged_no_doi = merged_no_eid[merged_no_eid["DOI"].isna() | (merged_no_eid["DOI"].astype(str).str.strip() == "")].copy()
dedup_doi = merged_doi.drop_duplicates(subset=["DOI"])

merged_no_doi["_norm_title"] = merged_no_doi["Title"].astype(str).str.strip().str.lower()
dedup_title = merged_no_doi.drop_duplicates(subset=["_norm_title"])

unique = pd.concat([dedup_eid, dedup_doi, dedup_title], ignore_index=True)
unique = unique.drop(columns=["_norm_title", "_source_file"], errors="ignore")
total_unique = len(unique)
duplicates_removed = total_raw - total_unique

print(f"Total raw records : {total_raw}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Unique records    : {total_unique}")

# ── Step 4: Screen ─────────────────────────────────────────────────────────────
decisions = [screen_record(row) for _, row in unique.iterrows()]
unique["Selection_Decision"] = [d[0] for d in decisions]
unique["Selection_Justification"] = [d[1] for d in decisions]

n_included = (unique["Selection_Decision"] == "Included").sum()
n_excluded = (unique["Selection_Decision"] == "Excluded").sum()
print(f"Included : {n_included}")
print(f"Excluded : {n_excluded}")

# ── Save screened CSV ──────────────────────────────────────────────────────────
cols = ["Title", "Authors", "Year", "Source title", "DOI", "EID",
        "Abstract", "Author Keywords", "Document Type",
        "Selection_Decision", "Selection_Justification"]
cols = [c for c in cols if c in unique.columns]
unique[cols].to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")
print(f"Saved: {OUTPUT_CSV}")

# ── Exclusion reason summary ───────────────────────────────────────────────────
excluded = unique[unique["Selection_Decision"] == "Excluded"].copy()
exclusion_reasons = {}
reason_labels = {
    "EC1": "EC1 — Purely technical scheduling/tool paper",
    "EC3": "EC3 — Technology platform without structural meeting analysis",
    "IC1_missing": "Missing IC1 — No professional meeting context",
    "IC2_IC3_missing": "Missing IC2 & IC3 — No taxonomy or structural dimension analysis",
}
for _, row in excluded.iterrows():
    j = row["Selection_Justification"]
    if "EC1" in j:
        exclusion_reasons["EC1"] = exclusion_reasons.get("EC1", 0) + 1
    elif "EC3" in j:
        exclusion_reasons["EC3"] = exclusion_reasons.get("EC3", 0) + 1
    elif "IC1" in j:
        exclusion_reasons["IC1_missing"] = exclusion_reasons.get("IC1_missing", 0) + 1
    elif "IC2" in j and "IC3" in j:
        exclusion_reasons["IC2_IC3_missing"] = exclusion_reasons.get("IC2_IC3_missing", 0) + 1
    else:
        exclusion_reasons["other"] = exclusion_reasons.get("other", 0) + 1

top3_reasons = sorted(exclusion_reasons.items(), key=lambda x: -x[1])[:3]
top3_formatted = [(reason_labels.get(k, k), v) for k, v in top3_reasons]

stats = {
    "total_raw": total_raw,
    "duplicates_removed": duplicates_removed,
    "total_unique": total_unique,
    "n_included": int(n_included),
    "n_excluded": int(n_excluded),
    "top3_exclusion": top3_formatted,
    "csv_files": [f.name for f in csv_files],
}
with open(FOLDER / "_stats.json", "w") as fh:
    json.dump(stats, fh, indent=2)
print("Stats saved to _stats.json")

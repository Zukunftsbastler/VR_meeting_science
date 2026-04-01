"""
Systematic Screening Script — 01_tech_emotion
Sprint 001: Merge, Deduplicate, and Screen Scopus Results
Date: 2026-04-01
"""

import pandas as pd
import os
import re
from pathlib import Path

# ── Paths ──────────────────────────────────────────────────────────────────────
FOLDER = Path(__file__).parent
OUTPUT_CSV = FOLDER / "screened_results.csv"
METHODOLOGY_MD = FOLDER / "Search_and_Selection_Methodology.md"

# ── Search strings (from searchString.md) ─────────────────────────────────────
SEARCH_STRINGS = {
    "TITLE-ABS-KEY": (
        '( "Virtual Reality" OR VR OR "Extended Reality" OR XR OR Metaverse ) '
        'AND ( "Interpersonal interaction" OR "Social interaction" OR "Social presence" ) '
        'AND ( "Nonverbal communication" OR "Non-verbal communication" OR "Facial expression" '
        'OR Haptic* OR Gaze OR Emotion* OR Empathy OR Trust ) '
        'AND ( Trend* OR Feasibility OR Evolution OR "Technological capability" )'
    ),
    "TITLE": (
        'TITLE ( ( "Virtual Reality" OR VR ) '
        'AND ( "Social Interaction" OR "Interpersonal Interaction" ) )'
    ),
}

# ── Inclusion / Exclusion Criteria ────────────────────────────────────────────
INCLUSION_CRITERIA = {
    "IC1": "Empirical or conceptual study addressing VR, XR, AR, MR, Extended Reality, or Metaverse technology.",
    "IC2": "Examines interpersonal interaction, social interaction, or social presence in a virtual/immersive environment.",
    "IC3": "Covers at least one nonverbal or socio-emotional dimension: facial expression, gaze, haptics, emotion, empathy, trust, body language, or paralanguage.",
    "IC4": "Discusses technological trends, feasibility, evolution, or capability of VR/XR for social/interpersonal purposes.",
    "IC5": "Published in English or German.",
}

EXCLUSION_CRITERIA = {
    "EC1": "Purely clinical/medical VR (rehabilitation, phobia treatment, surgical training) with no interpersonal communication analysis.",
    "EC2": "Single-player gaming or entertainment VR without a social/interpersonal dimension.",
    "EC3": "Hardware or rendering engineering paper without social or communicative analysis.",
    "EC4": "Abstract or full text not available in English or German.",
    "EC5": "Non-peer-reviewed material (editorials, prefaces, book chapters without empirical content).",
}

# ── Keyword sets for rule-based screening ─────────────────────────────────────
IC1_KEYWORDS = [
    "virtual reality", "vr", "extended reality", "xr", "augmented reality",
    "mixed reality", "metaverse", "immersive", "head-mounted", "hmd",
    "avatar", "virtual environment", "3d environment",
]
IC2_KEYWORDS = [
    "interpersonal", "social interaction", "social presence", "communication",
    "collaboration", "co-presence", "face-to-face", "meeting", "remote",
    "multi-user", "multiplayer social",
]
IC3_KEYWORDS = [
    "nonverbal", "non-verbal", "facial expression", "gaze", "haptic",
    "emotion", "empathy", "trust", "body language", "gesture", "paralanguage",
    "affective", "sentiment", "mood", "expression",
]
IC4_KEYWORDS = [
    "trend", "feasibility", "evolution", "capability", "advancement",
    "state of the art", "review", "survey", "systematic", "future",
    "development", "emerging",
]

EC1_PATTERNS = [
    r"\brehabilitat\w*", r"\bphobia\b", r"\bsurgical training\b",
    r"\bposttraumatic\b", r"\bptsd\b", r"\bexposure therapy\b",
    r"\bpain management\b", r"\bclinical trial\b", r"\btherapeutic vr\b",
    r"\bschizophrenia\b", r"\bpsychosis\b", r"\bpsychotic\b",
    r"\bbipolar\b", r"\badhd\b", r"\battention deficit\b",
    r"\bclinical intervention\b",
    r"\bneuromuscular\b", r"\bneurological rehab\w*\b",
]
EC2_PATTERNS = [
    r"\bsingle.?player\b", r"\bvideo game\b(?!.*social)",
    r"\bgaming(?!.*social)(?!.*collaborative)\b",
]
EC3_PATTERNS = [
    r"\brendering pipeline\b", r"\bgraphics engine\b",
    r"\bshader\b", r"\bpolygon\b", r"\blocalization algorithm\b",
]


def _text(row):
    """Return title + abstract + author keywords for screening.
    Index Keywords (Scopus-assigned) are intentionally excluded to avoid false
    positives caused by broad Scopus index terms that do not reflect the actual
    focus of the paper."""
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

    has_ic1 = _match_any(text, IC1_KEYWORDS)
    has_ic2 = _match_any(text, IC2_KEYWORDS)
    has_ic3 = _match_any(text, IC3_KEYWORDS)
    has_ic4 = _match_any(text, IC4_KEYWORDS)

    # EC1: clinical focus. Apply broadly only when IC2 is absent.
    # When IC1+IC2 are both met, only exclude if the clinical condition is in the TITLE
    # (indicating the paper's primary subject is the clinical population, not VR communication).
    has_ec1_title = _match_pattern(title_text, EC1_PATTERNS)
    has_ec1_full = _match_pattern(text, EC1_PATTERNS)
    has_ec1 = has_ec1_title or (has_ec1_full and not has_ic2)

    has_ec2 = _match_pattern(text, EC2_PATTERNS)
    has_ec3 = _match_pattern(text, EC3_PATTERNS)

    # Primary inclusion: IC1 + IC2 required
    primary_include = has_ic1 and has_ic2

    if has_ec3 and not (has_ic2 and has_ic3):
        return ("Excluded", "Excluded per EC3 (hardware/rendering focus without social analysis) "
                "and does not meet IC2/IC3 criteria for interpersonal or socio-emotional content.")

    if has_ec1:
        return ("Excluded", "Excluded per EC1 (primary focus is clinical/therapeutic VR for a specific "
                "patient population; interpersonal communication in professional or general contexts "
                "is not the main subject).")

    if not has_ic1:
        return ("Excluded", "Excluded: does not satisfy IC1 (no VR/XR/immersive technology focus "
                "identified in title, abstract, or author keywords).")

    if not has_ic2:
        return ("Excluded", "Excluded: does not satisfy IC2 (no interpersonal/social interaction or "
                "social presence dimension identified); the paper does not address VR-based "
                "interpersonal communication.")

    if primary_include:
        all_met = ["IC1", "IC2"]
        details = []
        if has_ic3:
            all_met.append("IC3")
            details.append("nonverbal/socio-emotional analysis")
        if has_ic4:
            all_met.append("IC4")
            details.append("trend/feasibility discussion")
        detail_str = f" ({', '.join(details)})" if details else ""
        return ("Included", f"Included: satisfies {', '.join(all_met)} — addresses VR/XR technology "
                f"and interpersonal/social interaction{detail_str}.")

    return ("Excluded", "Excluded: insufficient coverage of inclusion criteria IC1–IC4; "
            "no clear link to VR interpersonal communication trends identified.")


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
# Priority: EID > DOI > normalized Title
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
    "EC1": "EC1 — Clinical/medical VR without interpersonal analysis",
    "EC2": "EC2 — Single-player gaming without social dimension",
    "EC3": "EC3 — Hardware/rendering without social analysis",
    "IC1_missing": "Missing IC1 — No VR/XR/immersive technology focus",
    "IC2_missing": "Missing IC2 — No interpersonal/social interaction dimension",
    "insufficient": "Insufficient coverage of IC1–IC4",
}
for _, row in excluded.iterrows():
    j = row["Selection_Justification"]
    if "EC1" in j:
        exclusion_reasons["EC1"] = exclusion_reasons.get("EC1", 0) + 1
    elif "EC3" in j:
        exclusion_reasons["EC3"] = exclusion_reasons.get("EC3", 0) + 1
    elif "EC2" in j:
        exclusion_reasons["EC2"] = exclusion_reasons.get("EC2", 0) + 1
    elif "IC1" in j:
        exclusion_reasons["IC1_missing"] = exclusion_reasons.get("IC1_missing", 0) + 1
    elif "IC2" in j:
        exclusion_reasons["IC2_missing"] = exclusion_reasons.get("IC2_missing", 0) + 1
    else:
        exclusion_reasons["insufficient"] = exclusion_reasons.get("insufficient", 0) + 1

top3_reasons = sorted(exclusion_reasons.items(), key=lambda x: -x[1])[:3]
top3_formatted = [(reason_labels.get(k, k), v) for k, v in top3_reasons]

# ── Export stats for methodology doc ──────────────────────────────────────────
stats = {
    "total_raw": total_raw,
    "duplicates_removed": duplicates_removed,
    "total_unique": total_unique,
    "n_included": int(n_included),
    "n_excluded": int(n_excluded),
    "top3_exclusion": top3_formatted,
    "csv_files": [f.name for f in csv_files],
}

import json
with open(FOLDER / "_stats.json", "w") as fh:
    json.dump(stats, fh, indent=2)
print("Stats saved to _stats.json")

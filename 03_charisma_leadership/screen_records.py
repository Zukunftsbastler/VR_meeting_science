"""
Systematic Screening Script — 03_charisma_leadership
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
        '( "Virtual Reality" OR VR OR Metaverse OR Avatar* ) '
        'AND ( Charisma OR Leadership OR Influence OR Persuasion OR Trust ) '
        'AND ( Acoustic* OR Voice OR "Digital rhetoric" OR Paralanguage OR "Social presence" )'
    ),
    "TITLE": (
        'TITLE ( ( "Virtual Reality" OR VR OR Avatar* ) '
        'AND ( Charisma OR Leadership OR Trust ) )'
    ),
}

# ── Inclusion / Exclusion Criteria ────────────────────────────────────────────
# Serving the paper: "Analyzing the structural dimensions and taxonomy of
# professional business meetings" — charisma, leadership, and trust in VR
INCLUSION_CRITERIA = {
    "IC1": "Involves VR, avatar(s), metaverse, or immersive digital environments as the central platform or context.",
    "IC2": "Addresses charisma, leadership, authority, influence, or persuasion in VR/avatar/digital contexts; OR examines social trust, credibility, or rapport in VR interactions.",
    "IC3": "Analyzes acoustic features, voice, vocal cues, paralanguage, digital rhetoric, or social presence as communication signals.",
    "IC4": "Examines human-to-human or human-to-avatar social communication (not purely human-machine control/automation trust).",
    "IC5": "Published in English or German.",
}

EXCLUSION_CRITERIA = {
    "EC1": "Primarily clinical/therapeutic VR (rehabilitation, phobia treatment, pain management, disorder-specific therapy) without interpersonal communication analysis.",
    "EC2": "Autonomous vehicle (AV), robot, or AI system trust without a social/interpersonal VR communication dimension.",
    "EC3": "Hardware/rendering/graphics engineering without social, communicative, or leadership analysis.",
    "EC4": "Non-English and non-German publications.",
    "EC5": "Generic leadership theory, organizational behavior, or trust studies entirely outside VR/digital avatar contexts.",
}

# ── Keyword sets ───────────────────────────────────────────────────────────────
# IC1: VR/Avatar as central context
IC1_KEYWORDS = [
    "virtual reality", "extended reality", "mixed reality", "augmented reality",
    "head-mounted display", "hmd", "metaverse", "immersive environment",
    "immersive virtual", "virtual environment",
    "avatar", "virtual agent", "digital human", "embodied agent",
    "virtual character", "animated agent", "digital avatar",
]
# IC2: charisma/leadership/influence/trust — must be SOCIAL/INTERPERSONAL
IC2_KEYWORDS = [
    "charisma", "charism",
    "leadership", "leader",
    "persuasion", "persuasive",
    "authority",
    "credibility",
    "rapport",
    "social trust", "interpersonal trust",
    "trust in avatar", "trust in virtual", "avatar trust",
    "seller trust", "consumer trust", "user trust in",
    "trustworthiness", "trustworthy",
    "influential", "influencer",
]
# IC2 additional social-interpersonal signals
IC2_SOCIAL_INFLUENCE = [
    "social influence", "peer influence",
    "brand trust", "customer trust",
    "likeability", "likability",
    "attractiveness", "perceived credibility",
    "dominance", "status signal",
    "expressiveness", "expressive avatar", "expressive agent",
    "avatar perception", "avatar appeal",
    "proteus effect",
    "embodiment effect",
    "virtual influencer",
    "social robot", "service robot trust",
    "speaker credibility", "perceived trustworthiness",
    "social engagement", "audience engagement",
]

# IC3: voice/acoustic/paralanguage/social presence
IC3_KEYWORDS = [
    "social presence",
    "voice", "vocal", "acoustic", "speech",
    "paralanguage", "paraverbal",
    "digital rhetoric",
    "nonverbal", "non-verbal",
    "prosody", "intonation", "pitch",
    "tone of voice",
]

# EC1: clinical patterns (title-based exclusion if IC4 absent)
EC1_TITLE_PATTERNS = [
    r"\brehabilitat\w*", r"\bphobia\b", r"\bexposure therapy\b",
    r"\bpain\b.*\bvr\b|\bvr\b.*\bpain\b",
    r"\bptsd\b", r"\bposttraumatic\b",
    r"\bstroke\b", r"\bneurolog\w*\b",
    r"\bschizophrenia\b", r"\bpsychosis\b",
    r"\baddiction\b", r"\bsubstance\b",
    r"\bdementia\b", r"\bcognitive impairment\b",
]

# EC2: AV/robot/automation trust (but NOT if VR social context is also present)
EC2_PATTERNS = [
    r"\bautonomous vehicle\b", r"\bself.?driving\b", r"\bav trust\b",
    r"\bpedestrian.{0,30}trust\b", r"\bdriver trust\b",
    r"\brobot trust\b(?!.*avatar)", r"\bautomat\w+ trust\b",
    r"\bhuman.robot.{0,20}trust\b",
]

# EC3: hardware/rendering focus
EC3_TITLE_PATTERNS = [
    r"\brendering\b", r"\bshader\b", r"\bpolygon\b",
    r"\blocalization algorithm\b",
    r"\bdepth estimation\b", r"\bpoint cloud\b",
]

# EC5: pure non-VR leadership/trust (no VR reference in title or early abstract)
EC5_LEADERSHIP_NO_VR = [
    r"\borgani[sz]ation.{0,20}leadership\b(?!.*virtual|avatar|immersive)",
    r"\bmanagerial.{0,20}trust\b(?!.*virtual|avatar)",
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
    abstract_start = str(row.get("Abstract", "") or "")[:400].lower()

    has_ic1 = _match_any(text, IC1_KEYWORDS)
    has_ic2_specific = _match_any(text, IC2_KEYWORDS)
    has_ic2_social = _match_any(text, IC2_SOCIAL_INFLUENCE)
    # IC2 met if specific social/interpersonal leadership/trust/charisma terms are present
    # (standalone "trust" alone is NOT sufficient — must be specific interpersonal form)
    has_ic2 = has_ic2_specific or has_ic2_social
    has_ic3 = _match_any(text, IC3_KEYWORDS)

    has_ec1_title = _match_pattern(title_text, EC1_TITLE_PATTERNS)
    has_ec2 = _match_pattern(text, EC2_PATTERNS)
    has_ec3_title = _match_pattern(title_text, EC3_TITLE_PATTERNS)

    # EC3: hardware focus (title-level)
    if has_ec3_title and not (has_ic2_specific and has_ic3):
        return ("Excluded", "Excluded per EC3 (hardware/rendering focus without social, "
                "communicative, or leadership analysis).")

    # EC1: clinical/therapeutic (title-level) when IC2 specific is absent
    if has_ec1_title and not has_ic2_specific:
        return ("Excluded", "Excluded per EC1 (primary focus is clinical/therapeutic VR; "
                "charisma, leadership, or interpersonal trust in VR is not the main subject).")

    # EC2: AV/robot trust without VR social presence dimension
    if has_ec2 and not has_ic1:
        return ("Excluded", "Excluded per EC2 (autonomous vehicle or robot trust study "
                "without VR/avatar social communication context).")

    if not has_ic1:
        return ("Excluded", "Excluded: does not satisfy IC1 (no VR, avatar, metaverse, or "
                "immersive environment focus identified in title, abstract, or author keywords).")

    if not has_ic2:
        return ("Excluded", "Excluded: does not satisfy IC2 (VR/avatar context present but no "
                "charisma, leadership, influence, persuasion, or interpersonal trust dimension "
                "identified).")

    # IC1 + IC2 both met → Included
    all_met = ["IC1", "IC2"]
    details = []
    if has_ic3:
        all_met.append("IC3")
        details.append("analyzes voice/acoustic/social-presence signals")

    detail_str = f" ({', '.join(details)})" if details else ""
    return ("Included", f"Included: satisfies {', '.join(all_met)} — addresses "
            f"VR/avatar context with charisma/leadership/trust/persuasion dimension"
            f"{detail_str}.")


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
    "EC1": "EC1 — Clinical/therapeutic VR without interpersonal trust/charisma analysis",
    "EC2": "EC2 — AV/robot trust without VR social communication context",
    "EC3": "EC3 — Hardware/rendering focus without social analysis",
    "IC1_missing": "Missing IC1 — No VR/avatar/metaverse focus",
    "IC2_missing": "Missing IC2 — VR present but no charisma/leadership/trust dimension",
}
for _, row in excluded.iterrows():
    j = row["Selection_Justification"]
    if "EC1" in j:
        exclusion_reasons["EC1"] = exclusion_reasons.get("EC1", 0) + 1
    elif "EC2" in j:
        exclusion_reasons["EC2"] = exclusion_reasons.get("EC2", 0) + 1
    elif "EC3" in j:
        exclusion_reasons["EC3"] = exclusion_reasons.get("EC3", 0) + 1
    elif "IC1" in j:
        exclusion_reasons["IC1_missing"] = exclusion_reasons.get("IC1_missing", 0) + 1
    elif "IC2" in j:
        exclusion_reasons["IC2_missing"] = exclusion_reasons.get("IC2_missing", 0) + 1
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

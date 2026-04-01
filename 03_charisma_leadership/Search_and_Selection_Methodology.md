# Search and Selection Methodology
## Stream: Charisma, Leadership, and Trust in Virtual Reality / Avatar Contexts
**Date of search:** 2026-04-01  
**Database:** Scopus  
**Project:** Analyzing the structural dimensions and taxonomy of professional business meetings — with a focus on charisma, leadership, and interpersonal trust in VR/avatar-mediated communication

---

## 1. Search Strategy

Two complementary search queries were executed on Scopus on 2026-04-01.

### Query 1 — TITLE-ABS-KEY (broad)
```
TITLE-ABS-KEY
( "Virtual Reality" OR VR OR Metaverse OR Avatar* )
AND ( Charisma OR Leadership OR Influence OR Persuasion OR Trust )
AND ( Acoustic* OR Voice OR "Digital rhetoric" OR Paralanguage OR "Social presence" )
```

### Query 2 — TITLE (focused)
```
TITLE ( ( "Virtual Reality" OR VR OR Avatar* )
AND ( Charisma OR Leadership OR Trust ) )
```

**Exported files:**
- `scopus_export_Apr 1-2026_2a5d1071-72af-45a3-a55e-7bdd20f80134.csv`
- `scopus_export_Apr 1-2026_6107be1e-c88d-4c80-896e-3afc2545c639.csv`

---

## 2. Data Consolidation & Deduplication

| Metric | Count |
|--------|------:|
| Total records across all export files | 1005 |
| Duplicate records removed (by EID → DOI → normalized Title) | 13 |
| **Unique records for screening** | **992** |

**Deduplication procedure:**  
Records were merged into a single DataFrame. Deduplication was applied hierarchically:
1. Primary key: Scopus EID (`EID`) — exact match
2. Secondary key: Digital Object Identifier (`DOI`) — exact match
3. Tertiary key: Normalized title (stripped, lowercased) — exact match

---

## 3. Inclusion and Exclusion Criteria

Selection criteria aligned with the overarching paper:
*"Analyzing the structural dimensions and taxonomy of professional business meetings — charisma, leadership, and trust in VR/avatar-mediated communication."*

### Inclusion Criteria

| Code | Criterion |
|------|-----------|
| IC1 | Involves VR, avatar(s), metaverse, or immersive digital environments as the **central** platform or context (not merely a peripheral mention). |
| IC2 | Addresses charisma, leadership, authority, influence, or persuasion in VR/avatar contexts; OR examines social/interpersonal trust, credibility, rapport, expressiveness, or audience engagement specifically in VR or avatar-mediated interactions. |
| IC3 | Analyzes acoustic features, voice, vocal cues, paralanguage, prosody, digital rhetoric, or social presence as communication signals relevant to leadership or persuasion. |
| IC4 | Examines human-to-human or human-to-avatar social communication (as opposed to purely human-machine control or automation trust). |
| IC5 | Published in English or German. |

**Minimum threshold for inclusion:** IC1 and IC2 must both be satisfied.

### Exclusion Criteria

| Code | Criterion |
|------|-----------|
| EC1 | Primarily clinical/therapeutic VR (rehabilitation, phobia treatment, pain management, disorder-specific therapy such as PTSD, schizophrenia) without interpersonal communication analysis. |
| EC2 | Autonomous vehicle (AV), robotics, or automation trust studies without a social/interpersonal VR communication dimension. |
| EC3 | Hardware, rendering, or graphics engineering papers without social, communicative, or leadership analysis. |
| EC4 | Non-English and non-German publications. |
| EC5 | Generic leadership theory, organizational behavior, or trust studies with no connection to VR, avatar, or immersive digital contexts. |

**Note on IC2 precision:** The Scopus TITLE-ABS-KEY query included the broad keyword "Trust", which appears in a very wide range of research contexts (cognitive science, motor learning, HCI usability, autonomous driving). Standalone "trust" was not treated as sufficient for IC2. Papers were required to present explicit interpersonal or social trust in VR contexts, or to address charisma, leadership, credibility, persuasion, or related constructs in avatar-mediated settings.

---

## 4. Screening Procedure

Screening was performed programmatically using `screen_records.py`. Each unique record (n = 992) was evaluated on the basis of:
- **Title**
- **Abstract**
- **Author Keywords**

Scopus-assigned Index Keywords were excluded from matching to avoid broad database-assigned false positives. EC1 and EC3 patterns were applied at the **title level** when IC2 was absent; otherwise only papers with clinical/hardware primary focus at the title level were excluded under EC1/EC3 to preserve relevant papers that mention clinical applications in passing. Each record received a `Selection_Decision` (Included/Excluded) and a `Selection_Justification` referencing the applicable IC/EC codes. Results were saved to `screened_results.csv`.

---

## 5. Screening Results

| Decision | Count |
|----------|------:|
| Included | 206 |
| Excluded | 786 |
| **Total screened** | **992** |

### Top 3 Reasons for Exclusion

| Rank | Reason | Frequency |
|------|--------|----------:|
| 1 | Missing IC2 — VR/avatar context present but no charisma, leadership, interpersonal trust, or persuasion dimension identified (papers on general VR, cognitive science, motor control, HCI usability, audio engineering, or education without leadership/trust focus) | 586 |
| 2 | Missing IC1 — No VR, avatar, metaverse, or immersive environment focus (papers addressing trust/leadership/persuasion in non-VR contexts) | 187 |
| 3 | EC3 — Hardware/rendering/engineering focus without social or leadership analysis | 5 |

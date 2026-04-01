# Search and Selection Methodology
## Stream: Technology, Emotion & Social Interaction in VR/XR
**Date of search:** 2026-04-01  
**Database:** Scopus  
**Project:** Analyzing trends in interpersonal communication in Virtual Reality

---

## 1. Search Strategy

Two complementary search queries were executed on Scopus on 2026-04-01.

### Query 1 — TITLE-ABS-KEY (broad)
```
TITLE-ABS-KEY
( "Virtual Reality" OR VR OR "Extended Reality" OR XR OR Metaverse )
AND ( "Interpersonal interaction" OR "Social interaction" OR "Social presence" )
AND ( "Nonverbal communication" OR "Non-verbal communication" OR "Facial expression"
      OR Haptic* OR Gaze OR Emotion* OR Empathy OR Trust )
AND ( Trend* OR Feasibility OR Evolution OR "Technological capability" )
```

### Query 2 — TITLE (focused)
```
TITLE ( ( "Virtual Reality" OR VR )
AND ( "Social Interaction" OR "Interpersonal Interaction" ) )
```

**Exported files:**
- `scopus_export_Apr 1-2026_25d2c753-fb17-4902-b309-2f4d3fbdb5db.csv`
- `scopus_export_Apr 1-2026_d05cc02e-320d-41e6-94b9-8cf088359d5d.csv`

---

## 2. Data Consolidation & Deduplication

| Metric | Count |
|--------|------:|
| Total records across all export files | 183 |
| Duplicate records removed (by EID → DOI → normalized Title) | 3 |
| **Unique records for screening** | **180** |

**Deduplication procedure:**  
Records were merged into a single DataFrame. Deduplication was applied hierarchically:
1. Primary key: Scopus EID (`EID`) — exact match
2. Secondary key: Digital Object Identifier (`DOI`) — exact match
3. Tertiary key: Normalized title (stripped, lowercased) — exact match

---

## 3. Inclusion and Exclusion Criteria

The following criteria were applied to select papers relevant to the overarching paper:
*"Analyzing the structural dimensions and taxonomy of professional business meetings — with a focus on technology-mediated interpersonal communication trends in VR/XR."*

### Inclusion Criteria

| Code | Criterion |
|------|-----------|
| IC1 | Empirical or conceptual study addressing VR, XR, AR, MR, Extended Reality, or Metaverse technology. |
| IC2 | Examines interpersonal interaction, social interaction, or social presence in a virtual/immersive environment. |
| IC3 | Covers at least one nonverbal or socio-emotional dimension: facial expression, gaze, haptics, emotion, empathy, trust, body language, or paralanguage. |
| IC4 | Discusses technological trends, feasibility, evolution, or capability of VR/XR for social/interpersonal purposes. |
| IC5 | Published in English or German. |

**Minimum threshold for inclusion:** IC1 and IC2 must both be satisfied.

### Exclusion Criteria

| Code | Criterion |
|------|-----------|
| EC1 | Primarily clinical/medical/therapeutic VR (rehabilitation, phobia treatment, surgical training, or disorder-specific interventions such as schizophrenia, bipolar disorder, ADHD) without a focus on interpersonal communication in professional or general contexts. |
| EC2 | Single-player gaming or entertainment VR without a social/interpersonal dimension. |
| EC3 | Hardware or rendering engineering paper (shaders, polygon optimization, graphics pipelines) without social or communicative analysis. |
| EC4 | Abstract or full text not available in English or German. |
| EC5 | Non-peer-reviewed material (editorials, prefaces, book chapters without empirical content). |

**Note on EC1:** EC1 was applied broadly when IC2 was absent, and applied when the clinical focus appeared in the paper title (indicating the clinical population is the primary subject, not VR interpersonal communication generally).

---

## 4. Screening Procedure

Screening was performed programmatically using `screen_records.py`. Each unique record was evaluated on the basis of:
- **Title**
- **Abstract**
- **Author Keywords**

Scopus-assigned Index Keywords were excluded from the primary IC/EC keyword matching to avoid false positives from broad database-assigned terms. Each record received a `Selection_Decision` (Included/Excluded) and a `Selection_Justification` referencing the applicable IC/EC codes. Results were saved to `screened_results.csv`.

---

## 5. Screening Results

| Decision | Count |
|----------|------:|
| Included | 151 |
| Excluded | 29 |
| **Total screened** | **180** |

### Top 3 Reasons for Exclusion

| Rank | Reason | Frequency |
|------|--------|----------:|
| 1 | EC1 — Clinical/medical VR without interpersonal analysis | 17 |
| 2 | Missing IC1 — No VR/XR/immersive technology focus | 7 |
| 3 | Missing IC2 — No interpersonal/social interaction dimension | 5 |

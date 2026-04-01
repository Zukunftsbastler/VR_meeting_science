# Search and Selection Methodology
## Stream: Taxonomy and Structural Dimensions of Business Meetings
**Date of search:** 2026-04-01  
**Database:** Scopus  
**Project:** Analyzing the structural dimensions and taxonomy of professional business meetings

---

## 1. Search Strategy

Two complementary search queries were executed on Scopus on 2026-04-01.

### Query 1 — TITLE-ABS-KEY (broad)
```
TITLE-ABS-KEY
( "meeting science" OR "Business meeting" OR "Workplace meeting"
  OR "Corporate meeting" OR "Professional meeting" )
AND ( Taxonomy OR Typology OR Classification OR Ontology OR Framework )
AND ( Dimension* OR Characteristic* OR "Task type*" OR "Meeting type*" )
```

### Query 2 — TITLE (focused)
```
TITLE ( ( "Business meeting*" OR "Workplace meeting*" )
AND ( Taxonomy OR Typology OR Classification OR Framework ) )
```

**Exported files:**
- `scopus_export_Apr 1-2026_0bff5d5b-d341-445d-86ee-2d152d7c49f8.csv`
- `scopus_export_Apr 1-2026_101cde22-f4a3-432e-bf34-aee8cd18b92a.csv`
- `scopus_export_Apr 1-2026_754814d1-a959-4c15-8ae1-eb369ec04bb1.csv`

---

## 2. Data Consolidation & Deduplication

| Metric | Count |
|--------|------:|
| Total records across all export files | 57 |
| Duplicate records removed (by EID → DOI → normalized Title) | 27 |
| **Unique records for screening** | **30** |

**Note:** The high duplication rate (47%) reflects expected overlap between the TITLE-ABS-KEY and TITLE queries targeting the same subject domain.

**Deduplication procedure:**  
Records were merged into a single DataFrame. Deduplication was applied hierarchically:
1. Primary key: Scopus EID (`EID`) — exact match
2. Secondary key: Digital Object Identifier (`DOI`) — exact match
3. Tertiary key: Normalized title (stripped, lowercased) — exact match

---

## 3. Inclusion and Exclusion Criteria

Selection criteria for the paper: *"Analyzing the structural dimensions and taxonomy of professional business meetings."*

### Inclusion Criteria

| Code | Criterion |
|------|-----------|
| IC1 | Addresses professional, workplace, business, corporate, or organizational meetings as the **primary** subject — not merely as a contextual example. |
| IC2 | Proposes, reviews, or applies a taxonomy, typology, classification, ontology, or structural framework **specifically for meetings**. |
| IC3 | Examines structural dimensions, characteristics, purposes, task types, modalities, or attributes of professional meetings. |
| IC4 | Addresses meeting effectiveness, meeting quality, meeting facilitation, or professional communication within meetings. |
| IC5 | Published in English or German. |

**Minimum threshold for inclusion:** IC1 must be satisfied, plus at least one of IC2 or IC3.

### Exclusion Criteria

| Code | Criterion |
|------|-----------|
| EC1 | Purely technical software/engineering papers (scheduling algorithms, calendar optimization, room-booking systems) without structural or social analysis. |
| EC2 | Non-professional social interaction without an organizational meeting context. |
| EC3 | Conferencing technology or platforms discussed purely from an engineering standpoint without meeting taxonomy or structural analysis. |
| EC4 | Non-English and non-German publications. |
| EC5 | Non-peer-reviewed material: conference proceedings index entries, editorial prefaces, or documents without original empirical or conceptual contribution. |

**Note on IC1 precision:** The Scopus TITLE-ABS-KEY query returned several records where the term "meeting" appears in a non-meeting-science context (e.g., "meeting the requirements", "meeting trips" as travel, web event listings, medical/technical papers). The IC1 check required compound meeting-science terms rather than the standalone word "meeting". Additionally, a title-based off-topic filter was applied to exclude papers whose primary domain was clearly unrelated to professional meeting science.

---

## 4. Screening Procedure

Given the small number of unique records (n = 30), the screening applied both automated keyword matching (`screen_records.py`) and a manual title/abstract review to identify false positives from the broad Scopus TITLE-ABS-KEY query. Each record was evaluated on the basis of:
- **Title**
- **Abstract**
- **Author Keywords**

Scopus-assigned Index Keywords were excluded from matching to avoid broad database-assigned false positives. Each record received a `Selection_Decision` (Included/Excluded) and a `Selection_Justification` referencing the applicable IC/EC codes. Results were saved to `screened_results.csv`.

---

## 5. Screening Results

| Decision | Count |
|----------|------:|
| Included | 13 |
| Excluded | 17 |
| **Total screened** | **30** |

### Top 3 Reasons for Exclusion

| Rank | Reason | Frequency |
|------|--------|----------:|
| 1 | Off-topic domain — paper mentions "meeting" incidentally but primary subject is unrelated (e.g., image forgery detection, web event processing, medical/anatomical studies, business tourism) | 11 |
| 2 | Missing IC2 & IC3 — professional meeting context present (IC1 met) but no taxonomy, typology, or structural dimension analysis of meetings identified | 4 |
| 3 | EC5 — Conference proceedings index entry or non-research document | 2 |

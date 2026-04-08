# Research Method: Technology & Emotion — Nonverbal Communication Trends in VR/XR

**Paper:** Paper 1 of the VR Meeting Research Trilogy  
**Stream:** Technology, Emotion & Social Interaction in VR/XR  
**Methodology type:** Systematic Literature Review (SLR) with longitudinal BI forecasting component  
**Status of selection:** Complete (151 papers included from 180 unique records after screening)

---

## Methodological Foundations

This research method is grounded in three reference works:

1. **Budgen & Brereton (2006)** — *Performing Systematic Literature Reviews in Software Engineering.* Provides the foundational SLR process: protocol definition, search strategy documentation, inclusion/exclusion criteria, and data extraction procedures.
2. **Petersen, Vakkalanka & Kuzniarz (2015)** — *Guidelines for conducting systematic mapping studies in software engineering: An update.* Provides the PICO framework for search string derivation, data extraction templates, classification schemes, and visualization strategies for structuring a research area.
3. **Irshad, Petersen & Poulding (2018)** — *A systematic literature review of software requirements reuse approaches.* Provides a completed SLR as a structural template: research questions, start set, snowball sampling procedure, rigor/relevance scoring rubric, and reporting style.

---

## Research Questions

The following research questions (RQs) drive all subsequent activities, including data extraction, coding, and synthesis. They were formulated to be answerable from the 151 included papers and any supplementary patent/TRL data.

**RQ1 — Channel Coverage:**  
Which nonverbal communication channels (facial expression, gaze, body language/gesture, haptic feedback, paralanguage/voice, proxemics/spatial presence) are addressed in the VR/XR literature, and how has coverage evolved over time (publication year)?

**RQ2 — Emotion-Channel Mapping:**  
For each nonverbal channel, which interpersonal emotions (e.g., empathy, trust, social bonding, fear, joy) have been studied, and what is the reported fidelity of transmission compared to face-to-face (FTF) interaction?

**RQ3 — Technology Readiness:**  
What is the current Technology Readiness Level (TRL) or equivalent maturity indicator for each VR/XR system feature associated with nonverbal communication, and what do trend data (publication frequency, patent filings, hardware spec announcements) indicate about near-future capability?

**RQ4 — Feasibility Threshold:**  
Based on the literature, what minimum set of nonverbal transmission capabilities is required for a VR meeting to be considered emotionally equivalent (or functionally acceptable) to a FTF meeting?

**RQ5 — VR-Readiness Scoring:**  
Which professional meeting types (e.g., status update, negotiation, creative brainstorming, onboarding) are currently VR-ready based on their emotional-communication requirements, and how will this ranking change as technology matures?

---

## LLM Execution Protocol

This section provides step-by-step instructions for an LLM agent to execute the review end-to-end. Selection is already complete; begin at **Phase 3**.

### Phase 1 — Protocol Definition (Complete)
- Review questions defined above (RQ1–RQ5).
- PICO framework applied to derive search strings (documented in `Search_and_Selection_Methodology.md`).
- Databases: Scopus. Two complementary queries executed 2026-04-01.

### Phase 2 — Study Selection (Complete)
- 180 unique records screened; 151 included.
- Inclusion/exclusion criteria documented in `Search_and_Selection_Methodology.md`.
- Selected records stored in `screened_results.csv`.

### Phase 3 — Data Extraction

#### abstract analysis

Topic modeling explorative with Bertopic
Visualizations
Quality of clusters (silhouette score etc.)

#### full text analysis

For each paper in `screened_results.csv` where `Selection_Decision == "Included"`, extract the following structured fields. Record results in a new CSV or JSON file named `extracted_data.csv`.

| Field | Description | Maps to RQ |
|-------|-------------|-----------|
| `paper_id` | Scopus EID or DOI | — |
| `title` | Full paper title | — |
| `year` | Publication year | RQ1, RQ3 |
| `study_type` | Empirical / Conceptual / Review / Mixed | RQ3 |
| `vr_system` | Named VR/XR system(s) used or discussed (e.g., Meta Quest, HTC Vive, or generic) | RQ3 |
| `nonverbal_channels` | Semi-colon separated list from: {facial_expression, gaze, gesture/body_language, haptics, paralanguage/voice, proxemics/spatial, avatar_appearance, other} | RQ1, RQ2 |
| `emotions_studied` | Semi-colon separated list of interpersonal emotions addressed | RQ2 |
| `fidelity_reported` | Qualitative or quantitative fidelity compared to FTF: {superior, equivalent, reduced, absent, not_reported} | RQ2, RQ4 |
| `trl_indicator` | Explicit TRL level if stated, OR inferred from study type and deployment context: {1-3=basic_research, 4-6=prototype, 7-9=deployed} | RQ3 |
| `trend_data_type` | Whether patent, hardware spec, market forecast, or longitudinal measurement data is included: {yes/no} | RQ3 |
| `professional_meeting_context` | Whether the paper explicitly discusses professional/business meeting scenarios: {yes/no/implied} | RQ5 |
| `key_findings` | 2–4 sentence summary of main findings relevant to nonverbal communication fidelity or trend | RQ1–RQ5 |
| `limitations` | Author-reported limitations, especially re: ecological validity | RQ4 |

**Extraction procedure (per Irshad et al. 2018, Section 3.3):**
1. Read title + abstract. If sufficient, extract all fields.
2. If abstract is ambiguous for any field, read the Methods and Results sections.
3. If still ambiguous, read conclusions.
4. Record any uncertainty in a `notes` column.

### Phase 4 — Quality Assessment

Apply the **rigor and relevance scoring rubric** (Ivarsson & Gorschek, as used in Irshad et al. 2018) to all empirical studies in the extracted set (i.e., `study_type` ≠ Conceptual).

**Rigor criteria (score 0–1 each):**
- R1: Research hypothesis or research question explicitly stated
- R2: Research method clearly described (experiment, survey, case study, etc.)
- R3: Subjects/participants described (n, expertise, context)
- R4: Validity threats discussed
- R5: Results quantified with statistical or equivalent evidence

**Relevance criteria (score 0–1 each):**
- V1: Study conducted in realistic professional or ecologically valid setting
- V2: Subjects are representative of professional meeting participants
- V3: Findings directly applicable to nonverbal communication in professional VR meetings
- V4: Practical implications or recommendations stated

Record `rigor_score` (0–5) and `relevance_score` (0–4) in `extracted_data.csv`.

### Phase 5 — Classification and Mapping

After extraction, build the following derived artefacts:

**A. Nonverbal Channel × Emotion Matrix**
- Rows: nonverbal channels (from IC3 codebook above)
- Columns: interpersonal emotions
- Cell values: count of papers addressing this combination; mean fidelity rating
- This directly answers RQ1 and RQ2.

**B. TRL Timeline Chart**
- X-axis: publication year
- Y-axis: inferred TRL level per channel
- One line per nonverbal channel
- Overlay patent-filing counts and hardware launch events where available
- This answers RQ3.

**C. VR-Readiness Scoring Table**
- For each professional meeting type (drawn from Paper 2's taxonomy, once available), list: required channels, current TRL coverage, estimated near-future coverage
- Score: sum of (channel_weight × TRL_progress_ratio) over required channels
- This answers RQ5.

### Phase 6 — Synthesis and Analysis

1. **Trend analysis:** Use publication-year data from RQ1 to identify growth/decline in each channel's research attention. Report as frequency tables and bar charts by year.
2. **Gap analysis:** Identify channel × emotion combinations where fidelity data is absent or low. These represent research gaps.
3. **Forecasting model:** Triangulate TRL indicators, publication trend slopes, and any patent/hardware data to project readiness year per channel for TRL ≥ 7. Use a simple linear or exponential model; document assumptions explicitly.
4. **Cross-paper validation:** Where multiple studies address the same channel × emotion pair, compare fidelity ratings. Flag inconsistencies for discussion.

### Phase 7 — Manuscript Drafting

Structure the paper as follows, drawing directly from extracted and synthesized data:

| Section | Content | Source |
|---------|---------|--------|
| Introduction | Problem statement, motivation, research gap | RQ formulation, gap analysis |
| Related Work | Prior reviews of nonverbal VR communication | Excluded SLR/review papers |
| Methodology | SLR protocol, PICO, search strings, IC/EC criteria, extraction template | `Search_and_Selection_Methodology.md` + this document |
| Results — RQ1 | Channel coverage analysis (frequency, trend over time) | Phase 5A, Phase 6 |
| Results — RQ2 | Emotion-channel matrix, fidelity comparisons | Phase 5A |
| Results — RQ3 | TRL timeline, forecasting model output | Phase 5B, Phase 6 |
| Results — RQ4 | Feasibility threshold derivation | Phase 6 synthesis |
| Results — RQ5 | VR-readiness ranking by meeting type | Phase 5C |
| Discussion | Implications, limitations, future work | Quality scores, gap analysis |
| Conclusion | Summary of contributions | All RQs |

---

## Validity and Bias Mitigation

Following Petersen et al. (2015) Section 3.6 and Irshad et al. (2018) Section 3.6:

- **Descriptive validity:** Extraction fields are operationally defined above to minimize ambiguous coding.
- **Theoretical validity:** RQs grounded in existing nonverbal communication theory and TRL frameworks.
- **Generalizability:** Scope limited to Scopus; snowball sampling (backward) recommended to supplement if gaps are identified.
- **Interpretive validity:** Where a judgment call is required during extraction (e.g., inferring TRL), document reasoning in the `notes` field.
- **Bias in single-reviewer extraction:** Flag papers where extraction confidence is low; recommend second-reviewer check for high-impact papers (top quartile by citation count).

# Research Method: Digital Charisma and Influence in VR Leadership

**Paper:** Paper 3 of the VR Meeting Research Trilogy  
**Stream:** Charisma, Leadership, and Trust in Virtual Reality / Avatar Contexts  
**Methodology type:** Systematic Literature Review (SLR) with model synthesis  
**Status of selection:** Complete (206 papers included from 992 unique records after screening)

---

## Methodological Foundations

This research method is grounded in three reference works:

1. **Budgen & Brereton (2006)** — *Performing Systematic Literature Reviews in Software Engineering.* Provides the foundational SLR framework: defining a review protocol before analysis begins, documenting the search strategy, applying explicit inclusion/exclusion criteria, and extracting information in a structured, reproducible way. The SLR's goal to "examine how far a given hypothesis is supported or contradicted by available empirical evidence" directly matches this paper's investigation of digital charisma claims.
2. **Petersen, Vakkalanka & Kuzniarz (2015)** — *Guidelines for conducting systematic mapping studies in software engineering: An update.* The PICO framework and classification scheme guidelines are applied here to derive the search strings (documented in `Search_and_Selection_Methodology.md`) and to structure the charisma-factor extraction taxonomy. The visualization strategies (bubble charts, classification matrices) are used to present how research attention is distributed across charisma factors.
3. **Irshad, Petersen & Poulding (2018)** — *A systematic literature review of software requirements reuse approaches.* The completed study provides the most direct template: approach categorization, quality evaluation using the rigor/relevance rubric (Ivarsson & Gorschek), snowball sampling procedure, and the reporting structure for a multi-RQ SLR.

---

## Research Questions

The following research questions (RQs) drive all subsequent activities. They were formulated to be answerable from the 206 included papers.

**RQ1 — Physical Charisma Attrition:**  
Which physical and nonverbal charisma markers (facial microexpressions, posture, physical presence/body size, tactile cues, ambient environmental dominance) are fully lost, partially preserved, or transformed when communication is mediated through a VR avatar, and what does the literature report about the psychological consequences of each attrition?

**RQ2 — Acoustic Charisma:**  
What vocal and acoustic features (voice pitch, modulation range, speech rate, pausing, loudness variation, spatial audio positioning, vocal texture/timbre) have been shown to influence perceived charisma, leadership, or trust in VR or audio-mediated settings, and which features are most critical for compensating for lost physical cues?

**RQ3 — Avatar-Mediated Trust:**  
How does avatar design (realism level, humanoid vs. stylized, customization, appearance congruence with the real person) affect interpersonal trust, perceived credibility, and attributed authority in professional VR contexts such as negotiations, sales, or leadership interactions?

**RQ4 — Digital Rhetoric and Persuasion:**  
What digital rhetorical strategies (verbal framing, spatial positioning within VR, virtual gaze management, avatar-based signaling) have been identified in the literature as effective mechanisms for persuasion and influence in VR environments?

**RQ5 — Mitigation Strategies:**  
What practical strategies, guidelines, or design recommendations have been proposed for leaders, negotiators, or speakers to maximize charisma, trust, and persuasive impact when operating through VR avatars?

---

## LLM Execution Protocol

This section provides step-by-step instructions for an LLM agent to execute the review end-to-end. Selection is already complete; begin at **Phase 3**.

### Phase 1 — Protocol Definition (Complete)
- Review questions defined above (RQ1–RQ5).
- PICO framework applied to derive search strings (documented in `Search_and_Selection_Methodology.md`):
  - Population: VR/avatar-mediated professional interactions
  - Intervention: charisma, leadership, persuasion, trust in VR/avatar contexts
  - Comparison: face-to-face vs. VR-mediated charisma/trust
  - Outcome: measurable change in perceived charisma, trust, leadership, or persuasion
- Databases: Scopus. Two complementary queries executed 2026-04-01.

### Phase 2 — Study Selection (Complete)
- 992 unique records screened; 206 included.
- Inclusion/exclusion criteria documented in `Search_and_Selection_Methodology.md`.
- Selected records stored in `screened_results.csv`.

**Note on corpus size:** With 206 included papers, this is a large-scale SLR. Full extraction of all 206 is required. Priority extraction order (if batching is needed): highest-cited papers first, then most recent publications (2020–2026).

### Phase 3 — Data Extraction

For each paper in `screened_results.csv` where `Selection_Decision == "Included"`, extract the following structured fields. Record results in `extracted_data.csv`.

| Field | Description | Maps to RQ |
|-------|-------------|-----------|
| `paper_id` | Scopus EID or DOI | — |
| `title` | Full paper title | — |
| `year` | Publication year | All |
| `study_type` | Empirical-experiment / Empirical-survey / Empirical-case_study / Conceptual / Review | RQ1–RQ5 |
| `vr_platform` | Named VR/avatar system (or generic if unspecified) | RQ3 |
| `avatar_type` | Realistic / Stylized / Abstract / Text-based agent / Embodied agent / Not_applicable | RQ3 |
| `charisma_factors_studied` | Pipe-separated list from: {physical_presence, facial_expression, gaze, posture/gesture, voice_pitch, voice_modulation, speech_rate, spatial_audio, vocal_timbre, verbal_framing, avatar_appearance, other} | RQ1, RQ2 |
| `outcome_variable` | What was measured: {perceived_leadership / perceived_trust / perceived_credibility / persuasion_success / social_presence / rapport / other} | RQ1–RQ5 |
| `fidelity_vs_ftf` | How VR outcome compares to face-to-face benchmark: {superior / equivalent / reduced / absent / not_compared} | RQ1, RQ2 |
| `professional_context` | Professional scenario tested: {negotiation / sales / presentation / team_leadership / general_meeting / lab_task / none_specified} | RQ3, RQ5 |
| `mitigation_proposed` | Does the paper propose a strategy, guideline, or design recommendation? {yes/no} | RQ5 |
| `mitigation_description` | If yes: brief description of the strategy (1–3 sentences) | RQ5 |
| `key_findings` | 3–5 sentence summary of main empirical or theoretical contributions | RQ1–RQ5 |
| `limitations` | Author-reported limitations (sample, ecological validity, avatar fidelity) | Quality |

**Extraction procedure (following Irshad et al. 2018, Section 3.3):**
1. Read title + abstract. Extract all clearly identifiable fields.
2. For `charisma_factors_studied`, `outcome_variable`, and `fidelity_vs_ftf`, consult the Methods and Results sections if the abstract is insufficient.
3. For `mitigation_description`, consult the Discussion or Conclusion sections.
4. Record any ambiguity in a `notes` field.

### Phase 4 — Quality Assessment

Apply the **rigor and relevance scoring rubric** (Ivarsson & Gorschek, as used in Irshad et al. 2018) to all empirical studies (`study_type` contains "Empirical").

**Rigor criteria (score 0–1 each):**
- R1: Research hypothesis or RQ explicitly stated
- R2: Research method clearly described
- R3: Participants described (n, demographic, professional context)
- R4: Validity threats or limitations explicitly discussed
- R5: Quantitative results reported with statistical evidence OR qualitative results with systematic coding

**Relevance criteria (score 0–1 each):**
- V1: Study conducted in realistic professional or ecologically valid setting (not purely abstract lab task)
- V2: Participants are representative of professional adults (not solely student populations)
- V3: Findings generalizable to professional VR meeting contexts
- V4: Practical implications, design guidelines, or actionable recommendations stated

Record `rigor_score` (0–5) and `relevance_score` (0–4) in `extracted_data.csv`. Papers scoring ≥ 7 total are designated **high-quality anchors** for the synthesis.

### Phase 5 — Classification and Analysis

**Step 5.1 — Charisma Factor Taxonomy:**
1. Collect all unique charisma factor labels from `charisma_factors_studied`.
2. Group into three super-categories:
   - **Physical charisma factors:** Lost or fundamentally transformed by VR avatar mediation
   - **Acoustic/vocal charisma factors:** Preserved or amplified in VR (transmitted via audio)
   - **Digital charisma factors:** Emergent — unique to VR avatar-mediated interaction (avatar design, spatial positioning, virtual gaze, embodiment effects)
3. For each factor, record: (a) degree of attrition in VR (answering RQ1), (b) compensatory potential (answering RQ2).

**Step 5.2 — Avatar Trust Model:**
From papers addressing RQ3, build a model mapping avatar design choices to trust outcomes:
- Rows: avatar design dimensions (realism, appearance match, customization, expressiveness)
- Columns: trust/credibility outcomes
- Cell values: direction of effect (positive/negative/null/mixed) with citation count

**Step 5.3 — Acoustic Charisma Model:**
From papers addressing RQ2, build a model mapping vocal features to charisma/leadership outcomes:
- Feature list: pitch level, pitch variability, speech rate, pause frequency, loudness, spatial audio, timbre/vocal quality
- For each feature: effect direction, effect size estimate if available, VR-specific findings vs. general audio research

**Step 5.4 — Mitigation Strategy Catalogue:**
From papers addressing RQ5, compile all proposed strategies. Organize as a structured catalogue:
- `strategy_id`: Sequential code (S01, S02, ...)
- `category`: Acoustic / Avatar-design / Verbal-rhetorical / Spatial / Environmental
- `description`: Full strategy description
- `evidence_level`: Empirically validated / Conceptually proposed / Expert recommendation
- `source_papers`: Citing paper IDs

**Step 5.5 — Research Gap Analysis:**
Identify charisma factor × professional scenario combinations with sparse or no coverage. These become the "future research" section of the manuscript.

### Phase 6 — Synthesis

1. **Narrative synthesis:** For each RQ, synthesize findings across high-quality anchor papers first, then incorporate lower-quality papers as corroborating or conflicting evidence. Follow the pattern used in Irshad et al. (2018): state the finding, cite supporting papers, note conflicting evidence, explain discrepancies.
2. **Publication trend analysis:** Plot paper counts by year for the full set of 206 included papers, segmented by charisma factor super-category. This reveals how research attention has shifted from physical to digital/acoustic charisma over time.
3. **Acoustic Charisma Model output:** Present as a ranked list of acoustic features ordered by evidence strength (rigor × relevance × citation count) for their charismatic impact in VR.
4. **The Avatar Filter Framework:** Synthesize RQ1, RQ2, and RQ3 into a conceptual model depicting the transformation of charisma signals through the "avatar filter" — what is lost, what is transformed, what is preserved, and what is newly created.

### Phase 7 — Manuscript Drafting

| Section | Content | Source |
|---------|---------|--------|
| Introduction | Leadership in VR: the avatar filter problem; motivation and gap | RQ1 framing |
| Related Work | Prior reviews of VR social presence, avatar studies, and leadership | Excluded review papers + anchor papers |
| Methodology | SLR protocol, PICO, search strings, IC/EC criteria, extraction template, quality rubric | `Search_and_Selection_Methodology.md` + this document |
| Results — RQ1 | Physical charisma attrition analysis; charisma factor taxonomy | Step 5.1 |
| Results — RQ2 | Acoustic Charisma Model; ranked vocal features | Step 5.3, Phase 6 |
| Results — RQ3 | Avatar Trust Model; avatar design × trust outcomes | Step 5.2 |
| Results — RQ4 | Digital rhetoric strategies in VR | Phase 5 extraction |
| Results — RQ5 | Mitigation Strategy Catalogue | Step 5.4 |
| Discussion | The Avatar Filter Framework; integration with Papers 1 and 2; limitations | Phase 6 synthesis |
| Conclusion | Practical guidelines for VR leadership; future research priorities | Step 5.5, RQ gaps |

---

## Validity and Bias Mitigation

Following Budgen & Brereton (2006) Section 3 and Irshad et al. (2018) Section 3.6:

- **Selection bias:** The 992-record corpus was large; EC1 (clinical VR) and EC2 (autonomous vehicle trust) were applied broadly to exclude off-topic trust research. Flag borderline exclusions for review if synthesis reveals missing perspectives.
- **Extraction reliability:** With 206 papers, single-reviewer extraction is unavoidable for the full set. Apply second-reviewer check to the top 30 papers by citation count (high-quality anchors) to validate extraction accuracy.
- **Charisma construct validity:** "Charisma" is operationalized diversely across the literature (leadership ratings, persuasion rates, social presence scores, trust scales). Document which operationalization each paper uses; aggregate with care.
- **Temporal generalizability:** VR avatar technology has changed rapidly. Papers published before 2018 may not reflect current avatar fidelity. Segment findings by publication era (pre-2018 / 2018–2021 / 2022–2026) where findings diverge.
- **Ecological validity threat:** Many studies use student samples in lab settings. The relevance score in Phase 4 penalizes this; weight high-relevance papers more heavily in synthesis conclusions.
- **Publication bias:** Studies with null results (VR charisma = FTF charisma) may be underrepresented. Note this as a limitation and recommend future registered-report studies.

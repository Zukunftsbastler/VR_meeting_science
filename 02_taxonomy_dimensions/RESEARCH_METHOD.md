# Research Method: The DNA of Business Meetings — A Dimensional Framework

**Paper:** Paper 2 of the VR Meeting Research Trilogy  
**Stream:** Taxonomy and Structural Dimensions of Business Meetings  
**Methodology type:** Systematic Mapping Study (SMS) with framework synthesis  
**Status of selection:** Complete (13 papers included from 30 unique records after screening)

---

## Methodological Foundations

This research method is grounded in three reference works:

1. **Budgen & Brereton (2006)** — *Performing Systematic Literature Reviews in Software Engineering.* Provides the foundational SLR process: protocol definition, search strategy documentation, inclusion/exclusion criteria, and data extraction procedures. The taxonomy-building goal of this paper aligns with the SLR's mandate to "identify where there are gaps in current research" and to "provide an objective summary of research evidence concerning a topic."
2. **Petersen, Vakkalanka & Kuzniarz (2015)** — *Guidelines for conducting systematic mapping studies in software engineering: An update.* The systematic mapping study (SMS) methodology is the primary method here: SMS is explicitly designed to "structure a research area through classification and counting contributions," which directly matches the objective of building a dimensional taxonomy of business meetings. The updated guidelines provide the classification scheme design, visualization strategies (bubble charts, bar charts), and the distinction between SMS and SLR goals.
3. **Irshad, Petersen & Poulding (2018)** — *A systematic literature review of software requirements reuse approaches.* Provides a structural template for multi-dimensional classification: how to move from raw extracted data to a coherent taxonomy, how to present classification results, and how to assess the quality of included studies.

---

## Research Questions

The following research questions (RQs) drive all subsequent activities. They were formulated to be answerable from the 13 systematically selected papers plus the pre-existing grey literature in the `sources/meeting_science/` and `sources/Scopus_taxonomy_papers/` directories.

**RQ1 — Taxonomy Landscape:**  
What taxonomies, typologies, classification schemes, or structural frameworks for professional/business meetings exist in the literature, and how do they differ in scope, granularity, and theoretical basis?

**RQ2 — Dimensional Inventory:**  
What structural dimensions, characteristics, or attributes have been used to differentiate meeting types (e.g., purpose/goal, task type, level of formality, group size, interactivity, temporal structure, decision-authority, information-flow direction)?

**RQ3 — Dimension–Meeting Type Mapping:**  
How do the identified structural dimensions map onto standard professional meeting types (e.g., status update, decision meeting, brainstorming, negotiation, training, onboarding, social/team-building), and which dimensions are most discriminating?

**RQ4 — VR Suitability Hypothesis:**  
Based on each dimension, what hypotheses can be derived about VR's suitability? Specifically: which dimensions of a meeting increase or decrease the benefit of conducting it in VR versus video conferencing versus face-to-face?

**RQ5 — Framework Completeness:**  
What gaps exist in current taxonomies — dimensions that are theoretically relevant to VR suitability but not currently represented in the literature — and what dimensions should be added to create a complete, VR-aware meeting taxonomy?

---

## LLM Execution Protocol

This section provides step-by-step instructions for an LLM agent to execute the review end-to-end. Selection is already complete; begin at **Phase 3**.

### Phase 1 — Protocol Definition (Complete)
- Review questions defined above (RQ1–RQ5).
- PICO framework applied to derive search strings (documented in `Search_and_Selection_Methodology.md`):
  - Population: professional/workplace/business meetings
  - Intervention: taxonomy, typology, classification, dimensional framework
  - Comparison: different classification approaches
  - Outcome: structured dimensional framework usable for VR suitability assessment
- Databases: Scopus. Three complementary queries executed 2026-04-01.

### Phase 2 — Study Selection (Complete)
- 30 unique records screened; 13 included.
- Inclusion/exclusion criteria documented in `Search_and_Selection_Methodology.md`.
- Selected records stored in `screened_results.csv`.

**Important note:** The small number of systematically retrieved papers (n = 13) reflects the narrow Scopus query focus. The supplementary literature in `sources/meeting_science/` and `sources/Scopus_taxonomy_papers/` must be incorporated as a **grey literature / snowball supplement** (per Irshad et al. 2018, backward snowball from key anchor papers) to achieve sufficient dimensional coverage.

### Phase 3 — Data Extraction

For each paper in `screened_results.csv` where `Selection_Decision == "Included"`, plus each supplementary paper from `sources/meeting_science/` and `sources/Scopus_taxonomy_papers/`, extract the following structured fields. Record results in `extracted_data.csv`.

| Field | Description | Maps to RQ |
|-------|-------------|-----------|
| `paper_id` | DOI, EID, or short citation key | — |
| `title` | Full paper title | — |
| `year` | Publication year | RQ1 |
| `source_type` | Scopus_systematic / grey_literature / snowball | — |
| `taxonomy_proposed` | Does the paper propose a new taxonomy/typology/framework? {yes/no} | RQ1 |
| `taxonomy_name` | Name or label of the taxonomy if proposed | RQ1 |
| `theoretical_basis` | Underlying theory or discipline (e.g., communication theory, organizational behavior, speech act theory) | RQ1 |
| `dimensions_identified` | Pipe-separated list of all dimensions/attributes used to differentiate meeting types | RQ2 |
| `dimension_definitions` | For each dimension: short definition or operationalization as given by the authors | RQ2 |
| `meeting_types_covered` | Pipe-separated list of meeting types discussed or classified | RQ3 |
| `dimension_meeting_mapping` | For each dimension: which meeting types score high/low on it | RQ3 |
| `vr_discussed` | Does the paper discuss virtual/remote/technology-mediated meetings? {yes/no/implied} | RQ4 |
| `vr_suitability_claim` | Any explicit or implied claim about which meeting types suit virtual formats | RQ4 |
| `identified_gaps` | Dimensions the authors note as missing from their or other frameworks | RQ5 |
| `key_findings` | 3–5 sentence summary of core contributions | RQ1–RQ5 |

**Extraction procedure:**
1. Read title and abstract. If sufficient, extract all fields.
2. If abstract is ambiguous, read the section introducing the taxonomy/framework.
3. If still ambiguous, read the full results/discussion.
4. For supplementary books (e.g., Hoffman 2018 epub in `sources/meeting_science/`), extract chapter-level summaries relevant to meeting dimensions.

### Phase 4 — Quality Assessment

Because this is a systematic mapping study (Petersen et al. 2015), formal quality scoring is not required for all papers. However, apply the following minimal quality check to each included paper to flag low-quality sources:

| Check | Criterion | Disqualifier |
|-------|-----------|-------------|
| QC1 | Is the taxonomy/dimension set grounded in empirical data or theory? | Reject if purely anecdotal |
| QC2 | Are the dimensions clearly defined and mutually distinguishable? | Flag if definitions are absent |
| QC3 | Has the taxonomy been applied to real meeting examples? | Flag if purely theoretical without application |
| QC4 | Is the paper peer-reviewed? | Flag grey literature for sensitivity analysis |

Record `quality_flag` (pass / flag / reject) in `extracted_data.csv`.

### Phase 5 — Taxonomy Synthesis and Framework Construction

This is the core analytical phase, generating the paper's primary output.

**Step 5.1 — Dimension Consolidation:**
1. Collect all unique dimension labels from the `dimensions_identified` field across all included papers.
2. Group semantically equivalent dimensions (e.g., "formality level" = "degree of structure" = "meeting formality").
3. Produce a canonical dimension list with unified labels and cross-paper aliases.

**Step 5.2 — Dimension Codebook:**
For each canonical dimension, define:
- `dimension_id`: Short code (e.g., DIM01)
- `label`: Canonical label (e.g., Task Abstraction)
- `definition`: 1–2 sentence operational definition
- `value_range`: Possible values or scale (e.g., abstract ↔ concrete; ordinal 1–5; categorical)
- `source_papers`: Which papers address this dimension
- `vr_hypothesis`: Hypothesis about how VR performance varies along this dimension (e.g., "VR is disadvantaged for high-abstraction tasks requiring shared physical artefacts")

**Step 5.3 — Meeting Type × Dimension Matrix:**
- Rows: standard professional meeting types (minimum set: status update, decision meeting, brainstorming/ideation, negotiation, training/onboarding, social/team-building, one-on-one feedback)
- Columns: canonical dimensions from Step 5.1
- Cell values: score or qualitative rating derived from literature; flag if literature-derived vs. extrapolated
- This directly answers RQ3.

**Step 5.4 — VR Suitability Model:**
For each dimension, formulate a directional hypothesis (from RQ4) using the following template:

> "When a meeting scores HIGH on [dimension], VR is [more suitable / less suitable / neutral] because [mechanism derived from literature]."

Aggregate dimension-level hypotheses into a composite VR Suitability Score per meeting type. Document formula and weights explicitly.

**Step 5.5 — Gap Analysis (RQ5):**
Compare the canonical dimension set from Step 5.1 against a theoretical checklist of communication requirements relevant to VR (derived from Paper 1's nonverbal channel analysis). Identify dimensions that are:
- Absent from current taxonomies but theoretically required for VR suitability assessment
- Present but poorly operationalized for VR contexts

### Phase 6 — Visualization

Following Petersen et al. (2015) Section 5 on visualization:

- **Bubble chart:** X = time (publication year); Y = dimension category; bubble size = number of papers addressing that dimension. Shows research attention trends.
- **Heat map:** Meeting type × dimension matrix (from Step 5.3), color-coded by VR suitability direction.
- **Taxonomy tree:** Hierarchical diagram of meeting types organized by primary discriminating dimensions.

### Phase 7 — Manuscript Drafting

| Section | Content | Source |
|---------|---------|--------|
| Introduction | Gap in VR meeting research: absence of a structured meeting taxonomy for VR suitability | RQ1, RQ5 |
| Related Work | Existing taxonomies and their limitations | Phase 3 extraction, RQ1 |
| Methodology | SMS protocol, PICO, search strategy, extraction template | `Search_and_Selection_Methodology.md` + this document |
| Results — RQ1 | Taxonomy landscape: overview of existing frameworks | Phase 3, Step 5.1 |
| Results — RQ2 | Dimensional inventory: canonical dimension codebook | Step 5.2 |
| Results — RQ3 | Meeting type × dimension matrix | Step 5.3 |
| Results — RQ4 | VR suitability hypotheses per dimension | Step 5.4 |
| Results — RQ5 | Gap analysis: missing dimensions and recommended additions | Step 5.5 |
| Discussion | Framework validity, limitations, integration with Papers 1 and 3 | Quality flags, gap analysis |
| Conclusion | Dimensional framework as a practical tool for VR meeting planning | All RQs |

---

## Validity and Bias Mitigation

Following Petersen et al. (2015) Section 3.6:

- **Descriptive validity:** Canonical dimension labels must be derived inductively from the source text, not imposed a priori. Document any re-labeling decisions.
- **Theoretical validity:** Dimension codebook must be grounded in organizational communication theory. Cross-reference with `sources/meeting_science/` anchor texts.
- **Generalizability:** Small Scopus sample (n = 13) supplemented by snowball from `sources/meeting_science/`. Explicitly document which papers entered via each route.
- **Classification reliability:** Where two dimensions from different papers could be coded as the same or different, document the decision rule. Aim for MECE (Mutually Exclusive, Collectively Exhaustive) dimension set.
- **VR hypothesis bias:** Hypotheses in Step 5.4 must be derived from or consistent with literature; speculative hypotheses must be explicitly labeled as such.

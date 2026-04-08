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

#### Taxonomy Type Decision: Faceted Taxonomy

**Chosen approach:** The canonical framework constructed in this paper is a **faceted taxonomy**.

A faceted taxonomy defines a set of independent, orthogonal dimensions (facets). Each meeting type is described by assigning a value on every facet simultaneously; the combination of values constitutes the meeting type's profile. No single hierarchy is imposed, and a meeting type can score anywhere on any facet independently of its scores on others.

**Why faceted, not an alternative:**

| Type | Why rejected for this paper |
|------|-----------------------------|
| Hierarchical (tree) | Forces each meeting type into a single branch. Meetings blend purposes (a negotiation is also a decision meeting); a tree cannot represent this without arbitrary branching choices that introduce researcher bias. |
| Polyhierarchical | Allows multiple parents but still imposes inherited properties top-down. More flexible than a strict tree, but adds structural complexity without adding analytical power for VR scoring. |
| Flat list | Assigns named types with no dimensional structure. Provides no mechanism to compute VR suitability as a function of meeting characteristics. |
| Dimensional/continuous matrix | Places meetings in a continuous space on two or three axes. Useful for visualization (see Phase 6) but cannot serve as the classification instrument itself, since most dimensions in this paper are ordinal or categorical, not continuous. |

**Why faceted is correct here:** The VR Suitability Model (Step 5.4) must compute a score as a weighted sum of independent dimension-level contributions. This is only tractable if each dimension is an independent facet: the score for Task Abstraction does not depend on what the meeting scores for Group Size. A hierarchical structure would collapse these independent contributions into categorical placements, making the scoring model impossible to operationalize. The faceted structure also satisfies the MECE principle required for reliability: facets must be Mutually Exclusive (no two facets measure the same underlying construct) and Collectively Exhaustive (together they capture all dimensions relevant to VR suitability).

---

**Step 5.1 — Facet Consolidation:**
1. Collect all unique dimension labels from the `dimensions_identified` field across all included papers.
2. Group semantically equivalent dimensions under a single canonical label (e.g., "formality level" = "degree of structure" = "meeting formality" → canonical: **Formality**). Record all aliases.
3. Apply the **orthogonality check**: for any two candidate facets, ask whether knowing a meeting's value on facet A provides information about its value on facet B. If yes (e.g., "decision authority" and "meeting formality" are correlated but not identical), retain both but flag the correlation. If they are near-synonyms measuring the same construct, merge them.
4. Produce the final canonical facet list. Each facet must be:
   - **Independently scorable:** A meeting can be assigned a value on this facet without knowing its values on other facets.
   - **Operationally defined:** The scoring rule is unambiguous (see Step 5.2).
   - **Relevant to VR suitability:** At least one directional hypothesis about VR performance is derivable (see Step 5.4).

**Step 5.2 — Facet Codebook:**
For each canonical facet, define the following fields. These form the authoritative codebook used during Step 5.3 scoring.

| Field | Description |
|-------|-------------|
| `facet_id` | Short code (e.g., F01, F02, …) |
| `label` | Canonical facet label (e.g., Task Abstraction) |
| `aliases` | Alternative labels used in source papers |
| `definition` | 1–2 sentence operational definition |
| `value_range` | Scoring scale: ordinal (e.g., 1 = fully concrete ↔ 5 = fully abstract), binary (yes/no), or categorical (e.g., unidirectional / bidirectional / multi-directional) |
| `anchor_descriptions` | Brief description of what scores 1 and 5 (or each category) look like in practice |
| `source_papers` | Paper IDs that define or use this facet |
| `vr_hypothesis` | Directional hypothesis: "When a meeting scores HIGH on this facet, VR is [more / less / neutral] suitable because [mechanism]." |

**Step 5.3 — Faceted Meeting Profile Matrix:**

Using the faceted taxonomy decided above, construct the **Meeting Type × Facet Profile Matrix**: each meeting type is assigned a value on every facet, producing a structured faceted profile.

**Meeting types (minimum set):**
Status update, decision meeting, brainstorming/ideation, negotiation, training/onboarding, social/team-building, one-on-one feedback.
Add further types if source papers identify them as distinct.

**Scoring procedure:**
1. For each meeting type, assign a value on each facet using the anchor descriptions from the Step 5.2 codebook.
2. Derive values from source literature where possible. If no paper directly characterizes this meeting type on this facet, apply reasoned inference from the meeting type's definition and flag the cell as `[inferred]`.
3. Record provenance: for each cell, note whether the value is `[literature-derived]`, `[inferred-from-definition]`, or `[extrapolated-from-adjacent-type]`.

**Output format:** A matrix where rows are meeting types, columns are facet IDs, and each cell contains the facet value plus a provenance flag. Example structure:

| Meeting Type | F01 Task Abstraction | F02 Decision Authority | F03 Group Size | … | VR Suitability (Step 5.4) |
|---|---|---|---|---|---|
| Status update | 2 — concrete [lit] | Centralized [lit] | Medium [lit] | … | — |
| Negotiation | 3 — mixed [inferred] | Distributed [lit] | Small [lit] | … | — |
| Brainstorming | 5 — abstract [lit] | Distributed [lit] | Medium [inferred] | … | — |

The completed matrix directly answers **RQ3** and serves as the input to the VR Suitability Model in Step 5.4.

**Validation:** After scoring, check that no two meeting types share an identical profile across all facets. If they do, either a facet is redundant (merge it) or the two meeting types are not genuinely distinct (merge them or add a discriminating facet).

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

- **Bubble chart:** X = time (publication year); Y = facet category; bubble size = number of papers addressing that facet. Shows research attention trends across the literature.
- **Heat map:** Meeting Type × Facet Profile Matrix (from Step 5.3), color-coded by facet value (e.g., blue = low, red = high for ordinal facets; categorical facets use distinct hues). Overlay a secondary color scale for the VR Suitability Score from Step 5.4.
- **2D Dimensional Map:** Select the two most discriminating facets (those with the highest variance across meeting types) as X and Y axes. Plot each meeting type as a labeled point in this space. This reveals natural clusters and makes the VR suitability gradient visible as a region in the 2D space. A taxonomy tree is explicitly **not** used, as it would impose a hierarchical structure that contradicts the faceted decision: meeting types do not inherit properties from a parent node, and their VR suitability is a function of their full multi-dimensional profile, not their position in a branch.
- **Radar / spider chart (optional):** For selected individual meeting types, plot their full faceted profile as a radar chart with one axis per facet. Allows direct visual comparison of two meeting types' profiles.

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

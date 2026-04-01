# Role: Scientific Research Assistant
# Task: Systematic Merging, Deduplication, and Screening of Scopus Results

Please execute the following scientific workflow. All code and documentation must be in English. 
Consider the three subfolders 
01_tech_emotion, 02_taxonomy_dimensions, 03_charisma_leadership
as separate projects and perform all of the below independently in each separate subfolder. 

## Step 1: Data Consolidation & Deduplication
1. Scan the current directory for all CSV files (Title searches, Abstract searches, and corrected exports).
2. Merge all found CSV files into a single pandas DataFrame.
3. Perform a rigorous deduplication process using 'EID' or 'DOI' as the primary keys. If both are missing, use a normalized 'Title'.
4. Calculate and report the following statistics:
   - Total number of records across all files.
   - Number of duplicate records removed.
   - Final number of unique records for screening.

## Step 2: Methodological Documentation
1. Create a dedicated Markdown file named 'Search_and_Selection_Methodology.md'.
2. Read the search strategies and strings used from 'searchString.md'.
3. Document today's Scopus research process, including the search strings and the deduplication statistics calculated in Step 1.

## Step 3: Definition of Selection Criteria
Define clear Inclusion (IC) and Exclusion Criteria (EC) for the paper: "Analyzing the structural dimensions and taxonomy of professional business meetings."
- IC: Focus on professional/workplace context, meeting taxonomies, structural attributes, or task-based classifications.
- EC: Purely technical engineering/software papers without social/structural analysis, non-professional social interaction, or non-English/German publications.
- List these criteria in the 'Search_and_Selection_Methodology.md' file.

## Step 4: Systematic Screening & Justification
Analyze each unique record based on 'Title', 'Abstract', and 'Keywords'.
1. Create a Python script to perform the screening.
2. For every article, assign a 'Selection_Decision' (Included/Excluded).
3. Provide a 'Selection_Justification' (1-2 sentences) for every decision, explicitly linking it to the IC/EC codes.
4. Save the final results to 'screened_results.csv'.

## Step 5: Final Reporting
Update the 'Search_and_Selection_Methodology.md' with:
- A summary table of the screening results (Total included vs. excluded).
- The top 3 reasons for exclusion with their respective frequencies.

Please begin by merging the files and presenting the deduplication statistics.
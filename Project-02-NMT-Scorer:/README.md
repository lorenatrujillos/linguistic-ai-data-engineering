# Automated NMT Quality Scorer & Linguistic Auditor

## Project Overview
This project is a precision tool designed to evaluate **Machine Translation** quality. It moves beyond simple automated metrics by implementing a **hybrid evaluation layer** that combines mathematical scoring with custom linguistic heuristics, specifically tailored for the medical and clinical domain.

## Key Features
- **SacreBLEU Integration:** Industry-standard metric calculation for objective quality assessment.
- **Critical Error Detection:** A custom-built Python engine that identifies "false friends" and high-risk mistranslations (e.g., *Fast* -> *Rápido* vs *Ayuno*) that standard AI metrics often miss.
- **Actionable QA Reports:** Generates automated Excel reports with specific error flagging and suggested corrections to streamline the Post-editing workflow.

## The "SacreBLEU Paradox" (Analytical Insight)
During the development of this pipeline, I identified a critical limitation in the **SacreBLEU metric**:
* **The Issue:** Since BLEU relies on n-gram overlap (word-for-word matching), it often assigns high scores (e.g., >70) to sentences that contain **severe semantic errors**.
* **Example:** In the phrase *"Fast for 8 hours"*, a translation of *"Rápido"* instead of *"Ayune"* receives a high score because the rest of the sentence matches, even though the medical meaning is completely lost.
* **My Solution:** I engineered a **validation layer** to intercept these high-scoring but "fatally flawed" segments, ensuring data integrity for clinical safety.



## Tech Stack
- **Python** 3.13.5
- **Pandas:** For advanced data framing and report generation.
- **SacreBLEU:** For standardized MT evaluation.
- **Openpyxl:** For professional Excel output.

## How to Run
1. Generate the test dataset: 'nmt_generator.py'
2. Execute the quality auditor: 'nmt_scorer.py'
3. Review findings in: 'nmt-quality-report.xlsx'

## Why This Matters
Automated metrics are not enough for high-stakes industries like Healthcare. This tool demonstrates how **Linguistic Data Engineering** can bridge the gap between "machine-processed" and "human-reliable" AI outputs, reducing manual QA overhead by flagging the most critical risks automatically.

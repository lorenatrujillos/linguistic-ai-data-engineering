# Medical Prompt Engineering Framework: Clinical Trial ICFs

## Project Purpose
This project establishes a systematic framework for Prompt Design and Optimization within the medical localization industry. It focuses on the translation of Informed Consent Forms (ICFs) (high-stakes documents where terminology precision, formal register, and patient safety are paramount).

The goal is to demonstrate how structured prompting techniques (Role-Playing, Chain-of-Thought, and Few-Shot) significantly outperform baseline translations by enforcing regulatory compliance and professional medical tone.

## Methodology
I developed and compared two primary translation strategies to process an official World Health Organization (WHO) clinical trial template:

- Zero-Shot (Baseline): A direct translation request without specialized context or persona.

- Role-Playing + Chain-of-Thought (Optimized): A sophisticated framework that assigns the model the persona of a Senior Medical Quality Auditor. It forces the AI to analyze clinical risks and legal nuances before generating the Spanish output.

## Technical Architecture
The framework is built with the following structure:

- prompt_experiment.py: The Python engine that manages file paths, loads clinical data, and injects text into engineered templates.

- prompts/templates.json: A central repository for prompt versioning, allowing for logic updates without modifying the source code.

- data/source_text.txt: The raw source document (WHO ICF Phase III Template).

- outputs/: A directory containing the resulting translations from Zero-Shot and Role-Playing prompting techniques and the analysis report of these translations.

## Why This Matters
This project demonstrates that in a professional environment, AI is not used as a "black box" but as a precision tool guided by Linguistic Engineering. By structuring prompts as data (JSON) and scripts (Python), we ensure that AI outputs are predictable, auditable, and ready for clinical use.

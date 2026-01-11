## Automated Linguistic Data Cleaner

# Project Purpose
In the context of LLM Training, "garbage in, garbage out" is the golden rule. This module is a specialized ETL (Extract, Transform, Load) pipeline designed to sanitize raw medical bilingual datasets. It transforms noisy, unformatted Excel data into high-quality training pairs, ensuring that the model learns language patterns without being distracted by technical artifacts.

# Advanced Features & Logic
- HTML Artifact Stripping: Uses RegEx patterns to identify and remove nested HTML tags (e.g., '<b>', '<i>', '<span>') that often plague exported translation memories.
- Structural Validation: Automatically detects and drops incomplete segments (missing source or target) to prevent training bias.
- Whitespace Normalization: Cleans non-breaking spaces, tabs, and inconsistent line breaks often found in clinical exports.
- Deduplication Engine: Identifies and removes redundant entries to optimize the dataset size and improve model generalization.

# Tech Stack
- Python 3.13.5
- Pandas: High-speed data manipulation and duplicate detection.
- RegEx (re module): Advanced string pattern matching for noise removal.
- Openpyxl: Engine for professional Excel (.xlsx) file handling.

# Pipeline Workflow
1. Generation: 'excel_generator.py' simulates a "noisy" raw export from a Translation Management System.
2. Transformation: 'data_cleaner.py' applies the cleaning heuristics.
3. Verification: The system outputs 'cleaned-medical-dataset.xlsx' ready for AI fine-tuning.

# Why This Matters
By replacing manual cleaning with this automated pipeline:
- Accuracy: Eliminates human error in noise detection.
- Scalability: Capable of processing thousands of segments in seconds.
- Efficiency: Reduces the pre-processing phase of the localization workflow by an estimated **30 %**, allowing linguists to focus on high-level quality tasks.

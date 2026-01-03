import pandas as pd
import re

def clean_linguistic_data(input_file, output_file):
    """
    Linguistic Data Engineering script for cleaning 
    and validating medical bilingual datasets.
    """
    print(f"--- Starting Cleaning Pipeline: {input_file} ---")

    # 1. Load the Excel file
    try:
        # Now using openpyxl automatically to read .xlsx
        df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # 2. Data Integrity: Remove rows where Source or Target is missing
    initial_count = len(df)
    df = df.dropna(subset=['Source', 'Target'])
    print(f"Empty rows removed: {initial_count - len(df)}")

    # 3. Cleaning Function using RegEx
    def clean_text(text):
        if not isinstance(text, str):
            return text
        
        # Remove HTML tags (e.g., <b>, <i>)
        text = re.sub(r'<[^>]+>', '', text)
        
        # Normalize whitespace (tabs, newlines, multiple spaces)
        text = re.sub(r'\s+', ' ', text)
        
        # Leading and trailing spaces removal
        return text.strip()

    # Apply cleaning logic
    df['Source'] = df['Source'].apply(clean_text)
    df['Target'] = df['Target'].apply(clean_text)

    # 4. Deduplication: Remove repetitive entries
    before_dup = len(df)
    df = df.drop_duplicates()
    print(f"Duplicates removed: {before_dup - len(df)}")

    # 5. Quality Export
    df.to_excel(output_file, index=False)
    print(f"--- Process Completed ---")
    print(f"File saved as: {output_file}")
    print(f"Total clean segments: {len(df)}")

if __name__ == "__main__":
    # Updated filenames per your instructions
    input_filename = 'unprocessed-medical-dataset.xlsx'
    output_filename = 'cleaned-medical-dataset.xlsx'
    
    clean_linguistic_data(input_filename, output_filename)
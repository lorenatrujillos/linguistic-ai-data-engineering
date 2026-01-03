import pandas as pd
import sacrebleu

def calculate_nmt_quality(input_file, output_file):
    """
    Evaluates Machine Translation quality using BLEU and provides
    detailed feedback on critical terminology errors.
    """
    print(f"--- Starting NMT Evaluation Pipeline: {input_file} ---")

    # 1. Load the dataset
    try:
        df = pd.read_excel(input_file)
    except Exception as e:
        print(f"Error: Could not read file. {e}")
        return

    # 2. Define BLEU scoring logic
    def get_bleu_score(row):
        score = sacrebleu.sentence_bleu(str(row['Machine_Translation']), [str(row['Reference'])])
        return round(score.score, 2)

    # 3. Enhanced Critical Error Detection with Feedback
    def check_critical_errors(row):
        # Dictionary structure: 'source_term': (['forbidden_translations'], 'suggested_correction')
        critical_mistakes = {
            'fast': (['rápido',], 'ayune'),
            'store': (['tienda'], 'conservar/almacenar'),
            'stroke': (['golpe'], 'ictus/infarto/accidente cerebrovascular'),
            'subjects': (['temas'], 'sujetos (de estudio)'),
            'trial': (['juicio'], 'ensayo (clínico)'),
            'drug': (['droga'], 'fármaco/medicamento'),
            'side effects': (['efectos de lado'], 'efectos secundarios')
        }
        
        source_text = str(row['Source']).lower()
        mt_text = str(row['Machine_Translation']).lower()
        
        for term, (forbidden_list, correction) in critical_mistakes.items():
            if term in source_text:
                for forbidden in forbidden_list:
                    if forbidden in mt_text:
                        # Returns detailed feedback
                        return f"CRITICAL ERROR: '{term}' misused. Use '{correction}' instead."
        
        return ""

    # 4. Processing
    print("Calculating scores and generating detailed feedback...")
    df['BLEU_Score'] = df.apply(get_bleu_score, axis=1)
    df['Validation_Status'] = df.apply(check_critical_errors, axis=1)

    # 5. Export results
    try:
        df.to_excel(output_file, index=False)
        
        avg_bleu = df['BLEU_Score'].mean()
        critical_count = len(df[df['Validation_Status'] != ""])
        
        print(f"--- Evaluation Completed ---")
        print(f"Average BLEU Score: {avg_bleu:.2f}")
        print(f"Detailed Errors found: {critical_count}")
        print(f"Final report saved as: {output_file}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    input_filename = 'nmt-evaluation-dataset.xlsx'
    output_filename = 'nmt-quality-report.xlsx'
    
    calculate_nmt_quality(input_filename, output_filename)
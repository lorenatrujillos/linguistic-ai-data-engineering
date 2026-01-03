import pandas as pd

def generate_unprocessed_dataset():
    """
    Generates a raw medical bilingual dataset with structural noise 
    for testing the Linguistic Data Engineering pipeline.
    """
    print("Generating raw dataset...")

    # Bilingual medical data with strategic errors (HTML, whitespace, duplicates, NaNs)
    medical_data = {
        'Source': [
            'The patient was diagnosed with <b>Type 2 Diabetes</b>.  ', # HTML + Trailing spaces
            'Follow-up appointment scheduled for next  Tuesday.',      # Double spaces
            None,                                                      # Missing entry (NaN)
            'Administer 50mg of Aspirin daily.',                      # Duplicate 1
            'Administer 50mg of Aspirin daily.',                      # Duplicate 2
            '  Check blood pressure levels.',                          # Leading spaces
            'Patient exhibits symptoms of <i>acute rhinitis</i>.',      # HTML tags
            'The clinical trial showed a 95% success rate. ',          # Extra space
            'Chronic  obstructive pulmonary disease (COPD).',          # Noise
            '<b>WARNING:</b> High dosage may cause side effects.'      # Critical tags
        ],
        'Target': [
            'El paciente fue diagnosticado con <b>diabetes tipo 2</b>.  ',
            'Cita de seguimiento programada para el próximo  martes.',
            'Traducción huérfana',                                     
            'Administrar 50 mg de aspirina al día.',
            'Administrar 50 mg de aspirina al día.',
            '  Comprobar los niveles de presión arterial.',
            'El paciente presenta síntomas de <i>rinitis aguda</i>.',
            'El ensayo clínico mostró una tasa de éxito del 95 %. ',
            'Enfermedad  pulmonar obstructiva crónica (EPOC).',
            '<b>ADVERTENCIA:</b> Dosis altas pueden causar efectos secundarios.'
        ]
    }

    # Create DataFrame
    df = pd.DataFrame(medical_data)

    # Save as Excel using openpyxl
    try:
        output_name = 'unprocessed-medical-dataset.xlsx'
        df.to_excel(output_name, index=False)
        print(f"Success! '{output_name}' has been created with raw linguistic data.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    generate_unprocessed_dataset()


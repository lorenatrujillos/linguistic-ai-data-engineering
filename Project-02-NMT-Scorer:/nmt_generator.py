import pandas as pd

def generate_nmt_test_data():
    """
    Generates an expanded dataset to test NMT quality scoring.
    Includes 20 medical/technical segments with diverse quality levels.
    """
    print("Generating expanded raw dataset (20 segments)...")

    data = {
        'Source': [
            'The patient requires immediate surgery.',
            'Keep out of reach of children.',
            'Adverse reactions may include dizziness.',
            'Store in a cool, dry place.',
            'The clinical trial was conducted over six months.',
            'Symptoms include fever, cough, and fatigue.',
            'Apply a small amount to the affected area.',
            'Do not exceed the recommended dose.',
            'Blood samples were collected every four hours.',
            'The drug is contraindicated during pregnancy.',
            'Patients reported significant improvement.',
            'Discontinue use if a rash develops.',
            'The study results are statistically significant.',
            'High blood pressure is a risk factor for stroke.',
            'Ensure the device is properly calibrated.',
            'Long-term side effects are still unknown.',
            'Fast for at least 8 hours before the test.',
            'The treatment was well tolerated by the subjects.',
            'Review the patient’s medical history.',
            'Wash hands thoroughly before application.'
        ],
        'Reference': [
            'El paciente requiere cirugía inmediata.',
            'Manténgase fuera del alcance de los niños.',
            'Las reacciones adversas pueden incluir mareos.',
            'Conservar en un lugar fresco y seco.',
            'El ensayo clínico se realizó durante seis meses.',
            'Los síntomas incluyen fiebre, tos y fatiga.',
            'Aplique una pequeña cantidad en la zona afectada.',
            'No exceder la dosis recomendada.',
            'Se recogieron muestras de sangre cada cuatro horas.',
            'El fármaco está contraindicado durante el embarazo.',
            'Los pacientes informaron de una mejora significativa.',
            'Suspenda su uso si aparece una erupción.',
            'Los resultados del estudio son estadísticamente significativos.',
            'La hipertensión es un factor de riesgo de infarto.',
            'Asegúrese de que el dispositivo esté bien calibrado.',
            'Los efectos secundarios a largo plazo aún se desconocen.',
            'Ayune al menos 8 horas antes de la prueba.',
            'El tratamiento fue bien tolerado por los sujetos.',
            'Revise el historial médico del paciente.',
            'Lávese bien las manos antes de la aplicación.'
        ],
        'Machine_Translation': [
            'El paciente requiere cirugía inmediata.',      # Match
            'Mantener lejos de los niños.',                 # Different wording
            'Reacciones adversas incluir mareos.',          # Grammar error
            'Tienda en un lugar fresco y seco.',             # Mistranslation (Store)
            'El juicio clínico fue conducido sobre seis meses.', # Literal/Wrong context
            'Los síntomas incluyen fiebre, tos y fatiga.',  # Match
            'Aplicar una pequeña cantidad al área afectada.', # Good
            'No exceda la dosis recomendada.',              # Good
            'Muestras de sangre fueron colectadas cada cuatro horas.', # Passive/Anglicism
            'La droga está contraindicada durante el embarazo.', # 'Drug' as 'Droga'
            'Pacientes reportaron mejora significativa.',    # Missing articles
            'Deje de usarlo si aparece un sarpullido.', # Good
            'Los resultados del estudio son estadísticamente significativos.', # Match
            'La hipertensión es un factor de riesgo para el golpe.', # Mistranslation (Stroke)
            'Asegurar el aparato es propiamente calibrado.', # Grammar/Vocabulary
            'Efectos de lado de largo término son todavía desconocidos.', # Calque/Literal
            'Rápido durante al menos 8 horas antes de la prueba.',   # Mistranslation (Fast)
            'El tratamiento fue bien tolerado por los temas.', # Mistranslation (Subjects)
            'Revise la historia médica del paciente.',      # Good
            'Lavar manos a fondo antes de la aplicación.'    # Grammar
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_excel('nmt-evaluation-dataset.xlsx', index=False)
    print("Test file 'nmt-evaluation-dataset.xlsx' created with 20 segments.")

if __name__ == "__main__":
    generate_nmt_test_data()
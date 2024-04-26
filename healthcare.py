import pandas as pd

# Create the DataFrame
data = {
    'Patient ID': list(range(1, 51)),
    'Age': [45, 32, 60, 55, 68, 42, 50, 47, 58, 35, 
            62, 40, 48, 52, 65, 38, 56, 44, 70, 30, 
            57, 36, 49, 42, 61, 33, 53, 46, 63, 39, 
            51, 43, 67, 31, 54, 41, 59, 34, 64, 37, 
            55, 50, 66, 40, 48, 52, 69, 29, 58, 45],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female', 
               'Male', 'Female', 'Male', 'Female', 'Male', 
               'Female', 'Male', 'Female', 'Male', 'Female'],
    'Diagnosis': ['Hypertension', 'Diabetes', 'Coronary Artery Disease', 
                  'Hyperlipidemia', 'Hypertension', 'Thyroid Disorder', 
                  'Type 2 Diabetes', 'Obesity', 'Hypertension', 'Asthma', 
                  'Atrial Fibrillation', 'Migraine', 'Hypertension', 
                  'Type 2 Diabetes', 'Hyperlipidemia', 'Hypertension', 
                  'Type 2 Diabetes', 'Thyroid Disorder', 'Hypertension', 
                  'Obesity', 'Hypertension', 'Type 1 Diabetes', 
                  'Hyperlipidemia', 'Hypertension', 'Asthma', 
                  'Hypertension', 'Type 2 Diabetes', 'Hypothyroidism', 
                  'Hypertension', 'Coronary Artery Disease', 'Hypertension', 
                  'Type 2 Diabetes', 'Hypertension', 'Hyperlipidemia', 
                  'Type 2 Diabetes', 'Hypertension', 'Thyroid Disorder', 
                  'Obesity', 'Hypertension', 'Type 2 Diabetes', 
                  'Hyperlipidemia', 'Hypertension', 'Thyroid Disorder', 
                  'Hypertension', 'Type 2 Diabetes', 'Hyperlipidemia', 
                  'Hypertension', 'Type 1 Diabetes', 'Hyperlipidemia', 
                  'Hypertension'],
    'Blood Pressure': ['140/90', '130/80', '150/95', '135/85', '145/92', 
                       '120/75', '140/85', '150/95', '130/80', '125/78', 
                       '140/88', '130/82', '145/90', '135/85', '150/92', 
                       '125/80', '140/88', '130/82', '145/95', '150/90', 
                       '140/88', '130/82', '155/95', '125/80', '140/90', 
                       '130/82', '145/88', '135/85', '150/95', '130/80', 
                       '140/90', '135/85', '145/92', '130/82', '140/88', 
                       '125/78', '150/95', '125/78', '140/90', '130/82', 
                       '145/92', '120/75', '140/88', '150/95', '130/80', 
                       '145/92', '140/88', '150/95', '130/80'],
    'Cholesterol': [210, 190, 240, 220, 200, 180, 230, 250, 210, 190, 
                    220, 180, 240, 200, 230, 190, 250, 220, 210, 190, 
                    240, 200, 220, 180, 220, 210, 250, 220, 200, 190, 
                    240, 210, 250, 180, 190, 240, 210, 250, 220, 190, 
                    240, 220, 200, 230, 240, 220, 210, 190, 230],
    'Glucose': [110, 120, 130, 115, 125, 100, 135, 130, 115, 100, 
                120, 110, 125, 130, 135, 115, 120, 125, 130, 105, 
                120, 125, 130, 115, 125, 110, 135, 120, 125, 130, 
                115, 120, 125, 110, 130, 120, 125, 130, 115, 125, 
                110, 130, 120, 125, 130, 110, 125, 120],
    'Hemoglobin': [15.5, 13.2, 14.8, 16.2, 14.0, 13.5, 15.8, 13.0, 16.5, 
                   14.3, 15.1, 13.9, 16.8, 12.5, 15.3, 14.7, 13.2, 14.9, 
                   15.6, 13.8, 16.1, 12.6, 15.0, 14.4, 15.9, 13.3, 15.2, 
                   13.7, 16.3, 14.6, 15.7, 13.1, 16.0, 14.2, 15.5, 13.6, 
                   16.4, 14.5, 15.8, 12.9, 16.6, 14.1, 15.4, 13.8, 16.2, 
                   14.7, 15.9, 13.5, 16.8, 14.3]
}

df = pd.DataFrame(data)

# Convert Blood Pressure to systolic and diastolic columns
df[['Systolic BP', 'Diastolic BP']] = df['Blood Pressure'].str.split('/', expand=True)
df['Systolic BP'] = df['Systolic BP'].astype(int)
df['Diastolic BP'] = df['Diastolic BP'].astype(int)
df.drop(columns=['Blood Pressure'], inplace=True)

# Display basic statistics
print("Basic Statistics:")
print(df.describe())

# Count by Gender
gender_count = df['Gender'].value_counts()
print("\nCount by Gender:")
print(gender_count)

# Count by Diagnosis
diagnosis_count = df['Diagnosis'].value_counts()
print("\nCount by Diagnosis:")
print(diagnosis_count)

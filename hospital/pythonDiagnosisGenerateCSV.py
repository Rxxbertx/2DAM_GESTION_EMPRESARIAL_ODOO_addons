import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# Generar datos para los diagnósticos
diagnoses_data = []
for _ in range(20):  # Generar 20 diagnósticos
    diagnosis = {
        'name': "Diagnosis "+_.__str__(),  # Nombre del diagnóstico
        'date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),  # Fecha aleatoria en el último año
        'description': fake.text(),  # Descripción aleatoria
    }
    diagnoses_data.append(diagnosis)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.diagnosis.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name', 'date', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for diagnosis in diagnoses_data:
        writer.writerow(diagnosis)

print(f"Se han generado los datos de los diagnósticos en el archivo '{csv_filename}'.")

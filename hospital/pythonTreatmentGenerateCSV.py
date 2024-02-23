import csv
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker()

# Generar datos para los tratamientos
treatments_data = []
for _ in range(20):  # Generar 20 tratamientos
    treatment = {
        'name': fake.word(),  # Nombre del tratamiento
        'date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),  # Fecha aleatoria en el último año
        'description': fake.text(),  # Descripción aleatoria
    }
    treatments_data.append(treatment)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.treatment.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name', 'date', 'description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for treatment in treatments_data:
        writer.writerow(treatment)

print(f"Se han generado los datos de los tratamientos en el archivo '{csv_filename}'.")

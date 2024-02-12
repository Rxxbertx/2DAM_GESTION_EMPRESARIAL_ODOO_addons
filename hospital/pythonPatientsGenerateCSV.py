import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


# Función para generar una fecha de nacimiento aleatoria
def generate_date_of_birth():
    end_date = datetime.now() - timedelta(days=365 * 18)  # Hace que los pacientes tengan al menos 18 años
    start_date = end_date - timedelta(days=365 * 90)  # Hace que los pacientes tengan hasta 90 años
    return fake.date_between(start_date=start_date, end_date=end_date)


# Generar datos para 1000 pacientes extendidos
patients_data = []
for _ in range(20):
    name = fake.first_name()
    last_name = fake.last_name()
    date_of_birth = generate_date_of_birth()
    gender = random.choice(['male', 'female', 'other'])
    address = fake.address()
    phone = fake.phone_number()
    allergies = fake.sentence(nb_words=6)
    preexisting_conditions = fake.sentence(nb_words=8)
    social_security_number = fake.ssn()

    patient = {
        'name': name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'gender': gender,
        'address': address,
        'phone': phone,
        'allergies': allergies,
        'preexisting_conditions': preexisting_conditions,
        'social_security_number': social_security_number,
        'bed_id': None,
        'doctor_id': None,
    }
    patients_data.append(patient)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.extended.patient.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name', 'last_name', 'date_of_birth', 'gender', 'address', 'phone', 'allergies',
                  'preexisting_conditions', 'social_security_number', 'bed_id', 'doctor_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for patient in patients_data:
        writer.writerow(patient)

print(f"Se han generado los datos de 20 pacientes extendidos en el archivo '{csv_filename}'.")
# Output: Se han generado los datos de 20 pacientes extendidos en el archivo 'hospital.extended.patient.csv'.

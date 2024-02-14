import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()


# Función para generar una especialización aleatoria
def generate_specialization():
    specializations = ['Cardiology', 'Dermatology', 'Emergency Medicine', 'Gastroenterology', 'Neurology']
    return random.choice(specializations)


def generate_gender():
    gender = ['male', 'female', 'other']
    return random.choice(gender)


def generate_date_of_birth():
    end_date = datetime.now() - timedelta(days=365 * 18)  # Hace que los pacientes tengan al menos 18 años
    start_date = end_date - timedelta(days=365 * 90)  # Hace que los pacientes tengan hasta 90 años
    return fake.date_between(start_date=start_date, end_date=end_date)


# Generar datos para los médicos
doctors_data = []
for _ in range(20):  # Generar 20 médicos
    doctor = {
        'name': fake.first_name(),  # Nombre del médico
        'last_name': fake.last_name(),  # Apellido del médico
        'specialization': generate_specialization(),  # Especialización del médico
        'work_schedule': float(round(random.uniform(4, 10), 2)),  # Horario de trabajo del médico
        'phone': fake.phone_number(),  # Teléfono del médico
        'email': fake.email(),  # Correo electrónico del médico
        'date_of_birth': generate_date_of_birth(),  # Fecha de nacimiento del médico
        'gender': generate_gender(),
    }
    doctors_data.append(doctor)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.doctor.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name', 'last_name', 'specialization', 'work_schedule', 'phone', 'email', 'date_of_birth', 'gender']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for doctor in doctors_data:
        writer.writerow(doctor)

print(f"Se han generado los datos de los médicos en el archivo '{csv_filename}'.")

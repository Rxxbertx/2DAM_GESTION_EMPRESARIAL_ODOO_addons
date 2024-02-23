import csv
import random
from faker import Faker

fake = Faker()


# Función para generar un estado y tipo de cama aleatorio
def generate_bed_state_and_type():
    types = ['normal', 'intensive_care', 'pediatric']
    return random.choice(types)


# Generar datos para las camas y asociarlas con las plantas correspondientes
beds_data = []
for i in range(1, 6):  # Para cada planta
    for _ in range(random.randint(1, 50)):  # Generar un número aleatorio de camas
        bed_type = generate_bed_state_and_type()
        bed = {
            'name': "Bed"+_.__str__()+"-"+i.__str__(),  # Nombre de la cama
            'floor_id.id': i,  # ID de la planta asociada
            'state': 'available',  # Estado de la cama
            'type': bed_type,  # Tipo de cama
        }
        beds_data.append(bed)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.bed.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name', 'floor_id.id', 'state', 'type']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for bed in beds_data:
        writer.writerow(bed)

print(f"Se han generado los datos de las camas en el archivo '{csv_filename}'.")

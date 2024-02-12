import csv

from faker import Faker

fake = Faker()

# Generar datos para 5 plantas
floors_data = []
for i in range(1, 6):  # Para cada planta
    name = fake.word()  # Nombre de la planta

    floor = {
        'name': name,
    }
    floors_data.append(floor)

# Escribir los datos en un archivo CSV
csv_filename = 'data/hospital.floor.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for floor in floors_data:
        writer.writerow(floor)

print(f"Se han generado los datos de 5 plantas en el archivo '{csv_filename}'.")

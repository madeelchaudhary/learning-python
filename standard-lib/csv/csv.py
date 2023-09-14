from csv import reader, writer

# Write a CSV file
with open('fighters.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['Character', 'Move'])
    csv_writer.writerow(['Ryu', 'Hadouken'])

# Read a CSV file
with open('fighters.csv') as file:
    csv_reader = reader(file)
    for row in csv_reader:
        print(row)

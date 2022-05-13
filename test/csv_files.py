import csv

with open("data.csv", 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

with open("data.csv", 'a', newline = '') as f:
    writer = csv.writer(f)
    row = ['3', 'Kevin', 'Durant']
    writer.writerow(row)

with open("data.csv", 'r') as f:
    csv_file = csv.DictReader(f)
    for row in csv_file:
        print(dict(row))

import csv

with open('flight_rasp_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flights = []
    x = []
    for row in reader:
        flights.append(row['cco_hash'])
        
import csv


with open('flight_rasp_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flights = []
    x =[]
    for row in reader:
        flights.append(row['departure_terminal'])
    def fl():
        fl1 = [0, 0]
        for i in flights:
            if i == 'B':
                fl1[0] += 1
            else:
                fl1[1] += 1
        return fl
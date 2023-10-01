import csv

with open('flight_rasp_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = []
    x = []
    for row in reader:
        data.append(row['t_st'])


    def flights_per_day():
        count = 0
        flp = []
        for i in range(len(data)):
            if i < len(data) - 1:
                if data[i][:2] == data[i+1][:2]:
                    count += 1
                else:
                    flp.append(count)
                    count = 0
        return flp


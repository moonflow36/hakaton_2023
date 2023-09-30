import csv
with open('bsm_data_train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    times = []
    passangers = []
    for row in reader:
        times.append(row['MessageReceivedDate'])
    times = sorted(times)
    def per_hour():
        count = 1
        per_hour = []
        for i in range(len(times)):
            if i < len(times) - 1:
                if times[i][11:13] == times[i+1][11:13]:
                    count += 1
                else:
                    passangers.append(count)
                    count = 1
        print(len(passangers)) # пассажиры в час

        for i in range(24):
            per_hour.append([])


        for i in range(len(passangers)):
            v = i % 24
            per_hour[v].append(passangers[i])


        n = []
        for i in per_hour:
            n.append(sum(i) // len(i))

        return n


    with open('passangers_hour.csv', 'w') as f:
        writer = csv.writer(f)
        for row in per_hour():
            writer.writerow(str(row))

import csv
with open('bsm_data_test.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    times = []
    for row in reader:
        times.append(row['MessageReceivedDate'])
    times = sorted(times)
    def per_hour():
        count = 1
        passangers = []
        per_hour = []
        for i in range(len(times)):
            if i < len(times) - 1:
                if times[i][:2] == times[i+1][:2]:
                    count += 1
                else:
                    passangers.append(count)
                    count = 1


        for i in range(24):
            per_hour.append([])


        for i in range(len(passangers)):
            v = i % 24
            per_hour[v].append(passangers[i])


        n = []
        for i in per_hour:
            n.append(sum(i) // len(i))

        return n


    def day():
        days = []
        for i in per_hour():
            days.append(i * 24)
        return days


    with open('passangers_hour.csv', 'w') as f:
        writer = csv.writer(f)
        for row in per_hour():
            writer.writerow(str(row))



import csv

with open('bsm_data_train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    baggages = []
    x =[]
    for row in reader:
        baggages.append(row['MessageReceivedDate'])
    baggages = sorted(baggages)
    bag1 = []

    def count_baggages_per_day():
        c = []
        bag1 =[]
        coun = 0
        count = 0
        count_bag = []
        mx_bag = 0
        mn_bag = 0
        avg_bag = 0
        forecast_mn_baggage = []
        forecast_mx_baggage = []
        for i in range(len(baggages)):
            if i < len(baggages)-1:
                if baggages[i][8:10] == baggages[i + 1][8:10]:
                    count += 1
                    coun += 1
                else:
                    c.append(baggages[i][:10])
                    c.append(str(coun))
                    bag1.append(coun)
                    count_bag.append(count)
                    c = []
                    coun = 0
        mx_bag = max(bag1)
        mn_bag = min(bag1)
        avg_bag = sum(bag1) // len(bag1)
        forecast_bag = []
        for i in bag1:
            forecast_mn_baggage.append(i-(avg_bag-mn_bag))
        for i in bag1:
            forecast_mx_baggage.append(i + (mx_bag-avg_bag))
        for i in range(len(bag1)):
            forecast_bag.append(forecast_mx_baggage[i] - ((forecast_mx_baggage[i] - forecast_mn_baggage[i])) // 2)

        forecast = []
        forecast.append(forecast_mx_baggage)
        forecast.append(forecast_mn_baggage)
        forecast.append(bag1)
        forecast.append(forecast_bag)

        b = []
        for i in range(len(forecast_mx_baggage)):
            b.append([])
        for i in range(len(forecast_mx_baggage)):
            b[i].append(forecast_mx_baggage[i])
            b[i].append(forecast_mn_baggage[i])
            b[i].append(bag1[i])
            b[i].append(forecast_bag[i])

        return b



    with open('forecast.csv', 'w') as f:
        writer = csv.writer(f)
        for row in count_baggages_per_day():
            writer.writerow(row)

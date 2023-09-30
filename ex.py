import csv
with open('bsm_data_train.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    baggages = []
    for row in reader:
        baggages.append(row['MessageReceivedDate'])


with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    for row in baggages:
        writer.writerow(row)
print('ready')






'''bagi = []
    avg_days = []
    for i in range(7):
        b = []
        bagi.append(b)
    for i in range(len(count_bag)):
        if i % 7 == 0:
            bagi[5].append(bag1[i])
        elif i % 7 == 1:
            bagi[6].append(bag1[i])
        elif i % 7 == 2:
            bagi[0].append(bag1[i])
        elif i % 7 == 3:
            bagi[1].append(bag1[i])
        elif i % 7 == 4:
            bagi[2].append(bag1[i])
        elif i % 7 == 5:
            bagi[3].append(bag1[i])
        elif i % 7 == 6:
            bagi[4].append(bag1[i]) #дни недели - багажи за каждый день

    for i in range(7):
       avg_days.append(sum(bagi[i]) // len(bagi[i]))
    print(avg_days)'''

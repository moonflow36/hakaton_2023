import csv

with open('flight_rasp_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    flights = []
    data = []
    for row in reader:
        flights.append(row['cco_hash'])
    for row in reader:
        data.append(row['t_st'])
    list_for_company = ["f7adf0ba18d705092fa0a1e2f2c0bafb", "e2fca8135c2fadca093abd79a6b1c0d2", "655610c16fda311d29ed2360a1ffcbd1"]
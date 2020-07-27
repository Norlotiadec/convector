from datetime import datetime
import csv

data = []
data_mask1 = []
with open('acme_worksheet.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        data.append(row)
        data_mask1.append(row)
data_mask = []
data_mask1.pop(0)
print(data)
for i in data:
    if i[1] != 'Date':
        dt = datetime.strptime(i[1], "%b %d %Y")
        data_mask.append(dt.strftime('%Y-%m-%d'))
    for j in data_mask1:
        if i[0] == j[0] and i[1] == j[1]:
            print(i[0], j[0])
print(sorted(set(data_mask)))
print(data_mask1)

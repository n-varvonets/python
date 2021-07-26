import csv

with open('data/output1.csv', 'w') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_ALL)  # QUOTE_ALL
    writer.writerow((['1','2','3']))
    writer.writerow((['1','2','4']))
    writer.writerow((['1','2','5']))
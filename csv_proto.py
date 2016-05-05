import csv
reader = csv.reader(open('foo.csv', 'rb'))
for row in reader:
    print row

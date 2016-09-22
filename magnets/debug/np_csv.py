import csv

csv_file = open('test.csv')
csv_reader = csv.reader(csv_file)

for row in csv_reader:
    print('Row ' + str(csv_reader.line_num) + ': ' + str(row))

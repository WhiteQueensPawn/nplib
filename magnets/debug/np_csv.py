import csv

csv_input_file = open('input.csv')
csv_reader = csv.reader(csv_input_file)

csv_output_file = open('output.csv', 'w')
csv_writer = csv.writer(csv_output_file)

for row in csv_reader:
    csv_writer.writerow(list(csv_reader))

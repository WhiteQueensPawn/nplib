import csv

csvFile = open('test.csv')
csvReader = csv.reader(csvFile)
csvData = list(csvReader)
print csvData

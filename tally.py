# Python snippet to parse csv with first line as
# keywords and return totals of columns in the 
# following lines

import csv

def tally(filename=None):
	print (filename)
	reader = csv.reader(open(filename if filename != '.csv' and filename != None else 'tally.csv'))
	keys = [key for key in next(reader)]
	print (keys)

	dict_values = {}

	for key in keys:
		dict_values[key] = 0

	for row in  reader:
		for key in dict_values:
			dict_values[key] += int(row[keys.index(key)])

	print (dict_values)

def main():
	tally()

if __name__ == '__main__':
	main()
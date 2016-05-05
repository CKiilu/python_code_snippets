import csv
import tally

filename = input("Choose csv filename: ") +'.csv'
if filename != '.csv':
	row = []

	with open(filename, 'a') as f:
		stop = input("Press 'q' to stop: ")
		if stop.lower() != 'q':
			columns = int(input("Number of columns: "))
			count_rows = 0
			while stop.lower() != "q":
				for column in range(columns):
					row.append(input('Column ' + str(column + 1) + ' value: '))
				csv_writer = csv.writer(f)
				csv_writer.writerow(row)
				row = []
				stop = input("Press 'q' to stop: ")

tally.tally(filename)
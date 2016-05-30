import re


def main():
	# Open files
	N = open('cust.txt', 'r')
	Q = open('queries.txt', 'r')
	# Read lines of the files
	ls = N.readlines()
	qs = Q.readlines()
	# Remove newline from ends of strings
	queries = list(remove_new_lines(qs))
	lines = list(remove_new_lines(ls))
	queries_as_list = list(get_query(queries))
	found_vals = parse_data(queries_as_list, queries, lines)
	print found_vals

def remove_new_lines(array):
	for item in array:
		if bool(re.search('\n', item)):
			item = item.replace('\n', "")
		if not bool(re.search('</', item)):
			yield item

def get_query(array):
	for item in array:
		item = item.split('.')
		item = item[len(item)-1]
		item = item.split('~')
		yield item

def parse_data(queries_as_list, query_actual_values, lines):
	found_vals = {}
	searches = query_actual_values

	# Find existing query values
	for line in lines:
		for query in queries_as_list:
			if bool(re.search(query[0], line)) and bool(re.search(query[1], line)):
				for val in line.split(" "):
					if re.search(query[1], val):
						val = val.split('"')
						val = val[len(val)-2]
						index = queries_as_list.index(query)
						found_vals[searches[index]] = val
		
	# Show unfound values
	for value in searches:
		if not value in found_vals.keys():
			found_vals[value] = "Your query is invalid."

	return found_vals

if __name__ == '__main__':
	main()
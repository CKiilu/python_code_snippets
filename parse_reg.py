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
	
	for l in lines:
		for q in queries_as_list:
			if bool(re.search(r'{}'.format(q[0]), l)):
				if bool(re.search(r'{}'.format(q[1]), l)):
					res = re.search(r'(?<={}=")\S+(?=")'.format(q[1]), l)
					if res: print res.group()

	# found_vals = parse_data(queries_as_list, queries, lines)
	# print found_vals

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

if __name__ == '__main__':
	main()
def main():
	with open('num_5.txt', 'r') as f:
		first = f.next()
		for line in f:			
			line = line.replace('\n', '')
			if len(line) > 1:
				line = line.split(' ')
				length = len(line)
				large = largest(line)
				get_subset(line)
				
				# if rel_prime(line, large):
				# 	print("NO")
				# else:
				# 	print("YES")
				# print(line)


def largest(lst):
	"""Gets  largest value in list"""
	lg = lst[0]
	for val in lst:
		lg = val if val > lg else lg
	return int(lg)

def rel_prime(lst, large):
	"""Finds if numbers in list are relatively prime"""
	for divisor in range(1, large):
		if all([int(val) % divisor for val in lst]) == True:
			return True

def get_subset(lst):
	print(lst)
	# return lst	


if __name__ == '__main__':
	main()
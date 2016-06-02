def main():
	with open('num_6.txt', 'r') as f:
		first = f.next()
		count = 1
		for line in f:
			line = int(line.replace('\n', ''))
			iter_num = list(str(line))
			if rotate(iter_num, len(iter_num)) == True:
				print("divisible")
			else:
				print('Not')

def rotate(lst, ntimes):
	if ntimes > 0:		
		lst.insert(0, lst.pop(-1))
		temp_num = int("".join(lst))
		if temp_num % 8 == 0:
			return True
		else:
			return rotate(lst, ntimes-1)


if __name__ == '__main__':
	main()
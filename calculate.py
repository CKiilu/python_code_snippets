#!/usr/bin/python3
# Script for a simple calculator


def calculate():
	pass

def add(nums):
	total = 0
	for num in nums:
		total += num
	return total

def main():
	arr = []
	number = input('Type Number> ')
	arr.append(number if type(number) == type(1.3) or type(number) == type(4) else 0)
	print(add(arr))			

if __name__ == '__main__':
	main()
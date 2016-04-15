def r_fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return r_fib(n - 1) + r_fib(n - 2)

def i_fib(n):
	a, b = 0, 1
	for count in range(n):
		a, b = b, a + b
	return a

def main():
	print "R", r_fib(5)
	print "I", i_fib(5)

if __name__ == '__main__':
	main()
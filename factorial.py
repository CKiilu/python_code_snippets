
# Create both a recursive function called recursive_factorial 
# and iterative function called iterative_factorial that does the 
# following

# Accepts as parameter an Integer n
# Computes the factorial of n
# Returns the factorial of n
def recursive_factorial(n):
	if n < 2:
		return 1
	else:
		return n * recursive_factorial(n - 1)

def iterative_factorial(n):
	factorial = 1
	for x in range(1, n + 1):
		factorial *= x
	return factorial

def main():
	print iterative_factorial(0)
	print recursive_factorial(0)

if __name__ == '__main__':
	main()
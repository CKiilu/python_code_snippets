# Create a function get_algorithm_result to implement the algorithm below

# Get a list of numbers L1, L2, L3....LN as argument
# Assume L1 is the largest, Largest = L1
# Take next number Li from the list and do the following
# If Largest is less than Li
# Largest = Li
# If Li is last number from the list then
# return Largest and come out
# Else repeat same process starting from step 3
# Create a function prime_number that does the following

# Takes as parameter an integer and
# Returns boolean value true if the value is prime or
# Returns boolean value false if the value is not prime
import math

def get_algorithm_result():
	pass
def prime_number(num):
	return all( num % x for x in range(2, num))
def main():
	print prime_number(4)
	print prime_number(5)

if __name__ == '__main__':
	main()
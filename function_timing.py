
from timeit import Timer
from fibonacci import r_fib, i_fib

t1 = Timer("r_fib(10)","from fibo import r_fib")

total_for_iterative = 0

for i in range(1,41):
	s = "r_fib(" + str(i) + ")"
	t1 = Timer(s,"from fibonacci import r_fib")
	time1 = t1.timeit(3)
	s = "i_fib(" + str(i) + ")"
	t2 = Timer(s,"from fibonacci import i_fib")
	time2 = t2.timeit(3)
	total_for_iterative += time2
	print("n=%2d, r_fib: %8.6f, i_fib:  %7.6f, percent: %10.2f" % (i, time1, total_for_iterative, time1/time2))

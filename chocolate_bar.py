with open('num_7.txt', 'r') as f:
	first = f.next()
	for line in f:
		line = int(line.replace('\n', ''))
		x = line / 2
		y = x if line % 2 == 0 else x + 1
		
		size = x  * y
		print ("Line{}".format(line))
		print ("x:{}, y:{}, Size:{}".format(x,y,size))
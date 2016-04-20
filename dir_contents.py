def print_dir_contents(Path):
	import os 
	for child in os.listdir(Path):
		child_path = os.path.join(Path, child)
		if os.path.isdir(child_path):
			print_dir_contents(child_path)
		else:
			print (child_path)

def main():
	print_dir_contents(input("Path: "))

if __name__ == '__main__':
	main()
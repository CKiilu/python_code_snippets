# Create a function manipulate_data that does the following

# Accepts as the first parameter a string specifying the data structure to be used "list", "set" or "dictionary"
# Accepts as the second parameter the data to be manipulated based on the data structure specified e.g [1, 4, 9, 16, 25] for a list data structure
# Based off the first parameter
# return the reverse of a list or
# add items `"ANDELA"`, `"TIA"` and `"AFRICA"` to the set and return the resulting set
# return the keys of a dictionary.
def manipulate_data(data_type, data):
	if data_type.lower() == "list":
		return list(reversed(data))
	elif data_type.lower() == "set":
		data = set(data)
		data.update(["ANDELA", "TIA", "AFRICA"])
		return data
	elif data_type.lower() == "dictionary":
		return data.keys()

def main():
	print manipulate_data("list", [0,1,2,3,4,5,6,78,9])
	print manipulate_data("set", ["holere", "holere", "kuholela", "ffhs", 1, 2])
	print manipulate_data("dictionary", {"asdf": 1, "wer": 2, "wert":"sdfgh"})

if __name__ == '__main__':
	main()
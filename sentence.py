def err_bob(string):
    #your code here
    import re
    new_string = re.findall(r"[\w']+|[.,!?;]", string)
    arr = []
    for word in new_string:
        if word[-1] not in 'aeiouAEIOU.,?!;:()':
            if word[-1].isupper():
                word += 'ERR'
            else:
                word += 'err'
        arr.append(word)
    final = ''
    count = 0
    for word in arr:
    	if word[-1] in '.,?!;:()':
    		final += word
    	else:
    		final += word if count == 0 else ' ' + word
    	count += 1
    			
    print ( final)
    

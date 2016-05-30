import re

# Open files
N = open('htm.txt', 'r')
# Read lines of the files
ls = N.readlines()

lines = []
for val in ls:
    res = re.findall(r'(?<=<)\w+\d{0,}', val)
    if res:
        for d in res:
            lines.append(d)
        
tag_list = list(set(lines))
tag_list.sort()
print ";".join(tag_list)
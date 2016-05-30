import xml.etree.ElementTree
e = xml.etree.ElementTree.parse('data.xml').getroot()

for atype in e.findall('type'):
    print(atype.get('name'))

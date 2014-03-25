from lxml import objectify

path = '/Users/jhbco/Desktop/books.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

data = []


for i in root.book:
	book_data = {}
	for child in i.getchildren():
		book_data[child.tag] = child.pyval
	data.append(book_data)

#print data[0]['description']
print len(data)

for j in data:
	temp = j['description']
	print temp.strip()
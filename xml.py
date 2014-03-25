from lxml import objectify

path = '/Users/jhbco/Desktop/books.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

print parsed
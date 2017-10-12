import re
import collections
text = open('book.txt').read().lower()
words = re.findall('\w+', text)
print(collections.Counter(words).most_common(10))

f = open('data.txt', 'r')
lines = f.read()
f.close()
print(lines)

f = open('files/relative_data.txt', 'r')
lines = f.readlines()
f.close()
print(lines)

f = open('newfile.txt', 'a')
f.write("Jello\nMello\nEat\nMy\nYello")
f.close()
#2.1 split a string into fields, but the delimiters (and space around them) are not consistent throughout the string
#solution: use re.split() povide more flexibility
line = 'asdf fjkd; afred, as,some,        fooo, really!haha'
import re
words = re.split(r'[;,!\s]\s*', line)
print("after split, those words are:")
print(words)
#要注意使用的正则表达式
fields = re.split(r'(;|,|!|\s)\s*', line)
print("after split, those words are: ")
print(fields)
values = fields[::2]
delimiters = fields[1::2]+['']
print(values)
print(delimiters)
#reform the line using the same delimiters
reformed = ''.join(v+d for v, d in zip(values, delimiters))
print("reformed line: ", reformed)

values = re.split(r'(?:,|;|!|\s)\s*', line)
print("use ?: to split: ", values)


print("="*50)
"""
2.2 matching text at the start or end of a string
"""
#1. use str.startsWith or str.endsWith()方法
filename = 'c:\\test\\project\\spam.txt'
print("is it a text file? ", filename.endswith('.txt'))
print("is it a pdf file? ", filename.endswith('.pdf'))
url = "http://www.python.org"
print("is it an URL? ", url.startswith("http"))

#1.1 where there are multiple choices
import os
filenames = os.listdir('.')
#using tuple as an input!!
markdown = [name for name in filenames if name.endswith(('.md','.txt'))]
print(markdown)


print("="*50)
"""
2.3 matching strings using shell wildcard patterns
fnmatch module provides two functions - fnmatch() and fnmatchcaase()
"""
from fnmatch import fnmatch, fnmatchcase
isMatch = fnmatch('foo.txt', '*.txt')
print("is match foo.txt using *.txt? ", isMatch)
isMatch = fnmatch('foo.txt', '?oo.txt')
print("is match foo.txt using ?oo.txt? ", isMatch)
isMatch = fnmatch('dat45.csv', 'dat[0-9]*')
print("is match foo.txt using expression ", isMatch)
isMatch = fnmatchcase('foo.txt', '*.TXT')
print("is match foo.txt by case? ", isMatch)


print("="*50)
"""
2.4 matching and searching for text patterns
"""
text = "yeah, but no, but year, bot no, but yes"
print(text)
#1. using find
hasNo = text.find('no')
print("'no' positioned in ", hasNo)
#2. using match
import re
text1 = "11/27/2018"
text2 = 'Nov 27, 2018'
text3 = 'today is 11/27/2018. PyCon starts 3/14/2013'
isMatch = re.match(r'\d+/\d+/\d+', text1)
print('the pattern match the text? ', isMatch)
isMatch = re.match(r'\d+/\d+/\d+', text2)
print('the pattern match the text? ', isMatch)

datepat = re.compile(r'\d+/\d+/\d+')
isMatch = datepat.match(text1)
print('use patten repeatedly. result1: ', isMatch)
isMatch = datepat.match(text2)
print('use pattern repeatedly. result: ', isMatch)

#search text for all occurrences of a pattern
matchTexts = datepat.findall(text3)
print('all matched text in text3: ', matchTexts)

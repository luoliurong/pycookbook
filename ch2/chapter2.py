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


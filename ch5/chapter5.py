#1. use open() function with mode rt to read a text file.
filepath = r'C:\Projects\Python\pycookbook\ch5\test_ascii.txt'
filepath2 = r'C:\Projects\Python\pycookbook\ch5\test_utf8.txt'
filepath3 = r'C:\Projects\Python\pycookbook\ch5\test_write.txt'
with open(filepath, 'rt') as file:
    data = file.read()
    print(data)

#reading with default encoding
with open(filepath2, 'rt') as f:
    for line in f:
        print(line)

with open(filepath3, 'rt', encoding='utf-8') as f:
    for line in f:
        print(line)


#2. use open() function with mode wt to write a file
with open(filepath3, 'wt') as f:
    f.writelines('this is a test for writing\r\nthis is another line')

#another way to print file- redirect print result to a file
with open(filepath3, 'wt', encoding='utf-8') as f:
    print('hello world! 你好，世界！', file=f)
    print('done')


print('*'*100)

#read and write binary file
filepath = r'C:\Projects\Python\pycookbook\ch5\test1.bin'
filepath2 = r'C:\Projects\Python\pycookbook\ch5\notexistfile'
with open(filepath, 'wb') as f:
    f.write(b'Hello, world!')
    print('binary data has been written')

with open(filepath, 'rb') as f:
    data = f.read()
    print('binary data is read as ', data)

import os
if os.path.exists(filepath2):
    os.remove(filepath2)

#write to a file that does not exists
with open(filepath2, 'xb') as f:
    f.write(b'hello, world!\n')

if not os.path.exists(filepath2):
    with open(filepath2, 'wb') as f:
        f.write(b'world\n')
else:
    print('file already exists')

print('*'*100)


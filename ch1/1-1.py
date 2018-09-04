"""
有个包含N个元素的的元组或许列，现将其拆分为NN个单独的变量
"""
p = (4,5)
x, y = p
#section1:
data = ['ACME', 50, 91.1, (2012,12,21)]
name, age, score, date = data
name, age, score, (year, month, day)  = data

print("verify result for section 1:")
print("expected data (2012,12,21) <--->", date)
print("expected data 21 <--->", day)

str = "hello"
h,e,l,l2,o = str
print("string could be easily splitted: ", h,e,l,l2,o)

#怎么样在拆分的时候丢弃一些变量
_,shares,price,_ = data
print("expected shares value 50 <----> ", shares)


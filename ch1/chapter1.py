"""
1.1 有个包含N个元素的的元组或许列，现将其拆分为NN个单独的变量
"""
p = (4,5)
x, y = p
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


print("==================================================")
"""
1.2 需要从某个可迭代对象中分解出N个元素，但是这个可迭代对象的长度可能超过N。导致的问题是"分解的值过多"的异常。
一个典型的例子是，全班平均成绩统计，但是要求去掉一个最高分，去掉一个最低分 后再算平均分。
*表达式可以解决这个问题
"""
scores = [67, 18, 89, 89, 99, 100, 68,98,87,98,90,91,94]
sortedscore = sorted(scores)
lowest,*middle,highest = sortedscore
avgscore = sum(middle)/len(middle)
print("lowest, highest, average: ", lowest, highest, avgscore)


print("="*50)
"""
1.3 保存最后N个元素。 希望在迭代或者是其他形式的处理过程中对最后几项记录做一个有限的历史记录。
解决方法： collections.dequeue
"""
from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

all_lines = ("hello, world", "hello, Sql", "Hello, JS", "Hello, CSharp!", "Hello, Java", "Hello, Cotlin", "Hello, python" "Hello, Typescript", "Hello, HTML")
print("previous 3 lines are:")
for line, preline in search(all_lines, 'python', 3):
    for pline in preline:
        print(pline)


print("="*50)
"""
1.4 在某个集合中找出最大/最小的N个元素
用heapq模块中的nlargest/nsmallest()函数
"""
import heapq
nums = [1,2,8,7,23,-4,42,37,1]
print("3 largest number: ", heapq.nlargest(3,nums))
print("3 smallest number: ", heapq.nsmallest(3, nums))

#当然，可以用max,min函数
print("largest number: ", max(nums))
print("smallest number: ", min(nums))

#更加有趣的例子：使用函数的key参数
portfolio = [
    {'name':'IBM','shares':100,'price':91.1},
    {'name':'APPLE','shares':50,'price':591.1},
    {'name':'FB','shares':200,'price':21.9},
    {'name':'HPQ','shares':350,'price':59.7},
    {'name':'YHOO','shares':150,'price':51.2},
    {'name':'ACME','shares':75,'price':123.6},
    {'name':'MS','shares':350,'price':231.1},
    ]
cheap = heapq.nsmallest(3, portfolio, key=lambda s:s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])
print("3 cheapest: ", cheap)
print("3 expensive: ", expensive)


print("="*50)
"""
1.5 实现优先级队列
"""
#优先级队列类
class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        #将(-priority, self._index, item)，把priority取负值是为了让队列能够按元素的优先级从高到低的顺序排列。
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    
    def pop(self):
        #取出来后做了处理，取(-priority, self._index, item)中最后一项
        return heapq.heappop(self._queue)[-1]

#如何使用优先级队列类
class Item:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

myqueue = PriorityQueue()
myqueue.push(Item('foo'),1)
myqueue.push(Item('bar'),5)
myqueue.push(Item('spam'), 4)
myqueue.push(Item('grok'), 1)

highestPiorityItem = myqueue.pop()
print("highest priority item is: ", highestPiorityItem)


print("="*50)
"""
1.6 在字典中将键映射到多个值上
"""
from collections import defaultdict
d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(3)
print("my dictionary based on list: ", d)

d2 = defaultdict(set)
d2['a'].add(1)
d2['a'].add(2)
d2['b'].add(3)
print("my dictinary based on set: ", d2)


print("="*50)
"""
1.7 创建一个字典，同时，当对字典做迭代或序列化操作时，也能控制器中元素的顺序
collections模块中的orderedDict类,当对字典做迭代时，它会严格按照元素初始添加的顺序进行。
"""
from collections import OrderedDict
ord = OrderedDict()
ord['fooo'] = 1
ord['barr'] = 7
ord['spam'] = 3
ord['grok'] = 4
print("elements in my dictionary:")
for key in ord:
    print(key, ord[key])


print("="*50)
"""
1.8 在字典上对数据执行各式各样的计算，比如求最小值，最大值，排序等
"""
prices = {
    'ACME':45.23,
    'AAPL':62.77,
    'IBMI':205.17,
    'HPQQ':37.11,
    'MSFT':55.76,
    'UNSS':62.77
}
#1. 使用zip()将字典的键和值反转过来找最低，最高的价格
min_price = min(zip(prices.values(), prices.keys()))
print("minimum price is: ", min_price)
max_price = max(zip(prices.values(), prices.keys()))
print("maximum price is: ", max_price)
#2. 使用zip()结合sorted()排序
price_sorted = sorted(zip(prices.values(), prices.keys()))
print("sorted prices dictionary:")
print(price_sorted)
#NOTE: zip()创建了一个迭代器，它的内容只能被消费一次。


print("="*50)
"""
1.9 在两个字典里找相同的地方(相同的键，相同的值)
"""
a = {
    'x':1,
    'y':2,
    'z':3
}
b = {
    'w':11,
    'r':12,
    'z':3
}
c = {
    'w':11,
    'r':12,
    'z':4
}
#在两个字典中都存在的key
result1 = a.keys() & b.keys() # {'x','y'}
print(result1)
#在a中存在，在b中不存在的key
result2 = a.keys() - b.keys()
print(result2)
#在两个字典中都存在的键值对
result3 = a.items() & b.items()
print(result3)


print("="*50)
"""
1.10 去除序列中重复出现的元素，但是仍然保持剩下的元素顺序不变
如果列表中的值是可哈希的，可通过使用集合和生成器解决。
"""
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

duplist = [1,5,2,1,9,1,5,10]
#1. 简单快捷的办法， 但是不保证顺序
print("use set:")
myset = set(duplist)
print(myset)
#2. 自定义函数
print("use customized method:")
rmduplist = list(dedupe(duplist))
print(rmduplist)
#如果元素是不可哈希的对象，怎么办？
#参数key的作用是指定一个函数用来将许列中的元素转换为可哈希的类型
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [
    {'x':1, 'y':2},
    {'x':1, 'y':3},
    {'x':1, 'y':2},
    {'x':2, 'y':4}
]
list2 = list(dedupe2(a, key=lambda d:(d['x'],d['y'])))
print(list2)
list3 = list(dedupe2(a, key=lambda d:d['x']))
print(list3)


print("="*50)
"""
1.12 找出许列中出现次数最多的元素。
collections模块中的counter类有个方法most_common()
"""
words = [
    'look', 'hello', 'world', 'eyes', 'into', 'the', 'the','eyes','hello', 'around','my', 'desk', 'hello', 'years','look','eyes','hello','into','look','into'
]
from collections import Counter
word_count = Counter(words)
top_three_words = word_count.most_common(3)
print("most three common words are: ", top_three_words)


print("="*50)
"""
1.13 根据一个或多个字典中的值来对列表排序
"""
rows = [
    {'fname':'Brian', 'lname':'Jones', 'uid':1003},
    {'fname':'David', 'lname':'Beazley', 'uid':1002},
    {'fname':'John', 'lname':'Cleese', 'uid':1001},
    {'fname':'Big', 'lname':'Jones', 'uid':1004}
]
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
#也可以用lambda表达式, 但是用itemgetter会更加快一些
rows_by_fname2 = sorted(rows, key=lambda r:r['fname'])
print("data ordered by fname:")
print(rows_by_fname)
rows_by_uid = sorted(rows, key=itemgetter('uid'))
print("data ordered by uid: ")
print(rows_by_uid)
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print("data ordered by multiple feature:")
print(rows_by_lfname)


print("="*50)
"""
1.14 对不原生支持比较操作的对象进行排序
"""
class User:
    def __init__(self, user_id, uname):
        self.user_id = user_id
        self.user_name = uname
    
    def __repr__(self):
        return 'User({}, {})'.format(self.user_id, self.user_name)

users = [User(23, 'David'), User(3, 'Ron'), User(99, 'Ara')]
print("original user set: ")
print(users)
#1. sorted + lambda表达式
susers = sorted(users, key=lambda u:u.user_id)
print("sorted users by lambda: ")
print(susers)
#2. 使用operator.attrgetter(), 更加快，而且可添加多个attr
from operator import attrgetter
susers2 = sorted(users, key=attrgetter('user_id'))
print("sorted users by attrgetter: ")
print(susers2)
susers3 = sorted(users, key=attrgetter('user_id', 'user_name'))
print("sorted users by multiple attrs: ")
print(susers3)


print("="*50)
"""
1.15 有一系列的字典或对象实例，想根据某个特定的字段来分组迭代数据
itertools.groupby()函数
"""
rows = [
    {'address':'5412 North Clark', 'date':'07/01/2018'},
    {'address':'523 North Clark', 'date':'07/04/2018'},
    {'address':'3312 North Clark', 'date':'07/02/2018'},
    {'address':'5672 North Clark', 'date':'07/03/2018'},
    {'address':'5282 North Clark', 'date':'07/02/2018'},
    {'address':'541 North Clark', 'date':'07/02/2018'},
    {'address':'512 North Clark', 'date':'07/01/2018'},
    {'address':'5412 Sourth Clark', 'date':'07/04/2018'}
]
from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter('date'))
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for item in items:
        print(' ', item)


print("="*50)
"""
1.16 筛选许列中的元素。序列中含有一些数据，我们需要提取出其中的值，或者根据某些标准对序列做删减。
"""
#1. 使用列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
result1 = [n for n in mylist if n > 0]
print("all elements >0")
print(result1)
result2 = [n for n in mylist if n < 0]
print("all elements <0")
print(result2)

#2. 使用生成器表达式通过迭代的方法
print("generated by iterator: ")
pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

#3. 使用内建的filter函数
values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))
print("elements using filters are: ")
print(ivals)

#4. 列表推导式也有数据转换的功能
import math
sqrtVals = [math.sqrt(n) for n in mylist if n > 0]
print("sqrt elements are: ")
print(sqrtVals)


print("="*50)
"""
1.17 从字典中提取子集
"""
stocks = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQD': 27.20,
    'FBII': 10.75
}
#字典推导式
largestocks = {key:value for key, value in stocks.items() if value > 200}
print("stocks larger than 200: ")
print(largestocks)

company_names = {'AAPL', 'IBM', 'MSFT', 'HPQQ'}
compstocks = {key:value for key, value in stocks.items() if key in company_names}
print("Below company's stock (AAPI, IBM, MSFT, HPQQ): ")
print(compstocks)

#通过元组, 速度稍慢
tupstock = dict((key,value) for key, value in stocks.items() if value > 200)
print("by using tuple: ")
print(tupstock)


print("="*50)
"""
1.19 我们的代码是通过位置(索引/下标)来访问列表或元组的，但有时候这会使得代码难以阅读，我们希望可以通过名称来访问元素。
collections.namedtuple()
"""
from collections import namedtuple
UserInfo = namedtuple('Customer', ['addr', 'phone'])
ing = UserInfo('1777 EU North', '123456789')
print("our customer ING is: ")
print(ing)
print("ING's address is ", ing.addr)
print("ING's phone number is: ", ing.phone)
#分解
addr, ph = ing
print("after splitted, addr is: ", addr)


print("="*50)
"""
1.20 将多个映射合并为单个映射
使用collections的ChainMap
"""
from collections import ChainMap
a = {'x' : 1, 'z' : 3}
b = {'y' : 2, 'z' : 4}
c = ChainMap(a, b)
print("the chain map is: ")
print(c)
print("how about the dup key 'z'? ")
print(c['z'])


import os

current_dir = os.path.dirname(os.path.realpath(__file__))

"""
section1. reading and writing CSV files.
"""
#reading a csv file
stocks_file = current_dir + r'\stocks.csv'
import csv
with open(stocks_file) as f:
    f_csv = csv.reader(f, delimiter=',')
    headers = next(f_csv)
    for row in f_csv:
        print(row)


print("*"*100)
#reading a csv file another way - using namedtuple
from collections import namedtuple
with open(stocks_file) as f:
    f_csv = csv.reader(f)
    headings = next(f_csv)
    row = namedtuple('Row', headings)
    for r in f_csv:
        current_row = row(*r)
        print(current_row.Symbol)


print("*"*100)
#reading a csv file another way - using dictionary
with open(stocks_file) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print('symbol:', row["Symbol"], '    Price: ', row["Price"])


print("*"*100)
#to write rows to a csv file
headers = ['Symbol','Price','Date','Time','Change','Volume']
rows = [
    ('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
    ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
    ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
]
file_to_write = current_dir + r'\stocks_w.csv'
if os.path.exists(file_to_write):
    os.remove(file_to_write)

with open(file_to_write, 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)
print("write to file ", file_to_write)


"""
section1. reading and writing CSV files.
"""
print("*"*100)
#reading JSON file
import json
json_file = current_dir + r'\stocks.json'
with open(json_file, 'r') as f:
    data = json.load(f)
    print(data)

print("*"*100)
#reading json strings
data = {
    'name': 'ACME', 
    'shares': 100, 
    'price': 542.23
}
json_str = json.dumps(data)
print(json_str)
json_data = json.loads(json_str)
print(json_data["name"])

#write Json data
json_filew = current_dir + r'\stocks_w.json'
with open(json_filew, 'w') as f:
    json.dump(data, f)
    print("json data is dumped to ", json_filew)



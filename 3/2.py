import re

with open('input.txt','r') as datei:
    line = datei.read().strip()

list = re.search(r"mul\((\d+),(\d+)\)", line)

valied = re.search(r"do\(\)(.*?)don't\(\)",line,re.DOTALL)

for i in valied:
    list = re.findall(r"mul\((\d+),(\d+)\)", line)

sum = 0
mul = 0

for element in list:
    mul = int(element[0]) * int(element[1]) # tuple only read
    sum += mul

print(sum)
print("Test")

numberList = []
sortedNumbers = []

with open('input.txt','r') as datei:
    for line in datei:
        numbers = list(map(int,line.strip().split())) 
        numberList.append(numbers)
        if numbers == sorted(numbers) or numbers == sorted(numbers, reverse = True):
            sortedNumbers.append(numbers)
  
safe = 0

for numbers in sortedNumbers:
    is_safe = True
    for i in range(len(numbers) - 1):
        if abs(numbers[i] - numbers[i + 1]) > 3 or abs(numbers[i] - numbers[i + 1]) == 0:  # 如果相邻数字的差值大于3
            is_safe = False 
            break

    if is_safe: 
        safe += 1

print(safe) 


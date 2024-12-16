numberList = []
safe = 0

with open('input.txt', 'r') as datei:
    for line in datei:
        numbers = list(map(int, line.strip().split()))

        if (numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)) and \
           all(1 <= abs(numbers[i] - numbers[i + 1]) <= 3 for i in range(len(numbers) - 1)):
            safe += 1  
        else:
            numberList.append(numbers)  


for numbers in numberList:
    found_safe = False  
    for i in range(len(numbers)):
        
        temp_numbers = numbers[:i] + numbers[i+1:]
   
        if (temp_numbers == sorted(temp_numbers) or temp_numbers == sorted(temp_numbers, reverse=True)) and \
           all(1 <= abs(temp_numbers[k] - temp_numbers[k + 1]) <= 3 for k in range(len(temp_numbers) - 1)):
            safe += 1
            found_safe = True
            break  
    if found_safe:
        continue

print(safe)


# Erstmal checken, welche Zeile sortiert sind
# dann checken , ob die Elemente nebeneinander abs 1 ~ 3 ist
# dann ist es safe

# jetzt checken die Zeile die am Anfang nicht sortiert sind
# remove ein Element, checken ob es jetzt sortiert sind
# dann checken, ob die Eemente nebeneinander abs 1~3 ist
# dann ist es safe
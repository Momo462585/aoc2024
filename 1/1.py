
arrary1 = []
arrary2 = []

#datei zu öffnen
datei = open('input1.txt','r')

# die Elements in separat arrary speichern
for line in datei:
    elements = line.split() #die elemente trennen
    arrary1.append(elements[0]) # jede elements hinzufügen
    arrary2.append(elements[1])

# die arrarys sortieren
arrary1.sort()
arrary2.sort()

#das Unterschied rechnen
differences = []
for i in range(len(arrary1)):
    differences.append(int(arrary1[i]) - int(arrary2[i]))

summe = 0
for i in differences:
    summe += abs(i)

print(summe)

'''
#das Unterschied rechnen
#The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
#and then the second item in each passed iterator are paired together etc.

differences = [(abs(a-b) )for a,b in zip(arrary1,arrary2)]

print (differences)
'''
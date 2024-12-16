arrary2 = []
arrary1 = []

datei = open('input1.txt','r')

for line in datei:
    elements = line.strip().split() #die elemente trennen
    arrary1.append(int(elements[0])) # jede elements hinzufügen
    arrary2.append(int(elements[1]))


summe = []

for x in arrary1:
    count = arrary2.count(x)
    summe.append(int(x * count))

num = 0

for i in summe:
    num += i

print(num)
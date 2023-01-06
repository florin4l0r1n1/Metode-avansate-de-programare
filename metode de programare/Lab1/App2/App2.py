number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")
for i in range (0, n):
    print("Introdu elementul de pe pozitia: ", i,) 
    item = int(input())
    number_list.append(item)
print("Lista este: ", number_list)

minim, maxim = number_list[0], number_list[0]

for i in range(1, n):
    if minim > number_list[i]:
        minim = number_list[i]
    if maxim < number_list[i]:
        maxim = number_list[i]

print("Maximul este: ", maxim)
print("Minimul este: ", minim)

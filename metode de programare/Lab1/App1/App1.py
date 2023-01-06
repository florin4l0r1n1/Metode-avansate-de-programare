from ast import Num


number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")
for i in range(0, n):
    print("Introdu elementul de pe pozitia: ", i, )
    item = int(input())
    number_list.append(item)
print("Lista este:", number_list)

for i in range(0, n-1):
    for j in range(i+1, n):
        if number_list[i] > number_list[j]:
            aux = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = aux

print("Lista sortata este: ", number_list)

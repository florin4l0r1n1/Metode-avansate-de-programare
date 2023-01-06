from audioop import reverse
from pickle import FALSE


number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")
for i in range(0, n):
    print("Introdu elementul la pozitia: ", i, )
    item = int(input())
    number_list.append(item)

number_list.sort(reverse = False)
print("Lista este", number_list)
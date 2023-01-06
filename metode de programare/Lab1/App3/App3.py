
import string


thislist = []
n = int(input("Introduceti numarul de cuvinte: "))

for i in range(0, n):
    print("Introduceti cuvantul:", i)
    item = str(input())
    thislist.append(item)
print("Lista este: ", thislist)
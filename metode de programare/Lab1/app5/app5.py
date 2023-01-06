number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")

for i in range(0, n):
    print("Introdu elementul la pozitia: ", i, )
    item = int(input())
    number_list.append(item)

print("Lista este", number_list)

print("Introduceti un element nou: ")
element = int(input())
number_list.append(element)

print("\n")
print("Lista este", number_list)
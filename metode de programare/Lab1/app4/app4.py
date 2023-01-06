from xml.dom.minidom import Element


number_list = []
n = int(input("Introdu numarul de elemente: "))
print("\n")

for i in range(0, n):
    print("Introdu elementul la pozitia: ", i, )
    item = int(input())
    number_list.append(item)

print("Lista este", number_list)

print("\n")

print("Alege elementul pe care doresti sa-l stergi:")
element = int(input())
number_list.remove(element)

print("Lista este", number_list)

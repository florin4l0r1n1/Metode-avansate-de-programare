def divizor(a, b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    print(a)

c = int(input("Primul element: "))
d = int(input("Al doilea element: "))
divizor(c,d)
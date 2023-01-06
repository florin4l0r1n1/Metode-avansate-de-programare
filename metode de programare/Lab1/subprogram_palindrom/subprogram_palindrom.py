def palindrom(x):
    inv = 0
    n = x
    while n != 0:
        inv = inv*10 + n%10
        n = n//10
    if x == inv:
        print("Este palindrom.")
    else:
        print("Nu este palindrom.")

def main():
    print("Introduceti un element: ")
    element =  int(input())
    palindrom(element)

main()
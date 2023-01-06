nr = int(input("Introdu un element: "))
n = nr
inv = 0
while n != 0:
    inv = inv*10 + n%10
    n = n//10
if inv == nr:
    print("Este palindrom.")
else:
    print("Nu este palindrom.")

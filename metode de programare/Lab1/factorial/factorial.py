def factorial(x):
    if x == 1:
        return 1;
    else:
        return (x * factorial(x-1))

num = int(input("Introduceti un element: "))
print("Factorial", factorial(num))

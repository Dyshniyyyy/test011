def sum(a,b):
    return a + b


def sub(a,b):
    return a - b

def dif(a,b):
    return a // b


a, sign, b = input().split()

if sign == "+":
    print(sum(int(a), int(b)))

if sign == "-":
    print(sub(int(a), int(b)))

if sign == "//":
    print(dif(int(a), int (b)))

































    0
































a = int(input("Gib eine Zahl ein: "))
b = int(input("Gib eine zweite Zahl ein: "))

o = input("Choose you operator: + - / *")
c = True

if o == "+":
    if c:
        print(a + b)

elif o == "-":
    print (a - b)

elif o == "/":
    print (a / b)

elif o == "*":
    print (a * b)

else:
    print("ERROR")
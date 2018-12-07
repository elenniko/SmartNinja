print("Hello! This is a program that converts kilometers into miles!")

userinput = True

while userinput:
    kilometer = int(input("Please write the kilometer value you want to convert: "))

    miles = kilometer * 0.6213712

    print(miles)

    while True:
        dummy = input("Do you want to convert another value (y/n)?")

        if dummy == 'y':
            break

        if dummy == 'n':
            userinput = False
            print("Thank you for the values! See you next time!")
            break

import sys
while(1):
    print("\n------SIMPLE CALCULATOR------")
    print("1.ADDITION")
    print("2.SUBTRACTION")
    print("3.MULTIPLICATION")
    print("4.DIVISION")
    print("5.MODULUS")
    print("6.EXPONENT")
    print("7.FLOOR DIVISION")
    print("8.EXIT")
    choice = int(input("Enter your Choice:"))
    if(choice == 8):
        print("Exiting.... Bye")
        sys.exit()
    if(choice > 8):
        print("Enter valid choice(1-8)\n")
        continue
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    if(choice == 1):
        print("Addition of the given number is: ",num1 + num2)
    elif(choice == 2):
        print("Subtraction of the given number is: ",num1 - num2)
    elif(choice == 3):
        print("Multiplication of the given number is: ",num1 * num2)
    elif(choice == 4):
        print("Division of the given number is: ",num1 / num2)
    elif(choice == 5):
        print("Modulus of the given number is: ",num1 % num2)
    elif(choice == 6):
        print("Exponent of the given number is: ",num1 ** num2)
    elif(choice == 7):
        print("Floor Division of the given number is: ",num1 // num2)
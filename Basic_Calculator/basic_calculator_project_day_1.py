print("Welcome to Calculator Project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Select an operation: "))


if option == 1:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")

elif option == 2:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    sub = num1 - num2
    print(f"{num1} - {num2} = {sub}")

elif option == 3:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    mul = num1 * num2
    print(f"{num1} x {num2} = {mul}")

elif option == 4:
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 2: "))
    if num2 == 0:
        print("Error: Division by zero is undefined")
    else:
        div = num1 / num2
        print(f"{num1} / {num2} = {div}")

else:
    print("Invalid Input!")

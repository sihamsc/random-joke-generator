import math

def calculator():
    print("Simple Calculator: Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square root")

    choice = input("Enter choice (1-5): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero!")
    elif choice == '5':
        num = float(input("Enter number for square root: "))
        print(f"Square root of {num} is {math.sqrt(num)}")
    else:
        print("Invalid input!")

if __name__ == "__main__":
    calculator()

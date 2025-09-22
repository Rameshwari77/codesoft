def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        result = add(num1, num2)
        op = "+"
    elif choice == '2':
        result = subtract(num1, num2)
        op = "-"
    elif choice == '3':
        result = multiply(num1, num2)
        op = "*"
    elif choice == '4':
        result = divide(num1, num2)
        op = "/"
    else:
        print("Invalid operation choice.")
        return

    print(f"\nResult: {num1} {op} {num2} = {result}")

if __name__ == "__main__":
    main()

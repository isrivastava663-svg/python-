# ================================
#   Simple Calculator - Python
# ================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "❌ Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("=" * 35)
    print("       🧮 SIMPLE CALCULATOR")
    print("=" * 35)

    while True:
        print("\nOperations:")
        print("  1. Addition       (+)")
        print("  2. Subtraction    (-)")
        print("  3. Multiplication (×)")
        print("  4. Division       (÷)")
        print("  5. Exit")
        print("-" * 35)

        choice = input("Enter choice (1-5): ").strip()

        if choice == '5':
            print("\n👋 Goodbye! Thanks for using Calculator.")
            break

        if choice not in ['1', '2', '3', '4']:
            print("⚠️  Invalid choice! Please enter 1-5.")
            continue

        try:
            a = float(input("Enter first number : "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("⚠️  Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            result = add(a, b)
            symbol = '+'
        elif choice == '2':
            result = subtract(a, b)
            symbol = '-'
        elif choice == '3':
            result = multiply(a, b)
            symbol = '×'
        elif choice == '4':
            result = divide(a, b)
            symbol = '÷'

        print(f"\n✅ Result: {a} {symbol} {b} = {result}")

if __name__ == "__main__":
    calculator()

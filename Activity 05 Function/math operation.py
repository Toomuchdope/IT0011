def divide(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a / b

def exponentiate(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a % b

def summation(a, b):
    if a >= b:
        print("Error: Second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMathematical Operations Menu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").strip().upper()
        
        if choice == 'Q':
            print("Exiting the program. Goodbye!")
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = int(input("Enter the first number: "))
                b = int(input("Enter the second number: "))
                
                if choice == 'D':
                    result = divide(a, b)
                elif choice == 'E':
                    result = exponentiate(a, b)
                elif choice == 'R':
                    result = remainder(a, b)
                elif choice == 'F':
                    result = summation(a, b)
                
                if result is not None:
                    print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

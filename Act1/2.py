
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))


if num1 >= num2:
    if num1 >= num3:
        if num2 >= num3:
            print(f"The numbers in descending order are: {num1}, {num2}, {num3}")
        else:
            print(f"The numbers in descending order are: {num1}, {num3}, {num2}")
    elif num3 >= num2:
        print(f"The numbers in descending order are: {num3}, {num1}, {num2}")
    else:
        print(f"The numbers in descending order are: {num2}, {num1}, {num3}")
elif num2 >= num3:
    if num1 >= num3:
        print(f"The numbers in descending order are: {num2}, {num1}, {num3}")
    else:
        print(f"The numbers in descending order are: {num2}, {num3}, {num1}")
else:
    print(f"The numbers in descending order are: {num3}, {num2}, {num1}")

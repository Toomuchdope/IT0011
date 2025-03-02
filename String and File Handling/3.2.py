FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")


FullName = f"{FirstName} {LastName}"


FullName_upper = FullName.upper()
FullName_lower = FullName.lower()
FullName_length = len(FullName)

print("------------------------------------------------------------------------------")
print(f"Full Name: {FullName}")
print(f"Full Name (Upper Case): {FullName_upper}")
print(f"Full Name (Lower Case): {FullName_lower}")
print(f"Length of Full Name: {FullName_length}")
print("------------------------------------------------------------------------------")
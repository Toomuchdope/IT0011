print("------------------------------------------------------------------------------")
FirstName = input("Enter your first name: ")
LastName = input("Enter your last name: ")
age = input("Enter your age: ")
print("------------------------------------------------------------------------------")
FullName = f"{FirstName} {LastName}"
SlicedName = FirstName[:3]
print("------------------------------------------------------------------------------")
print(f"\nFull Name: {FullName}")
print(f"Sliced Name: {SlicedName}")
print(f"Greeting Message: Hello, {SlicedName}! Welcome. You are {age} years old.")
print("------------------------------------------------------------------------------")
LastName = input("Enter last name: ")
FirstName = input("Enter first name: ")
age = input("Enter age: ")
ContactNumber = input("Enter contact number: ")
course = input("Enter course: ")


student_info = (
    f"Last Name: {LastName}\n"
    f"First Name: {FirstName}\n"
    f"Age: {age}\n"
    f"Contact Number: {ContactNumber}\n"
    f"Course: {course}\n"
)


FileName = 'students.txt'


with open(FileName, 'a') as file:  
    file.write(student_info)

print(f"Student information has been saved to '{FileName}'.")
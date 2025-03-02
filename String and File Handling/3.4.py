FileName = r"C:\Users\john andrew\OneDrive - STI College Cubao\Desktop\IT0011-1\String and File Handling\students.txt"

try:
    with open(FileName, 'r', encoding="utf-8") as file:
        print("Reading Student Information:\n")
        print(file.read())
except FileNotFoundError:
    print(f"Error: The file '{FileName}' was not found. Please check the file location.")
except Exception as e:
    print(f"An error occurred: {e}")

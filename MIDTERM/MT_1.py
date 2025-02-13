# Function to check if a number is a palindrome
def is_palindrome(num):
    return str(num) == str(num)[::-1]

# Open the numbers.txt file
with open('numbers.txt', 'r') as file:
    # Read each line in the file
    for line_number, line in enumerate(file, start=1):
        # Split the line by commas and remove any empty strings
        numbers = [number.strip() for number in line.strip().split(',') if number.strip()]

        # Convert each number in the list to an integer and sum them
        total_sum = sum(int(number) for number in numbers)

        # Check if the sum is a palindrome
        if is_palindrome(total_sum):
            print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Palindrome")
        else:
            print(f"Line {line_number}: {line.strip()} (sum {total_sum}) - Not a palindrome")
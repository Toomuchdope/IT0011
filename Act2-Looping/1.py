
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))


sum_terms = 0


for i in range(first_term, last_term + 1):
    sum_terms += i


print(f"The sum of the numbers from {first_term} to {last_term} is {sum_terms}")

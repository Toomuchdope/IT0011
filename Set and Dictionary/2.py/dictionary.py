import pandas as pd

# Load the currency exchange rates file
file_path = "currency.csv"  # Update the path if needed
df = pd.read_csv(file_path, encoding="ISO-8859-1")

# Create a dictionary for quick lookup
exchange_rates = dict(zip(df['code'], df['rate']))

def convert_currency(amount, currency_code):
    if currency_code in exchange_rates:
        converted_amount = amount * exchange_rates[currency_code]
        return converted_amount
    else:
        return None

# Get user input
dollar_amount = float(input("How much dollar do you have? "))
currency_code = input("What currency do you want to have? ").upper()

# Convert and display result
converted_amount = convert_currency(dollar_amount, currency_code)

if converted_amount is not None:
    print(f"\nDollar: {dollar_amount} USD")
    print(f"{currency_code}: {converted_amount:.6f}")
else:
    print("Invalid currency code. Please try again.")

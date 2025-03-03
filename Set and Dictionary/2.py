import pandas as pd

def load_exchange_rates(file_path):
    """Loads currency exchange rates from a CSV file."""
    try:
        df = pd.read_csv(file_path, encoding='latin1')
        return df.set_index('code')['rate'].to_dict()
    except Exception as e:
        print("Error loading exchange rates:", e)
        return {}

def convert_currency(usd_amount, target_currency, exchange_rates):
    """Converts USD to the target currency using exchange rates."""
    if target_currency in exchange_rates:
        converted_amount = usd_amount * exchange_rates[target_currency]
        return converted_amount
    else:
        return None

def main():
    file_path = "currency.csv"  # Update this path if needed
    exchange_rates = load_exchange_rates(file_path)
    
    usd_amount = float(input("How much dollar do you have? "))
    target_currency = input("What currency you want to have? ").upper()
    
    converted_amount = convert_currency(usd_amount, target_currency, exchange_rates)
    
    if converted_amount is not None:
        print(f"\nDollar: {usd_amount} USD")
        print(f"{target_currency}: {converted_amount:.6f}")
    else:
        print("Currency code not found!")

if __name__ == "__main__":
    main()
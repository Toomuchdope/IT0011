from datetime import datetime

def convert_date_format(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%m/%d/%Y')
        return date_obj.strftime('%B %d, %Y')
    except ValueError:
        return "Invalid date format. Please use mm/dd/yyyy."

def main():
    date_input = input("Enter the date (mm/dd/yyyy): ")
    human_readable_date = convert_date_format(date_input)
    print(f"Date Output: {human_readable_date}")

if __name__ == "__main__":
    main()
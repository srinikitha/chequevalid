import re
from datetime import datetime

# Function to validate cheque number (Assuming 6-digit number)
def validate_cheque_number(number):
    return bool(re.fullmatch(r"\d{6}", number))

# Function to validate date format (DD-MM-YYYY)
def validate_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False

# Function to validate name (only alphabets and spaces)
def validate_name(name):
    return bool(re.fullmatch(r"[A-Za-z ]+", name))

# Function to validate amount in numbers (positive float)
def validate_amount_number(amount):
    try:
        return float(amount) > 0
    except ValueError:
        return False

# Function to validate amount in words (simplified)
def validate_amount_words(words):
    return bool(re.fullmatch(r"[A-Za-z\- ]+", words))

# Main validation
def main():
    print("=== Cheque Validation System ===")
    
    cheque_number = input("Enter Cheque Number (6 digits): ")
    date = input("Enter Date (DD-MM-YYYY): ")
    name = input("Enter Account Holder Name: ")
    amount_number = input("Enter Amount in Numbers: ")
    amount_words = input("Enter Amount in Words: ")

    valid = True

    if not validate_cheque_number(cheque_number):
        print("❌ Invalid Cheque Number.")
        valid = False

    if not validate_date(date):
        print("❌ Invalid Date Format.")
        valid = False

    if not validate_name(name):
        print("❌ Invalid Account Holder Name.")
        valid = False

    if not validate_amount_number(amount_number):
        print("❌ Invalid Amount in Numbers.")
        valid = False

    if not validate_amount_words(amount_words):
        print("❌ Invalid Amount in Words.")
        valid = False

    if valid:
        print("\n✅ Cheque is Valid.")
    else:
        print("\n⚠️ Cheque Validation Failed.")

# Run the main program
if __name__ == "__main__":
    main()

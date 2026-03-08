import re


def validate_phone(phone):
    """
    Validates a phone number in the formats: 123-456-7890 or (123) 456-7890.
    """
    # Regex pattern for phone numbers
    pattern = r'^(\(\d{3}\)\s*|\d{3}-)\d{3}-\d{4}$'
    if re.match(pattern, phone):
        return True
    return False


def validate_ssn(ssn):
    """
    Validates a Social Security Number in the format: XXX-XX-XXXX.
    """
    # Regex pattern for SSN
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    if re.match(pattern, ssn):
        return True
    return False


def validate_zip(zip_code):
    """
    Validates a 5-digit ZIP code.
    """
    # Regex pattern for 5-digit zip
    pattern = r'^\d{5}$'
    if re.match(pattern, zip_code):
        return True
    return False


def main():
    # Collect input from the user
    print("--- Data Validation Tool ---")
    user_phone = input("Enter Phone Number (e.g., 123-456-7890): ")
    user_ssn = input("Enter SSN (e.g., 000-00-0000): ")
    user_zip = input("Enter 5-digit ZIP code: ")

    # Validate and display results
    print("\n--- Validation Results ---")

    if validate_phone(user_phone):
        print(f"Phone Number '{user_phone}': VALID")
    else:
        print(f"Phone Number '{user_phone}': INVALID")

    if validate_ssn(user_ssn):
        print(f"SSN '{user_ssn}': VALID")
    else:
        print(f"SSN '{user_ssn}': INVALID")

    if validate_zip(user_zip):
        print(f"ZIP Code '{user_zip}': VALID")
    else:
        print(f"ZIP Code '{user_zip}': INVALID")


if __name__ == "__main__":
    main()
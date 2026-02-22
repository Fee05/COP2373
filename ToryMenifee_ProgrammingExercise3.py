from functools import reduce


def get_expenses():
    """Collects expense data from the user."""
    expense_list = []
    print("--- Monthly Expense Tracker ---")

    while True:
        name = input("Enter the type of expense (or 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        try:
            amount = float(input(f"Enter the amount for {name}: "))
            # Store as a dictionary for easy access in reduce
            expense_list.append({'type': name, 'amount': amount})
        except ValueError:
            print("Invalid input. Please enter a numerical value for the amount.")

    return expense_list


def analyze_expenses(expenses):
    """Uses reduce and lambda to calculate total, max, and min expenses."""
    if not expenses:
        return None

    # Calculate Total
    total = reduce(lambda acc, curr: acc + curr['amount'], expenses, 0)

    # Find Highest Expense
    highest = reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses)

    # Find Lowest Expense
    lowest = reduce(lambda a, b: a if a['amount'] < b['amount'] else b, expenses)

    return total, highest, lowest


def display_results(total, highest, lowest):
    """Formats and prints the analysis to the console."""
    print("\n--- Expense Analysis ---")
    print(f"Total Monthly Expenses: ${total:,.2f}")
    print(f"Highest Expense: {highest['type']} (${highest['amount']:,.2f})")
    print(f"Lowest Expense: {lowest['type']} (${lowest['amount']:,.2f})")


def main():
    """Main entry point of the program."""
    data = get_expenses()

    if data:
        total, high, low = analyze_expenses(data)
        display_results(total, high, low)
    else:
        print("No expenses were entered.")


if __name__ == "__main__":
    main()
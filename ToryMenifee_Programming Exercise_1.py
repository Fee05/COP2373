# Constants defined in UPPERCASE per PEP 8 standards
MAX_TICKETS_PER_BUYER = 4
TOTAL_TICKETS_AVAILABLE = 10


def validate_purchase(requested, remaining):
    """
    Brief Description: Checks if a ticket request meets all sale constraints.
    Parameters:
        requested (int): The number of tickets the user wants to buy.
        remaining (int): The current count of tickets left in inventory.
    Variables:
        None used outside of parameters.
    Logical Steps:
        1. Check if the request is 0 or negative.
        2. Check if the request exceeds the per-person limit of 4.
        3. Check if the request exceeds the actual tickets remaining.
        4. Return True if all checks pass, otherwise False.
    Return: bool: True if valid, False if invalid.
    """
    # Verify the request is within the 1-4 range and doesn't exceed stock
    # This prevents the program from selling more tickets than available
    if requested <= 0:
        print("Please enter a positive number.")
        return False

    if requested > MAX_TICKETS_PER_BUYER:
        print(f"Limit exceeded. You can only buy up to "
              f"{MAX_TICKETS_PER_BUYER} tickets.")
        return False

    if requested > remaining:
        print(f"Only {remaining} tickets left. Please adjust your amount.")
        return False

    return True


def run_ticket_sale():
    """
    Brief Description: Manages the main sale loop and displays final results.
    Parameters: None
    Variables:
        tickets_remaining (int): Tracks inventory, starting at 20.
        buyer_count (int): Accumulator to track total successful transactions.
        user_request (int): The integer input provided by the user.
    Logical Steps:
        1. Initialize ticket count and buyer accumulator.
        2. Enter a while loop that runs until tickets_remaining is 0.
        3. Prompt user for input and validate it is an integer.
        4. Call validate_purchase() to check against business rules.
        5. Update ticket count and buyer count if valid.
        6. Display final buyer total after the loop ends.
    Return: None
    """
    tickets_remaining = TOTAL_TICKETS_AVAILABLE
    buyer_count = 0

    print("--- Welcome to the Cinema Ticket Pre-Sale ---")

    # Continue the sale until the inventory reaches zero
    while tickets_remaining > 0:
        try:
            print(f"\nTickets currently available: {tickets_remaining}")

            # Get input and convert to integer for calculation
            user_request = int(input("Please enter the number of tickets you wish to purchase: "))

            # Check if the requested amount meets all business rules
            if validate_purchase(user_request, tickets_remaining):
                tickets_remaining -= user_request

                # Increment to track the total number of unique buyers
                buyer_count += 1
                print(f"Purchase successful! {tickets_remaining} tickets left.")

        except ValueError:
            # Handle non-integer inputs to prevent the program from crashing
            print("Invalid input. Please enter a whole number.")

    # Display final results once the loop terminates (all tickets sold)
    print("\n--- All tickets have been sold! ---")
    print(f"The total number of buyers was: {buyer_count}")


if __name__ == "__main__":
    run_ticket_sale()

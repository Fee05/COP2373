def calculate_spam_score(message):
    """
    Scans a string for 30 common spam keywords and calculates a total score.

    Parameters:
        message (str): The text string entered by the user to be analyzed.

    Returns:
        score (int): The total count of spam keywords detected.
        flagged_words (list): A list of the specific keywords found in the text.
    """
    # Initialize variables
    score = 0
    flagged_words = []

    # Comprehensive list of 30 common spam keywords/phrases
    spam_keywords = [
        "winner", "free", "urgent", "cash", "prize", "claim now", "offer",
        "lottery", "congratulations", "billion", "unsecured", "debt",
        "expire", "guaranteed", "investment", "refund", "security", "bonus",
        "hidden", "opportunity", "unlimited", "membership", "billing",
        "account", "verify", "password", "cheap", "click here", "legal", "act now"
    ]

    # Convert to lowercase for case-insensitive matching
    clean_message = message.lower()

    for word in spam_keywords:
        # Use .count() to score every occurrence of the word
        count = clean_message.count(word)
        if count > 0:
            score += count
            flagged_words.append(word)

    return score, flagged_words


def main():
    """
    Handles user input and displays the final spam analysis report.
    """
    print("--- Official Spam Analyzer (Tory Menifee) ---")
    user_input = input("Enter the message you want to scan for spam:\n> ")

    if not user_input.strip():
        print("Error: Message cannot be empty.")
        return

    # Call the score function and unpack both return values
    final_score, words_detected = calculate_spam_score(user_input)

    # Determine the likelihood based on the score
    if final_score >= 6:
        likelihood = "High Likelihood"
    elif 3 <= final_score <= 5:
        likelihood = "Moderate Likelihood"
    else:
        likelihood = "Low Likelihood"

    # Display Results
    print("\n" + "=" * 30)
    print("SPAM SCAN RESULTS")
    print("=" * 30)
    print(f"Total Spam Score:  {final_score}")
    print(f"Likelihood Rating: {likelihood}")

    # Display the "Causes" as required by the prompt
    if words_detected:
        print(f"Flagged phrases:   {', '.join(words_detected)}")
    else:
        print("Flagged phrases:   None")
    print("=" * 30)


# Run the program
if __name__ == "__main__":
    main()
import random


# Deck Class exactly as presented in Section 11.5
class Deck():
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            print('Reshuffling...!!!')
        self.current_card += 1
        return self.card_list[self.current_card - 1]


def get_card_name(card_num):
    # Logic from Section 11.5 to convert 0-51 into rank and suit
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']

    r = card_num % 13
    s = card_num // 13
    return f"{ranks[r]} of {suits[s]}"


def display_hand(hand):
    # Formats and displays the current Poker hand
    print("\nYour current Poker hand:")
    for i, card_val in enumerate(hand, 1):
        print(f"{i}: {get_card_name(card_val)}")


def play_poker_game():
    # Main function to handle the Poker game and draw phase
    my_deck = Deck(52)

    # Initial deal of 5 cards
    hand = [my_deck.deal() for _ in range(5)]
    display_hand(hand)

    # Draw phase
    print("\nEnter the card numbers to replace (e.g., 1, 3, 5) or press Enter to keep your hand.")
    replace_input = input("Selection: ")

    if replace_input.strip():
        try:
            # Convert input string to list of integer indices
            indices = [int(x.strip()) - 1 for x in replace_input.split(',')]

            for idx in indices:
                if 0 <= idx < 5:
                    hand[idx] = my_deck.deal()
                else:
                    print(f"Index {idx + 1} is invalid. Skipping.")

            print("\n--- Final Hand after Draw ---")
            display_hand(hand)
        except ValueError:
            print("Invalid input. Please use numbers and commas.")
    else:
        print("\nStaying with the current hand.")


if __name__ == "__main__":
    play_poker_game()
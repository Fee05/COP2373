import re


def split_into_sentences(text):
    """
    Uses regular expressions to split text into sentences based on
    punctuation followed by whitespace and a capital letter or digit.
    """
    # Pattern looks for . ! or ? followed by a space and a Capital or Digit
    sentence_list = re.split(r'(?<=[.!?])\s+', text)

    # Remove any empty strings resulting from extra spaces
    clean_sentences = [s.strip() for s in sentence_list if s.strip()]

    return clean_sentences


def display_results(sentences):
    """
    Iterates through the list of sentences to print them and
    displays the final count.
    """
    print("\n--- Individual Sentences ---")
    for index, sentence in enumerate(sentences, 1):
        print(f"{index}. {sentence}")

    total_count = len(sentences)
    print(f"\nTotal number of sentences: {total_count}")


def main():
    """
    Main entry point of the program. Handles user input.
    """
    print("Sentence Parser and Counter")
    paragraph = input("Enter a paragraph: ")

    if paragraph:
        sentence_data = split_into_sentences(paragraph)
        display_results(sentence_data)
    else:
        print("No text entered.")


if __name__ == "__main__":
    main()
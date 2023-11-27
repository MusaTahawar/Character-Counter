def count_characters(input_string):
    # Using len() to count the characters in the input string
    return len(input_string)

if __name__ == "__main__":
    # Get user input
    user_input = input("Enter a string: ")

    # Count characters
    character_count = count_characters(user_input)

    # Display the character count
    print(f"Number of characters: {character_count}")

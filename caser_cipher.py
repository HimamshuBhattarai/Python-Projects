import os

def welcome():
    """
    Prints a welcome message for the Caesar Cipher program.
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text using Caesar Cipher.")

def encrypt(text, shift):
    """
    Encrypts the given text using the Caesar Cipher with the specified shift.

    Args:
        text (str): The text to be encrypted.
        shift (int): The shift value for encryption.

    Returns:
        str: The encrypted text.
    """
    text = text.upper()
    result = ""

    for char in text:
        if char.isalpha():
            x = ord(char) + shift
            if char.isupper() and x > ord('Z'):
                x -= 26
            elif char.islower() and x > ord('z'):
                x -= 26

            y = chr(x)
            result = result +y
        else:
            result =result + char

    return result

def decrypt(text, shift):
    """
    Decrypts the given text using the Caesar Cipher with the specified shift.

    Args:
        text (str): The text to be decrypted.
        shift (int): The shift value for decryption.

    Returns:
        str: The decrypted text.
    """
    return encrypt(text, -shift)

def get_shift():
    """
    Gets the shift value from the user.

    Returns:
        int: The shift value entered by the user.
    """
    while True:
        try:
            shift = int(input("What is the shift number: "))
            return shift
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_user_choice():
    """
    Gets the user's choice for encryption or decryption.

    Returns:
        str: 'e' for encryption or 'd' for decryption.
    """
    while True:
        inp = input("Would you like to encrypt (e) or decrypt (d)?: ").lower()
        if inp in ('e', 'd'):
            return inp
        else:
            print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")

def get_message(action):
    """
    Gets the message from the user for encryption or decryption.

    Args:
        action (str): Either "encrypt" or "decrypt".

    Returns:
        str: The message entered by the user.
    """
    return input(f"What message would you like to {action}: ")

def is_file(filename):
    """
    Checks if the given file exists.

    Args:
        filename (str): The name of the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.exists(filename)

def write_messages(messages):
    """
    Writes a list of messages to a file named 'results.txt'.

    Args:
        messages (list): List of messages to be written to the file.

    Returns:
        str: The filename to which the messages are written.
    """
    filename = "results.txt"
    with open(filename, "w") as file:
        for msg in messages:
            file.write(msg + "\n")
    print(f"Output written to: {filename}")
    return filename

def process_file(filename, mode):
    """
    Processes a file for encryption or decryption.

    Args:
        filename (str): The name of the file to be processed.
        mode (str): 'e' for encryption or 'd' for decryption.

    Returns:
        list: List of messages resulting from the processing.
    """
    messages = []

    if is_file(filename):
        shift_key = int(input("Enter the shift number: "))
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if mode == 'e':
                    encrypted_line = encrypt(line, shift_key)
                    messages.append(encrypted_line)
                elif mode == 'd':
                    decrypted_line = decrypt(line, shift_key)
                    messages.append(decrypted_line)
                else:
                    print("Invalid mode")
                    return []

        return messages
    else:
        print(f"Invalid file: '{filename}' not found.")
        return []

def main():
    """
    The main function that runs the Caesar Cipher program.
    """
    welcome()

    while True:
        mode = get_user_choice()

        if mode == 'e' or mode == 'd':
            choice = input("Do you want to process a file (f) or a message (m)?: ").lower()

            if choice == 'f':
                filename = input("Enter the filename: ")
                messages = process_file(filename, mode)
                write_messages(messages)
            elif choice == 'm':
                message = get_message("encrypt" if mode == 'e' else "decrypt")
                shift = get_shift()
                result = encrypt(message, shift) if mode == 'e' else decrypt(message, shift)
                print(result)
            else:
                print("Invalid choice.")

            another_message = input("Would you like to encrypt or decrypt another message or process another file? (y/n): ").lower()
            if another_message != 'y':
                print("Thanks for using the program, goodbye!")
                break
        else:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")

if __name__ == "__main__":
    main()

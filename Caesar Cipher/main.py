import string

lowercase_alphabets = list(string.ascii_lowercase)
# Create a mapping for quick lookup: char -> index
# This is much more efficient than looping through lowercase_alphabets every time
alpha_to_index = {char: i for i, char in enumerate(lowercase_alphabets)}
index_to_alpha = {i: char for i, char in enumerate(lowercase_alphabets)}


def encrypt_phrase(phrase, shift):
    encrypted_chars = []
    for char in phrase:
        if 'a' <= char <= 'z':  # Check if it's a lowercase letter
            original_index = alpha_to_index[char]
            shifted_index = (original_index + shift) % 26 # % 26 handles wrapping around (e.g., z + 1 = a)
            encrypted_char = index_to_alpha[shifted_index]
            encrypted_chars.append(encrypted_char)
        elif 'A' <= char <= 'Z': # Handle uppercase letters
            char_lower = char.lower() # Convert to lowercase for index lookup
            original_index = alpha_to_index[char_lower]
            shifted_index = (original_index + shift) % 26
            encrypted_char_lower = index_to_alpha[shifted_index]
            encrypted_chars.append(encrypted_char_lower.upper()) # Convert back to uppercase
        else:
            encrypted_chars.append(char) # Keep non-alphabetic characters as they are
    return "".join(encrypted_chars) # Join the list back into a string

def decrypt_phrase(phrase,shift):
    decrypted_chars = []
    for char in phrase:
        if 'a' <= char <= 'z': #Check if it's a lowercase letter
            original_index = alpha_to_index[char]
            shifted_index = (original_index - shift) % 26
            decrypted_char_lower = index_to_alpha[shifted_index]
            decrypted_chars.append(decrypted_char_lower.upper())
        elif 'A' <= char <= 'Z': # Handle uppercase letters
            char_lower = char.lower() # Convert to lowercase for index lookup
            original_index = alpha_to_index[char_lower]
            shifted_index = (original_index - shift) % 26
            decrypted_char_lower = index_to_alpha[shifted_index]
            decrypted_chars.append(decrypted_char_lower.upper()) # Convert back to uppercase

        else:
            decrypted_chars.append(char)
    return "".join(decrypted_chars)


# --- Your main game loop (simplified for demonstration) ---
userTermination = False
while not userTermination:
    userInput = input("Enter 'encrypt' or 'decrypt' or 'quit': ").lower()

    if userInput == "encrypt":
        userInputPhrase = input("Enter word or phrase to encrypt: ").lower() # Keep it lowercase for easier logic
        
        while True: # Loop to ensure valid shift number
            try:
                userShiftNumber = int(input("Enter shift number: "))
                break # Exit loop if conversion is successful
            except ValueError:
                print("Invalid shift number. Please enter an integer.")

        encrypted_result = encrypt_phrase(userInputPhrase, userShiftNumber)
        print("Encrypted Phrase:", encrypted_result)
    
    elif userInput == "decrypt":
        userInputPhrase = input("Enter word or phrase to decrypt: ").lower() # Keep it lowercase for easier logic
        
        while True: # Loop to ensure valid shift number
            try:
                userShiftNumber = int(input("Enter shift number: "))
                break # Exit loop if conversion is successful
            except ValueError:
                print("Invalid shift number. Please enter an integer.")

        decrypted_result = decrypt_phrase(userInputPhrase, userShiftNumber)
        print("Decrypted Phrase:", decrypted_result)

    elif userInput == "quit":
        userTermination = True
        print("Exiting game. Goodbye!")
    else:
        print("Invalid command. Please enter 'encrypt' or 'quit'.")
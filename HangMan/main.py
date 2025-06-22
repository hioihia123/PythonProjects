import random

word_list = ["USA", "Hello", "President"]

def mask_word(word):
    # Create a string of asterisks with the same length as the word
    masked_replacement = '*' * len(word)
    return masked_replacement

def playTheGame():
    # Randomly choose a word from the word-list
    chosen_word = random.choice(word_list)
    
    # Initialize masked_word as a list of characters for easier updating
    masked_display = list(mask_word(chosen_word)) 
    
    print("Welcome to Guess the Word!")
    print("The word is:", "".join(masked_display)) # Convert list back to string for printing

    correctGuess = 0
    incorrectGuess = 0
    
    # Keep track of letters already guessed
    guessed_letters = [] 

    # Game loop - continue until word is guessed or too many incorrect guesses
    max_incorrect_guesses = 6 # You can adjust this

    while "*" in masked_display and incorrectGuess < max_incorrect_guesses:
        userInput = input("Guess a letter: ").lower()

        if len(userInput) != 1 or not userInput.isalpha():
            print("Please enter a single letter.")
            continue # Ask for input again

        if userInput in guessed_letters:
            print(f"You already guessed '{userInput}'. Try another letter.")
            print("Current word:", "".join(masked_display))
            continue

        guessed_letters.append(userInput) # Add to guessed letters

        found_in_word = False
        # Iterate through the chosen_word with its index
        for i, char_in_word in enumerate(chosen_word.lower()): # Convert chosen_word to lower for comparison
            if userInput == char_in_word:
                masked_display[i] = chosen_word[i] # Reveal the letter at its position
                correctGuess += 1
                found_in_word = True
        
        if found_in_word:
            print("You guessed correctly!")
        else:
            incorrectGuess += 1
            print(f"Incorrect guess! You have {max_incorrect_guesses - incorrectGuess} guesses left.")

        print("Current word:", "".join(masked_display)) # Print the updated masked word
        print("Guessed letters:", ", ".join(sorted(guessed_letters)))
        print("-" * 20) # Separator

    if "*" not in masked_display:
        print(f"Congratulations! You guessed the word: {chosen_word}")
    else:
        print(f"Game over! You ran out of guesses. The word was: {chosen_word}")

# --- To make your script run, you need to call the playTheGame() function ---
playTheGame()
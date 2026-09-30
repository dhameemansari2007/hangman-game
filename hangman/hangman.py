import random

# Predefined list of 5 words themed around gravity/anti-gravity
words = ["gravity", "orbit", "weight", "planet", "float"]

# Pick a random word from the list
secret_word = random.choice(words)

# List to keep track of letters the player has guessed
guessed_letters = []

# Counter for incorrect guesses
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman!")
print("Theme: Gravity and Anti-Gravity")
print("You have 6 incorrect guesses allowed.")

# Main game loop
while wrong_guesses < max_wrong:
    # Build the display string using standard for loop and string concatenation
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display = display + letter + " "
        else:
            display = display + "_ "
    
    print("\nWord: " + display)
    
    # Check if the player has guessed all the letters
    all_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            all_guessed = False
            break
            
    if all_guessed:
        print("Congratulations! You guessed the word: " + secret_word)
        break

    # Get the player's guess
    guess = input("Guess a letter: ").lower()

    # Check if the guess was already made
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in secret_word:
        print("Good job! That letter is in the word.")
        guessed_letters.append(guess)
    else:
        print("Wrong guess!")
        guessed_letters.append(guess)
        wrong_guesses = wrong_guesses + 1
        print("Incorrect guesses left: " + str(max_wrong - wrong_guesses))

# If player used up all guesses
if wrong_guesses == max_wrong:
    print("\nGame Over! You ran out of guesses.")
    print("The word was: " + secret_word)

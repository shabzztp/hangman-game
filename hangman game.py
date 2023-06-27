import random

def hangman():
    word_list = ["python", "hangman", "game", "programming", "computer", "player"]
    chosen_word = random.choice(word_list)
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while True:
        hidden_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_ "

        print("\nGuess the word:", hidden_word)

        if hidden_word == chosen_word:
            print("Congratulations! You guessed the word correctly.")
            break

        if attempts == max_attempts:
            print("You lost! The word was:", chosen_word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            guessed_letters.append(guess)

            if guess in chosen_word:
                print("Correct guess!")
            else:
                attempts += 1
                print("Wrong guess! Attempts left:", max_attempts - attempts)

hangman()

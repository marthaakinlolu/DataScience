import random

mystery_words = ['mango', 'banana', 'cherry', 'watermelon', 'strawberry', 'orange', 'grape']

def select_word(word_list):
    return random.choice(word_list)
    
def play_game():
    mystery_word = select_word(mystery_words)
    guessed_letters = set()
    strikes = 0
    max_strikes = 7
    solved = False

    while not solved and strikes < max_strikes:
        # print current state of the mystery word
        current_state = ""
        for letter in mystery_word:
            if letter in guessed_letters:
                current_state += letter
            else:
                current_state += "_"
        print(f"Current state: {current_state}")
        
        # ask user to guess a letter
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif guess in mystery_word:
            print(f"Good guess! {guess} is in the mystery word.")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, {guess} is not in the mystery word.")
            strikes += 1
            print(f"You have {max_strikes - strikes} strikes left.")

        # check if the word has been fully revealed
        if set(mystery_word) == guessed_letters:
            solved = True

    # print end of game message
    if solved:
        print(f"Congratulations, you guessed the word: {mystery_word}")
    else:
        print(f"Sorry, you ran out of strikes. The word was {mystery_word}.")
play_game()

from utils import *
from string import ascii_letters

MAX_NUMBER_OF_TRIES = 8

def hangman_game() -> None:
    number_of_attempts = MAX_NUMBER_OF_TRIES
    word_to_guess = random_word()
    guessed_word = list('*' * len(word_to_guess))
    player_name = input("Enter your name to start the game: ")
    first_game, score = get_player_score(player_name)
    print(bcolors.OKGREEN + f"\n{'Welcome' if first_game else 'Welcome Back'} {player_name}" + bcolors.ENDC)
    print("\n- Your score is:", score)
    print(f"\n- The word to guess have {len(word_to_guess)} letters.")
    print(f"\n- You have {number_of_attempts} attempts to guess the word.")

    while number_of_attempts > 0:
        letter = input(f"\n{input_message(guessed_word)}")
        letter = letter.lower()

        try:
            assert len(letter) == 1 and letter in ascii_letters
        except AssertionError:
            print(bcolors.FAIL + "\nError: You must enter a letter!" + bcolors.ENDC)
            continue
        else:
            if letter in word_to_guess:
                letter_position = word_to_guess.index(letter)
                if letter in guessed_word:
                    letter_position = word_to_guess.index(letter, letter_position + 1)
                guessed_word[letter_position] = letter
            print(bcolors.OKBLUE + "".join(guessed_word) + bcolors.ENDC)
            number_of_attempts -= 1

        if "".join(guessed_word) == word_to_guess:
            score += number_of_attempts
            print(bcolors.OKGREEN + f"Congratulations {player_name}, you guessed the word “{word_to_guess}” with {MAX_NUMBER_OF_TRIES - number_of_attempts} attempts." + bcolors.ENDC)
            break
        else:
            if number_of_attempts == 0:
                print(bcolors.FAIL + f"\nGame Over: The word to guess was {word_to_guess}" + bcolors.ENDC)
                break
            print(bcolors.WARNING + f"\nNumber of attempts remaining: {number_of_attempts}" + bcolors.ENDC)
        
    update_player_score(player_name, score)
                
    
if __name__ == "__main__":
    hangman_game()
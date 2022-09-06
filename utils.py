import pickle
import random 

def random_word() -> str:
    """
    This function reads the words contained in the file 
    words.txt returns a random word included in the list.        
    """

    with open("words.txt", "r") as file:
        words = file.read().splitlines()
    words = [word for word in words if len(word) < 9]
    return random.choice(words)


def save_score(score: dict) -> None:
    """
    This function is intended to save in a file the
    score of the players contained in the score object.
    """

    with open("scores", "wb") as file:
        pickler = pickle.Pickler(file)
        pickler.dump(score)


def read_score() -> dict:
    """
    Returns a dict containing the players' scores.
    """

    try:
        with open("scores", "rb") as file:
            pickler = pickle.Unpickler(file)
            return pickler.load()
    except:
        return {}


def get_player_score(name: str) -> tuple:
    """
    Returns a tuple object containing respectively a boolean that
    determines whether the player is new or old and the player's score.
    """

    saved_score = read_score()

    name = name.lower()

    if name in saved_score.keys():
        return False, saved_score[name]
    
    saved_score[name] = 0
    save_score(saved_score)

    return True, 0

def update_player_score(name: str, score: int) -> None:
    """
    Update the player's score in the score object.
    """

    saved_score = read_score()
    name = name.lower()
    saved_score[name] = score
    save_score(saved_score)

def input_message(guessed_word: list) -> str:
    """
    It formats the input message according to the remaining letters to guess.
    """

    count = len(guessed_word) - guessed_word.count('*')

    if count == 0:
        return "Enter the first letter to guest the word: "
    elif count == 1:
        return "Enter the second letter to guest the word: "
    elif count == 2:
        return "Enter the third letter to guest the word: "
    elif count == 3:
        return "Enter the fourth letter to guest the word: "
    elif count == 4:
        return "Enter the fith letter to guest the word: "
    elif count == 5:
        return "Enter the sixth letter to guest the word: "
    elif count == 6:
        return "Enter the seventh letter to guest the word: "
    elif count == 7:
        return "Enter the eighth letter to guest the word: "

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
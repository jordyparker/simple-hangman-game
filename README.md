# hangman game

It is a game that randomly generates a word and asks the player to guess it with a set number of tries. 

## How it works

When the player starts the game, the program first asks for his name in order to add or update his score in an object containing the scores of all players. This object is saved in a text file and will be updated every time a player finishes a game.

The number of letters of the word to guess is less than 9 and the player only have 8 attempts to guess the random word.

At each game, we add the number of remaining attempts as game points to the score. If, for example, I have three attempts left when I find the word, I win three points.
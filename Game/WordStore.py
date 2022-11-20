import random

words = ["ancestor","cause","coma","custody","available","resolution","dedicate","understanding",
             "approval","commemorate","vigorous","fresh","bland","queen","foster", "rider","present",
             "paralyzed","enfix","overcharge","aloof","exclusive","delivery","retirement","shorts"]


class WordStore:
    """The WordStore class is responsble for randomly choosing a word and verifying if the player guesses correctly

    Attributes:
        words: the list of words available in the game
        selected_word: the randomly chosen word
    
    
    """

    selected_word = ""     

    def __init__(self):
        self.selected_word = random.choice(words)


    def correct_guess(self, guess):
        """Returns if the correct word was guessed or if the character is in the word
        
        Args:
            guess: the guess is either a word or a character
        """
        if len(guess) == 1 and guess.isalpha():
            return guess in self.selected_word 
        elif len(guess) == len(self.selected_word):
            return guess == self.selected_word
        else:
            return False

    def filled_out_chars(self, guessed_lettters):
        """Prints the word with blanks for letters that have not been guessed and letters in the correct places
        
        Args:
            guessed_letters: the letters that have been guessed
        """
        filled_out_word = ""
        for c in self.selected_word:
            if(c in guessed_lettters):
                filled_out_word += f"{c} "
            else:
                filled_out_word += '_ '
        return filled_out_word
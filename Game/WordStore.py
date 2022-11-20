import random

words = ["ancestor","cause","coma","custody","available","resolution","dedicate","understanding",
             "approval","commemorate","vigorous","fresh","bland","queen","foster", "rider","present",
             "paralyzed","enfix","overcharge","aloof","exclusive","delivery","retirement","shorts"]


class WordStore:

    selected_word = ""     

    def __init__(self):
        self.selected_word = random.choice(words)


    def correct_guess(self, guess):
        if len(guess) == 1 and guess.isalpha():
            return guess in self.selected_word 
        elif len(guess) == len(self.selected_word):
            return guess == self.selected_word
        else:
            return False

    def filled_out_chars(self, guessed_lettters):
        filled_out_word = ""
        for c in self.selected_word:
            if(c in guessed_lettters):
                filled_out_word += f"{c} "
            else:
                filled_out_word += '_ '
        return filled_out_word
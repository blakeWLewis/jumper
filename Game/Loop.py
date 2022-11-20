from Game.WordStore import WordStore
from Game.Board import Board

class Loop:
    """The game loop that controls the play of the game
    
    
    """

    def start_game(self):
        """This is the main function of the game loop
        
        Args:
            bad_guesses: the number of guesses that did not result in a correct letter being found or whole words that were wrong
            guessed_letters: the letters that have already been guessed
            winner: true if the player has guessed the word or all of the letters

        """
        bad_guesses = 0
        guessed_letters = []
        winner = False

        print("Game starting")
        word_store = WordStore()
        print(f"Random word: {word_store.selected_word}")

        board = Board()

        filled_out_chars = word_store.filled_out_chars([])
        print(filled_out_chars)

        board.printJumper(bad_guesses)

        while bad_guesses < 4 and not winner:
            guess = input("Guess a letter [a-z]: ")

            if len(guess) == 1:
                if guess in guessed_letters:
                    print(f"You already guessed {guess}")
                elif word_store.correct_guess(guess):
                    guessed_letters.append(guess)
                    word_store.filled_out_chars(guessed_letters)
                    characters_in_selected_word = set(word_store.selected_word)
                    winner = len(characters_in_selected_word - set(guessed_letters)) == 0
                else:
                    guessed_letters.append(guess)
                    print(f"Sorry {guess} isn't in the word!")
                    bad_guesses += 1
            else:
                if word_store.correct_guess(guess):
                    print(f"You guessed the correct word: {word_store.selected_word}")
                    winner = True
                else:
                    print(f"{guess} is not the word :(")
                    bad_guesses += 1
            
            print(f"\n{word_store.filled_out_chars(guessed_letters)}")
            board.printJumper(bad_guesses)


        if winner:
            print(f"You won the game!")
        else:
            print(f"You lost the word was {word_store.selected_word}")
        







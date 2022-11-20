from WordStore import WordStore

ws = WordStore()

def test_correct_guess_char_method():
    print(f"selected_word = {ws.selected_word}")
    guess = ws.selected_word[0]
    assert ws.correct_guess(guess), "Should have been correct"

def test_correct_guess_word_method():
    print(f"selected_word = {ws.selected_word}")
    guess = ws.selected_word
    assert ws.correct_guess(guess), "Should have been correct"

def test_incorrect_guess_char_method():
    print(f"selected_word = {ws.selected_word}")
    characters = set('abcdefghijklmnopqrstuvwxyz')
    not_in_string = characters - set(ws.selected_word)
    print(f"chars not in {ws.selected_word} were {not_in_string}")
    guess = next(iter(not_in_string))
    assert not ws.correct_guess(guess), "Should have been incorrect"

def test_incorrect_guess_word_method():
    print(f"selected_word = {ws.selected_word}")
    guess = "Frank"
    assert not ws.correct_guess(guess), "Should have been incorrect"

def test_filled_out_chars_method():
    ws.filled_out_chars(['a','b','c','d'])
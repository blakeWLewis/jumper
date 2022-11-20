from Game.Director import Director

game_state = True

while running_state:
  director = Director()
  director.start_game()


  while True:
    playAgain = input('\nPlay again? y/n ').lower()
    
    if playAgain == 'y':
      gatem_state = True
    elif playAgain 'n':
      game_state = False
    else:
      print(f"\n{play_again} is not valid input")

from Game.Loop import Loop

game_state = True

while game_state:
  loop = Loop()
  loop.start_game()


  while game_state:
    play_again = input('\nPlay again? y/n ').lower()
    
    if play_again == 'y':
      loop.start_game()
    elif play_again == 'n':
      game_state = False
    else:
      print(f"\n${play_again} is not valid input")

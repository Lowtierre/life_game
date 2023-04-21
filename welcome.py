print("Welcome in Game of Life!!")
user_name = input("\nWhat's your name? ")
new_or_old = input(f"\nHi, {user_name}! Do you create a new simulation or start an old one? Press 'N' for a new simulation, or 'O' for a simulation already existing. ")

while new_or_old != 'N' or new_or_old != 'n' or new_or_old != 'O' or new_or_old != 'o':
  if new_or_old == 'N' or new_or_old == 'n':
      grid_dim = input(f"\nEnter an integer between 2 and 50 to select the dimension of the grid. ")
      time_game = input(f"\nYou've chosen to play with a {grid_dim}-dimension grid. Now, tell me the numbers of generations the game should simulate. ")
      print(f"\nPerfect, {user_name}, this simulation will be in a {grid_dim}-dimension grid and its durate will be of {time_game} generations.")
      break
  elif new_or_old == 'O' or new_or_old == 'o':
      # choose a file from list of saved simulations
      pass
  else:
      new_or_old = input("Should you press 'N' or 'O'. ")

game_features = {'dim': grid_dim, 'time': time_game}
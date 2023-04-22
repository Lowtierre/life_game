import os
import re
from game import *

cells = []

saved_games = os.getcwd() + "\saved_games"
saved_files = os.listdir(saved_games)

print("""  ___    __    __  __  ____    _____  ____    __    ____  ____  ____ 
 / __)  /__\  (  \/  )( ___)  (  _  )( ___)  (  )  (_  _)( ___)( ___)
( (_-. /(__)\  )    (  )__)    )(_)(  )__)    )(__  _)(_  )__)  )__) 
 \___/(__)(__)(_/\/\_)(____)  (_____)(__)    (____)(____)(__)  (____)
 """)
print("______________________________________________________________________")
print("\nWelcome in the Game of Life.")
user_name = input("\nWhat's your name? ")
new_or_old = input(f"\nHi, {user_name}! Do you wanna create a new simulation or start an old one? Press 'N' for a new simulation, or 'O' for a simulation already existing. ")

# create a while loop so that each time user doesn't press 'n' or 'o' s/he can try again

while new_or_old.lower() != 'n' or new_or_old.lower() != 'o':
  if new_or_old == 'N' or new_or_old == 'n':
    grid_dim = input(f"\nEnter an integer between 2 and 50 to select the dimension of the grid. ")
    time_game = input(f"\nYou've chosen to play with a {grid_dim}-dimension grid. Now, tell me the numbers of generations the game should simulate. ")
    percentage = input(f"\nFinally, enter an integer between 0 and 10 to decide the percentage of alive cells. ")
    
    l = int(grid_dim)
    t = int(time_game)
    p = int(percentage)

    print(f"\nPerfect, {user_name}, this simulation will be in a {grid_dim}-dimension grid and its durate will be of {time_game} generations.")
    # create simulation
    create_grid(l, t, cells)
    grid_code = write_init_grid(l, cells)
    create_binds(cells, l)
    simulation(l, t, cells)
    saving = input("\nThe simulation is over. Do you wanna save it? (Press 'Y' if you want, otherwise press each other key) ")
    if saving.lower() == 'y':
       name_file = input("\nWhat's the name do you want to give it? ")
       save_file(name_file, grid_code)
       print("Ok, your file was saved in saved_games subdirectory! See you soon!")
    break
  elif new_or_old == 'O' or new_or_old == 'o':
    # choose a file from list of saved simulations
    for file in saved_files:
        print(file)
    name = input("\nWrite the name of the file you want to open (without '.txt'). ")
    while f"{name}" not in saved_files:
      if f"{name}.txt" in saved_files:
        l = open_file(name, cells)
        time_game = input("\nHow many generations do you want to see? ")
        i = 0
        while re.search('\D+', time_game):
          while i > 0:
            time_game = input(">> ")
            break
          i += 1
          if not re.search('\D+', time_game):
            t = int(time_game)
            break
          else:
            print("\nYou must enter a number. ")
            continue
           
        create_binds(cells, l)
        simulation(l, t, cells)
        break
      else:
        name = input("Doesn't exist this file, re-write in a correct way! ")
    print("\nThe simulation is over! See you soon! ")
    break
  else:
      new_or_old = input("Should you press 'N' or 'O'. ")
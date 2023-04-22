import os

saved_games = os.getcwd() + "\saved_games"
saved_files = os.listdir(saved_games)
print(saved_files)
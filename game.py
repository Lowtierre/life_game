import random
import time
from welcome import game_features
from cell_class import Cell

# cell list

cells = []

# game parameters

l = int(game_features['dim'])
t = int(game_features['time'])

# create cells grid

for i in range(l):
    cells += [[]]
    for j in range(l):
        p = random.randrange(0, 10)
        if p >= 5:
            cell = Cell(i, j, True)
            cells[i] += [cell]
        else:
            cell = Cell(i, j, False)
            cells[i] += [cell]

initial_cells = cells

# function for neighborhood

def know_neighbors(cell):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (cell.x + i >= 0 and cell.x + i < l) and (cell.y + j >= 0 and cell.y + j < l) and (i != 0 or j != 0):
                cell.neighbors += [cells[cell.x + i][cell.y + j]]

# create neighborhood binds

for i in range(l):
    for j in range(l):
        know_neighbors(cells[i][j])

# create terminal grid

def draw_grid():
    for i in range(l):
        for j in range(l):
            cells[i][j].is_alive = cells[i][j].will_live
    grid = ''
    for i in range(l):
        row = ''
        for j in range(l):
            if cells[j][i].is_alive:
                row += ' A  '
            else:
                row += ' D  '
        grid += '\n\n' + row
    print(grid)

# create simulation

for m in range(t):
    time.sleep(1)
    for i in range(l):
        for j in range(l):
            cells[i][j].live_or_die()
    print(f"\n\nGeneration {m}:")
    draw_grid()

# save game 

with open(f"saved_games/{l}dim_{t}time.txt", "w") as game1:
    game1.write((str(initial_cells)))
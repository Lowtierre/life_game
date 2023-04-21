import random
import time
from welcome import game_features
from cell_class import Cell

# cell list

cells = []

# game parameters

l = int(game_features['dim'])
t = int(game_features['time'])
p = int(game_features['percent'])

# create cells grid
def create_grid(dim, percent, cell_list):
    for i in range(dim):
        cell_list += [[]]
        for j in range(dim):
            d = random.randrange(1, 11)
            if d <= percent:
                cell = Cell(i, j, True)
                cell_list[i] += [cell]
            else:
                cell = Cell(i, j, False)
                cell_list[i] += [cell]

# function for neighborhood

def know_neighbors(cell):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (cell.x + i >= 0 and cell.x + i < l) and (cell.y + j >= 0 and cell.y + j < l) and (i != 0 or j != 0):
                cell.neighbors += [cells[cell.x + i][cell.y + j]]

# create neighborhood binds
def create_binds(dim):
    for i in range(dim):
        for j in range(dim):
            know_neighbors(cells[i][j])

# create terminal grid

def draw_grid():
    for i in range(l):
        for j in range(l):
            cells[j][i].is_alive = cells[j][i].will_live
    grid = ''
    for i in range(l):
        row = ''
        for j in range(l):
            if cells[i][j].is_alive == True:
                row += f' A  '
            else:
                row += f' D  '
        grid += '\n\n' + row
    print(grid)

# create simulation
create_grid(l, p, cells)
initial_cells = cells

create_binds(l)

for m in range(t):
    time.sleep(1)
    for i in range(l):
        for j in range(l):
            if m == 0:
                continue
            cells[i][j].live_or_die()
    print(f"\n\nGeneration {m}:")
    draw_grid()

# save game 

with open(f"saved_games/{l}dim_simulation.txt", "w") as game1:
    game1.write((str(initial_cells)))
import random
import time
from cell_class import Cell

# create cells grid
def create_grid(dim, percent, cell_list):
    for i in range(dim):
        cell_list += [[]]
        for j in range(dim):
            d = random.randrange(1, 11)
            if d <= percent:
                cell = Cell(i, j, True)
            else:
                cell = Cell(i, j, False)
            cell_list[i] += [cell]

# save initial grid in new file

def write_init_grid(dim, cell_list):
    grid_code = f'{dim},'
    for i in range(dim):
        for j in range(dim):
            if cell_list[i][j].is_alive:
                grid_code += 'I'
            else:
                grid_code += 'O'
    return grid_code

def save_file(name, grid):
    with open(f"saved_games/{name}.txt", "w") as game1:
        game1.write((grid))

# function for neighborhood

def know_neighbors(cell_list, cell, dim):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (cell.x + i >= 0 and cell.x + i < dim) and (cell.y + j >= 0 and cell.y + j < dim) and (i != 0 or j != 0):
                cell.neighbors += [cell_list[cell.x + i][cell.y + j]]

# create neighborhood binds
def create_binds(cell_list, dim):
    for i in range(dim):
        for j in range(dim):
            know_neighbors(cell_list, cell_list[i][j], dim)

# create terminal grid

def draw_grid(cell_list, dim):
    for i in range(dim):
        for j in range(dim):
            cell_list[j][i].is_alive = cell_list[j][i].will_live
    grid = ''
    for i in range(dim):
        row = ''
        for j in range(dim):
            if cell_list[i][j].is_alive == True:
                row += f' I  '
            else:
                row += f' O  '
        grid += '\n\n' + row
    print(grid)

# simulate game

def simulation(dim, time_game, cell_list):
    for m in range(time_game):
        time.sleep(1)
        for i in range(dim):
            for j in range(dim):
                if m == 0:
                    continue
                cell_list[i][j].live_or_die()
        print(f"\n\nGeneration {m}:")
        draw_grid(cell_list, dim)

# open old file and create the grid

def open_file(name, cell_list):
    with open(f"saved_games/{name}.txt", "r") as file:
        file_grid = file.readline()
    grid = file_grid.split(',')
    index = 0
    for i in range(int(grid[0])):
        cell_list += [[]]
        for j in range(int(grid[0])):
            index += 1
            if grid[1][index - 1] == 'I':
                cell = Cell(i, j, True)
            else:
                cell = Cell(i, j, False)
            cell_list[i] += [cell]
    return int(grid[0])
import random
import time

class Cell():
    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.is_alive = life
        self.will_live = life
        self.neighbors = []

    def __repr__(self):
        return f"cell({self.x},{self.y})"
    
    def know_neighbors(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.x + i >= 0 and self.x + i < l) and (self.y + j >= 0 and self.y + j < l) and (i != 0 or j != 0):
                    self.neighbors += [cells[self.x + i][self.y + j]]
        print(f"The neighbors of cell({self.x},{self.y}) are: {self.neighbors}")

    def live_or_die(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.is_alive:
                count += 1
        if self.is_alive:
            if count < 2 or count > 3:
                self.will_live = False
        else:
            if count == 3:
                self.will_live = True


cells = []

l = 5
t = 5

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


# create neighborhood binds

for i in range(l):
    for j in range(l):
        cells[i][j].know_neighbors()

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
                row += '* '
            else:
                row += '^ '
        grid += '\n' + row
    print(grid)

# create simulation

for i in range(t):
    time.sleep(1)
    for i in range(l):
        for j in range(l):
            cells[i][j].live_or_die()
    draw_grid()
    

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = []

    def __repr__(self):
        return f"cell({self.x},{self.y})"
    
    def know_neighbors(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if (self.x + i >= 0 and self.x + i < l) and (self.y + j >= 0 and self.y + j < l) and (i != 0 or j != 0):
                    self.neighbors += [cells[self.x + i][self.y + j]]
        print(f"The neighbors of cell({self.x},{self.y}) are: {self.neighbors}")

cells = []

l = 3

# create cells grid

for i in range(l):
    cells += [[]]
    for j in range(l):
        cell = Cell(i, j)
        cells[i] += [cell]

# create neighborhood binds

for i in range(l):
    for j in range(l):
        cells[i][j].know_neighbors()

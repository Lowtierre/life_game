from welcome import game_features

l = int(game_features['dim'])

class Cell():
    def __init__(self, x, y, life):
        self.x = x
        self.y = y
        self.is_alive = life
        self.will_live = life
        self.neighbors = []

    def __repr__(self):
        return f"cell({self.x},{self.y})"

    def live_or_die(self):
        count = 0
        for neighbor in self.neighbors:
            if neighbor.is_alive:
                count += 1
        if self.is_alive:
            if count < 2 or count > 3:
                self.will_live = False
            else:
                self.will_live = True
        else:
            if count == 3:
                self.will_live = True


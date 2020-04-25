import numpy as np

class Constants:
    ALIVE, DEAD = 1, 0
    NUMBER_COLUMNS, NUMBER_ROWS = 50, 50

class GameState:
    def __init__(self):
        self.currentState = np.zeros((Constants.NUMBER_COLUMNS, Constants.NUMBER_ROWS))
        self.newState = np.copy(self.currentState)

    def get_number_neighbours(self, x, y):
        numberNeighbours =  self.currentState[(x - 1) % Constants.NUMBER_COLUMNS, (y - 1) % Constants.NUMBER_ROWS] + \
                            self.currentState[(x)     % Constants.NUMBER_COLUMNS, (y - 1) % Constants.NUMBER_ROWS] + \
                            self.currentState[(x + 1) % Constants.NUMBER_COLUMNS, (y - 1) % Constants.NUMBER_ROWS] + \
                            self.currentState[(x - 1) % Constants.NUMBER_COLUMNS, (y)     % Constants.NUMBER_ROWS] + \
                            self.currentState[(x + 1) % Constants.NUMBER_COLUMNS, (y)     % Constants.NUMBER_ROWS] + \
                            self.currentState[(x - 1) % Constants.NUMBER_COLUMNS, (y + 1) % Constants.NUMBER_ROWS] + \
                            self.currentState[(x)     % Constants.NUMBER_COLUMNS, (y + 1) % Constants.NUMBER_ROWS] + \
                            self.currentState[(x + 1) % Constants.NUMBER_COLUMNS, (y + 1) % Constants.NUMBER_ROWS]

        return numberNeighbours

    def is_dead(self, x, y):
        return self.newState[x, y] == Constants.DEAD

    def update_state(self, x, y, state):
        if state:
            self.newState[x, y] = Constants.ALIVE
        else:
            self.newState[x, y] = Constants.DEAD

    def draw(self, screen, x, y):
        from cell import Cell

        isDead = self.is_dead(x, y)

        cell = Cell(x, y, isDead)
        cell.draw(screen)

    def change_state_bypos(self, posX, posY):
        from cell import Constants as c

        x, y = int(np.floor(posX / c.WIDTH_CELL)), int(np.floor(posY / c.HEIGHT_CELL))
        self.change_state(x, y)
    
    def change_state(self, x, y):
        self.newState[x, y] = not self.newState[x, y]

    def swapp(self):
        self.currentState = np.copy(self.newState)

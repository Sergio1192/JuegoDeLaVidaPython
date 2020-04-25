import numpy as np

class Constants:
    from screen import Constants as s
    ALIVE, DEAD = 1, 0
    RATIO = 20
    NUMBER_COLUMNS, NUMBER_ROWS = int(np.floor(s.SCREEN_WIDTH / RATIO)), int(np.floor(s.SCREEN_HEIGHT / RATIO))

from cell import Cell
from rules import Rules

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

    def draw(self, screen):
        for y in range(0, Constants.NUMBER_ROWS):
            for x in range(0, Constants.NUMBER_COLUMNS):
                isDead = self.is_dead(x, y)

                cell = Cell(x, y, isDead)
                cell.draw(screen)

        self.swapp()

    def change_state_bypos(self, posX, posY):
        x, y = Cell.get_location(posX, posY)
        self.change_state(x, y)
    
    def change_state(self, x, y):
        self.newState[x, y] = not self.newState[x, y]

    def swapp(self):
        self.currentState = np.copy(self.newState)
    
    def action(self):
        for y in range(0, Constants.NUMBER_ROWS):
            for x in range(0, Constants.NUMBER_COLUMNS):
                numberNeighbours = self.get_number_neighbours(x, y)

                # Reglas
                if self.is_dead(x, y):
                    if Rules.born(numberNeighbours):
                        self.update_state(x, y, True)
                else:
                    if Rules.kill(numberNeighbours):
                        self.update_state(x, y, False)

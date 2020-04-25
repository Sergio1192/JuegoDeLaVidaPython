import pygame as pg

class Constants:
    from screen import Constants as s
    from game_state import Constants as gc

    SOLID_COLOR = 0
    CELL_ALIVE_COLOR = 255, 255, 255

    BORDER_WIDTH = 1
    CELL_DEAD_COLOR = 125, 125, 125

    WIDTH_CELL = int(s.SCREEN_WIDTH / gc.NUMBER_COLUMNS)
    HEIGHT_CELL = int(s.SCREEN_HEIGHT / gc.NUMBER_ROWS)

class Cell:
    def __init__(self, x, y, isDead):
        #poly = [
        #    ((x)     * widthCell, (y)     * heightCell),
        #    ((x + 1) * widthCell, (y)     * heightCell),
        #    ((x + 1) * widthCell, (y + 1) * heightCell),
        #    ((x)     * widthCell, (y + 1) * heightCell)
        #]
        
        self.cell = (x * Constants.WIDTH_CELL, y * Constants.HEIGHT_CELL, Constants.WIDTH_CELL, Constants.HEIGHT_CELL)
        
        if (isDead):
            self.color = Constants.CELL_DEAD_COLOR
            self.width = Constants.BORDER_WIDTH
        else:
            self.color = Constants.CELL_ALIVE_COLOR
            self.width = Constants.SOLID_COLOR
    
    def draw(self, screen):
        #pg.draw.polygon(screen, cellColor, poly, borderSize)
        pg.draw.rect(screen, self.color, self.cell, self.width)
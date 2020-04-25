import pygame as pg

class Constants:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
    BACKGROUND_COLOR = 0, 0, 0

class Screen:
    def __init__(self):
        self.screen = pg.display.set_mode((Constants.SCREEN_HEIGHT, Constants.SCREEN_WIDTH))

    def empty(self):
        self.screen.fill(Constants.BACKGROUND_COLOR)

    def show(self):
        pg.display.flip()
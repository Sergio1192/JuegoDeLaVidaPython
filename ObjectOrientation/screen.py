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

    def get_mouse_position(self):
        return pg.mouse.get_pos()
    
    def is_pressed(self):
        isKeyPressed = False
        isMousePressed = False

        events = pg.event.get()
        for event in events:
            if (event.type == pg.KEYDOWN):
                isKeyPressed = True
            if (event.type == pg.MOUSEBUTTONDOWN):
                isMousePressed = True
    
        return (isKeyPressed, isMousePressed)
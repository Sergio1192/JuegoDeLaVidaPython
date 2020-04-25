# Imports
import pygame as pg
import numpy as np
import time as t

# Variables
ALIVE = 1
DEAD = 0

SOLID_COLOR = 0
CELL_ALIVE_COLOR = 255, 255, 255
CELL_DEAD_COLOR = 125, 125, 125

BORDER_WIDTH = 1

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 1000
BACKGROUND_COLOR = 0, 0, 0
NUMBER_COLUMNS, NUMBER_ROWS = 50, 50

WIDTH_CELL = int(SCREEN_WIDTH / NUMBER_COLUMNS)
HEIGHT_CELL = int(SCREEN_HEIGHT / NUMBER_ROWS)

SLEEP_TIME = 0.1

isPaused = True

# Rules
NUMBER_MIN_KEEP_ALIVE = 2
NUMBER_MAX_KEEP_ALIVE = 3
NUMBER_RETURN_ALIVE = 2

# Estado de la celdas
gameState = np.zeros((NUMBER_COLUMNS, NUMBER_ROWS))
newGameState = np.copy(gameState)

# Pantalla
screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Bucle de ejecución
while True:
    screen.fill(BACKGROUND_COLOR)

    # Eventos
    events = pg.event.get()
    for event in events:
        if (event.type == pg.KEYDOWN):
            isPaused = not isPaused

        if (event.type == pg.MOUSEBUTTONDOWN):
            posX, posY = pg.mouse.get_pos()
            cellX, cellY = int(np.floor(posX / WIDTH_CELL)), int(np.floor(posY / HEIGHT_CELL))
            newGameState[cellX, cellY] = not newGameState[cellX, cellY]

    for y in range(0, NUMBER_ROWS):
        for x in range(0, NUMBER_COLUMNS):
            if not isPaused:
                numberNeighbours =  gameState[(x - 1) % NUMBER_COLUMNS, (y - 1) % NUMBER_ROWS] + \
                                    gameState[(x)     % NUMBER_COLUMNS, (y - 1) % NUMBER_ROWS] + \
                                    gameState[(x + 1) % NUMBER_COLUMNS, (y - 1) % NUMBER_ROWS] + \
                                    gameState[(x - 1) % NUMBER_COLUMNS, (y)     % NUMBER_ROWS] + \
                                    gameState[(x + 1) % NUMBER_COLUMNS, (y)     % NUMBER_ROWS] + \
                                    gameState[(x - 1) % NUMBER_COLUMNS, (y + 1) % NUMBER_ROWS] + \
                                    gameState[(x)     % NUMBER_COLUMNS, (y + 1) % NUMBER_ROWS] + \
                                    gameState[(x + 1) % NUMBER_COLUMNS, (y + 1) % NUMBER_ROWS]

                currentState = gameState[x, y]
                # Rules
                if currentState == DEAD:
                    if numberNeighbours == NUMBER_RETURN_ALIVE:
                        newGameState[x, y] = ALIVE
                else:
                    if numberNeighbours < NUMBER_MIN_KEEP_ALIVE or numberNeighbours > NUMBER_MAX_KEEP_ALIVE:
                        newGameState[x, y] = DEAD

            #poly = [
            #    ((x)     * widthCell, (y)     * heightCell),
            #    ((x + 1) * widthCell, (y)     * heightCell),
            #    ((x + 1) * widthCell, (y + 1) * heightCell),
            #    ((x)     * widthCell, (y + 1) * heightCell)
            #]

            #pg.draw.polygon(screen, cellColor, poly, borderSize)

            rect = (x * WIDTH_CELL, y * HEIGHT_CELL, WIDTH_CELL, HEIGHT_CELL)

            if (newGameState[x, y] == DEAD):
                currentColor = CELL_DEAD_COLOR
                width = BORDER_WIDTH
            else:
                currentColor = CELL_ALIVE_COLOR
                width = SOLID_COLOR

            pg.draw.rect(screen, currentColor, rect, width)

    gameState = np.copy(newGameState)

    pg.display.flip()

    t.sleep(SLEEP_TIME)

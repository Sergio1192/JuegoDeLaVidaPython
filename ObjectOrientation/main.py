# Imports
import pygame as pg
import time as t

from screen import Screen
from game_state import GameState
from game_state import Constants as GameStateContants

# Variables
SLEEP_TIME = 0.1

isPaused = True

# Rules
NUMBER_MIN_KEEP_ALIVE = 2
NUMBER_MAX_KEEP_ALIVE = 3
NUMBER_RETURN_ALIVE = 2

# Estado de la celdas
gameState = GameState()

# Pantalla
screen = Screen()

# Bucle de ejecución
while True:
    screen.empty()

    # Eventos
    events = pg.event.get()
    for event in events:
        if (event.type == pg.KEYDOWN):
            isPaused = not isPaused
        
        if (event.type == pg.MOUSEBUTTONDOWN):
            posX, posY = pg.mouse.get_pos()
            gameState.change_state_bypos(posX, posY)

    for y in range(0, GameStateContants.NUMBER_ROWS):
        for x in range(0, GameStateContants.NUMBER_COLUMNS):
            if not isPaused:
                numberNeighbours = gameState.get_number_neighbours(x, y)

                # Rules
                if gameState.is_dead(x, y):
                    if numberNeighbours == NUMBER_RETURN_ALIVE:
                        gameState.update_state(x, y, True)
                else:
                    if numberNeighbours < NUMBER_MIN_KEEP_ALIVE or numberNeighbours > NUMBER_MAX_KEEP_ALIVE:
                        gameState.update_state(x, y, False)

            gameState.draw(screen.screen, x, y)

    gameState.swapp()

    screen.show()

    t.sleep(SLEEP_TIME)

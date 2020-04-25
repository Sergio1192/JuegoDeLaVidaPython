# Imports
import time as t

from rules import Rules
from screen import Screen
from game_state import GameState
from game_state import Constants as GameStateContants

# Variables
SLEEP_TIME = 0.1
isPaused = True

# Estado de la celdas
gameState = GameState()

# Pantalla
screen = Screen()

# Bucle de ejecución
while True:
    screen.empty()

    # Eventos
    isKeyPressed, isMousePressed = screen.is_pressed()
    if isKeyPressed:
        isPaused = not isPaused
    
    if isMousePressed:
        posX, posY = screen.get_mouse_position()
        gameState.change_state_bypos(posX, posY)

    # Bucle
    for y in range(0, GameStateContants.NUMBER_ROWS):
        for x in range(0, GameStateContants.NUMBER_COLUMNS):
            if not isPaused:
                numberNeighbours = gameState.get_number_neighbours(x, y)

                # Reglas
                if gameState.is_dead(x, y):
                    if Rules.born(numberNeighbours):
                        gameState.update_state(x, y, True)
                else:
                    if Rules.kill(numberNeighbours):
                        gameState.update_state(x, y, False)

            # Dibujado
            gameState.draw(screen.screen, x, y)

    gameState.swapp()

    screen.show()

    t.sleep(SLEEP_TIME)

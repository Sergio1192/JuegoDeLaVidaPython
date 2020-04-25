# Imports
import time as t

from screen import Screen
from game_state import GameState

# Variables
SLEEP_TIME = 0.1
isPaused = True

# Estado de la celdas
gameState = GameState()

# Pantalla
screen = Screen()

# Bucle de ejecución
while True:
    # Eventos
    isKeyPressed, isMousePressed = screen.is_pressed()
    if isKeyPressed:
        isPaused = not isPaused
    
    if isMousePressed:
        posX, posY = screen.get_mouse_position()
        gameState.change_state_bypos(posX, posY)

    # Acciones que modifican el estado del juego
    if not isPaused:
        gameState.action()

    # Dibujado
    screen.empty()
    gameState.draw(screen.screen)
    screen.show()

    t.sleep(SLEEP_TIME)

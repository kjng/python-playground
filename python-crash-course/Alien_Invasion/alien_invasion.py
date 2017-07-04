import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
  # Initialize game and create a screen object
  pygame.init()
  pygame.display.set_caption("Alien Invasion")

  settings = Settings()

  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

  # Create ship
  ship = Ship(settings, screen)

  # Start the main loop of the game
  while True:
    # Handle keypresses and game events
    gf.check_events(ship)

    # Update ship position
    ship.update()

    # Redraw screen
    gf.update_screen(settings, screen, ship)

run_game()

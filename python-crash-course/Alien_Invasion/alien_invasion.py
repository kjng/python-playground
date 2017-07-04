import sys
import pygame

from settings import Settings

def run_game():
  # Initialize game and create a screen object
  pygame.init()
  pygame.display.set_caption("Alien Invasion")

  settings = Settings()

  screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

  # Start the main loop of the game
  while True:
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)

    # Make the most recently drawn screen visible
    pygame.display.flip()

run_game()

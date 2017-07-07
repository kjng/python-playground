import pygame

from rocket import Rocket

def run_game():
  pygame.init()
  pygame.display.set_caption("Rocket Game")

  screen = pygame.display.set_mode((1600, 900))

  rocket = Rocket(screen)

  while True:
    rocket.listen_movement()
    rocket.update()

    # Redraw screen
    screen.fill((255, 255, 255))
    rocket.blitme()
    pygame.display.flip()

run_game()

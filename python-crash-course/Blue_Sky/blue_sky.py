import sys
import pygame

def run_game():
  pygame.init()
  screen = pygame.display.set_mode((150, 150))
  pygame.display.set_caption('Blue Sky')

  # Blue background
  screen.fill((0, 0, 255))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

    pygame.display.flip()

run_game()

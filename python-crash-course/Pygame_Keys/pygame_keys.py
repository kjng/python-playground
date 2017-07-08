import sys
import pygame

def run_app():
  pygame.init()
  pygame.display.set_caption("Pygame Keys")
  pygame.display.set_mode((250, 100))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        print(event.key)

run_app()

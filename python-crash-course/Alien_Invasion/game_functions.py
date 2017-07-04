import sys
import pygame

def check_events(ship):
  """Respond to keypresses and game events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

    elif event.type == pygame.KEYDOWN:
      # Move ship to right
      if event.key == pygame.K_RIGHT:
        ship.moving_right = True
      elif event.key == pygame.K_LEFT:
        ship.moving_left = True

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        ship.moving_right = False
      elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(settings, screen, ship):
  """Update screen for each pass of loop"""
  screen.fill(settings.bg_color)
  ship.blitme()

  # Show most recent screen
  pygame.display.flip()

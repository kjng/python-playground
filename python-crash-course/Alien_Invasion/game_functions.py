import sys
import pygame

def check_events(ship):
  """Respond to keypresses and game events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      check_keydown_events(event, ship)
    elif event.type == pygame.KEYUP:
      check_keyup_events(event, ship)

def update_screen(settings, screen, ship):
  """Update screen for each pass of loop"""
  screen.fill(settings.bg_color)
  ship.blitme()

  # Show most recent screen
  pygame.display.flip()

def check_keydown_events(event, ship):
  # Move ship to right
  if event.key == pygame.K_RIGHT:
    ship.moving_right = True
  elif event.key == pygame.K_LEFT:
    ship.moving_left = True

def check_keyup_events(event, ship):
  if event.key == pygame.K_RIGHT:
    ship.moving_right = False
  elif event.key == pygame.K_LEFT:
    ship.moving_left = False

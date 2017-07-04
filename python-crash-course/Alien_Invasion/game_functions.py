import sys
import pygame

def check_events():
  """Respond to keypresses and game events"""
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

def update_screen(settings, screen, ship):
  """Update screen for each pass of loop"""
  screen.fill(settings.bg_color)
  ship.blitme()

  # Show most recent screen
  pygame.display.flip()

import pygame

class Ship():
  def __init__(self, screen):
    """Initialize ship and set its starting position"""
    self.screen = screen

    # Load ship image and get rectangle
    self.image = pygame.image.load('ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start ship at bottom in the center of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

  def blitme(self):
    """Draw ship at location"""
    self.screen.blit(self.image, self.rect)

import pygame

class Ship():
  def __init__(self, settings, screen):
    """Initialize ship and set its starting position"""
    self.screen = screen
    self.settings = settings

    # Load ship image and get rectangle
    self.image = pygame.image.load('ship.bmp')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start ship at bottom in the center of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = self.screen_rect.bottom

    # Movement flags
    self.moving_right = False
    self.moving_left = False

    # Store decimal of ship's center
    self.center = float(self.rect.centerx)

  def update(self):
    if self.moving_right:
      self.center += self.settings.ship_speed_factor
      if self.rect.right > self.screen_rect.right + self.rect.width:
        self.center = 0
    if self.moving_left:
      self.center -= self.settings.ship_speed_factor
      if self.rect.left < 0 - self.rect.width:
        self.center = self.settings.screen_width

    self.rect.centerx = self.center

  def blitme(self):
    """Draw ship at location"""
    self.screen.blit(self.image, self.rect)

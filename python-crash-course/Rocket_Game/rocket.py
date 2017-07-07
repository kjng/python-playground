import sys
import pygame

class Rocket():
  def __init__(self, screen):
    self.screen = screen

    self.speed = 1.5

    self.image = pygame.image.load("rocket.bmp")
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()

    # Start ship at center of the screen
    self.rect.centerx = self.screen_rect.centerx
    self.rect.centery = self.screen_rect.centery

    # Movement flags
    self.moving_up = False
    self.moving_right = False
    self.moving_down = False
    self.moving_left = False

    # Store decimal of ship's center
    self.center = float(self.rect.centerx)
    self.centery = float(self.rect.centery)

  def update(self):
    if self.moving_up and self.rect.top > self.screen_rect.top:
      self.centery -= self.speed
    if self.moving_right and self.rect.right < self.screen_rect.right:
      self.center += self.speed
    if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
      self.centery += self.speed
    if self.moving_left and self.rect.left > self.screen_rect.left:
      self.center -= self.speed

    self.rect.centerx = self.center
    self.rect.centery = self.centery

  def blitme(self):
    """Draw rocket at location"""
    self.screen.blit(self.image, self.rect)

  def listen_movement(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()

      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          self.moving_up = True
        elif event.key == pygame.K_RIGHT:
          self.moving_right = True
        elif event.key == pygame.K_DOWN:
          self.moving_down = True
        elif event.key == pygame.K_LEFT:
          self.moving_left = True

      elif event.type == pygame.KEYUP:
        if event.key == pygame.K_UP:
          self.moving_up = False
        elif event.key == pygame.K_RIGHT:
          self.moving_right = False
        elif event.key == pygame.K_DOWN:
          self.moving_down = False
        elif event.key == pygame.K_LEFT:
          self.moving_left = False

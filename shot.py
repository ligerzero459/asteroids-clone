import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt
    if self.velocity.x > 0:
      if self.position.x - self.radius >= SCREEN_WIDTH:
        self.position.x = self.position.x - (self.radius * 2) - SCREEN_WIDTH
    else:
      if self.position.x + self.radius <= 0:
        self.position.x = self.position.x + (self.radius * 2) + SCREEN_WIDTH

    if self.velocity.y > 0:
      if self.position.y - self.radius >= SCREEN_HEIGHT:
        self.position.y = self.position.y - (self.radius * 2) - SCREEN_HEIGHT
    else:
      if self.position.y + self.radius <= 0:
        self.position.y = self.position.y + (self.radius * 2) + SCREEN_HEIGHT

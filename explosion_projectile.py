import pygame

from circleshape import CircleShape
from constants import *

class ExplosionProjectile(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.start_time = pygame.time.get_ticks()
    self.duration = 500

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, 1)

  def update(self, dt):
    self.position += self.velocity * dt
    if pygame.time.get_ticks() - self.start_time >= self.duration:
      self.kill()

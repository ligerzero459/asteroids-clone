import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return

    log_event("asteroid_split")
    new_angle = random.uniform(20, 50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    new_asteroids = [
      Asteroid(self.position.x, self.position.y, new_radius),
      Asteroid(self.position.x, self.position.y, new_radius)
    ]
    new_asteroids[0].velocity = self.velocity.rotate(new_angle) * 1.2
    new_asteroids[1].velocity = self.velocity.rotate(-new_angle) * 1.2

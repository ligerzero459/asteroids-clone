import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from explosion import Explosion
from logger import log_event

class Asteroid(CircleShape):
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

  def split(self, field):
    self.kill()
    field.despawn()
    if self.radius <= ASTEROID_MIN_RADIUS:
      Explosion(self.position.x, self.position.y).explode()
      return

    log_event("asteroid_split")
    new_angle = random.uniform(20, 50)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    field.spawn(new_radius, self.position, (self.velocity.rotate(new_angle) * 1.2))
    field.spawn(new_radius, self.position, (self.velocity.rotate(-new_angle) * 1.2))

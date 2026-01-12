import pygame

from circleshape import CircleShape
from constants import *
from explosion_projectile import ExplosionProjectile
from logger import log_event

class Explosion():
  def __init__(self, x, y):
    self.position = pygame.Vector2(x, y)
    self.velocities = []

    initial_velocity = pygame.Vector2(1,0)
    for i in range(-7, 11):
      self.velocities.append(initial_velocity * ASTEROID_EXPLOSION_VELOCITY)
      initial_velocity = initial_velocity.rotate(20)

  def explode(self):
    log_event("asteroid_exploded")
    for explosion in self.velocities:
      projectile = ExplosionProjectile(self.position.x, self.position.y, ASTEROID_EXPLOSION_RADIUS)
      projectile.velocity = explosion

import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)

    self.rotation = 0
    self.shot_cooldown_timer = 0
    self.score = 0

  # in the Player class
  def triangle(self):
    forward = pygame.Vector2(0, 1).rotate(self.rotation)
    right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

  def update(self, dt):
    self.shot_cooldown_timer -= dt
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        self.rotate(-dt)
    if keys[pygame.K_d]:
        self.rotate(dt)
    if keys[pygame.K_w]:
        self.move(dt)
    if keys[pygame.K_s]:
        self.move(-dt)
    if keys[pygame.K_SPACE]:
       self.shoot()

  def rotate(self, dt):
    self.rotation += (PLAYER_TURN_SPEED * dt)

  def move(self, dt):
    unit_vector = pygame.Vector2(0, 1).rotate(self.rotation)
    self.position += unit_vector * PLAYER_SPEED * dt
    if unit_vector.x > 0:
      if self.position.x - self.radius >= SCREEN_WIDTH:
        self.position.x = self.position.x - (self.radius * 2) - SCREEN_WIDTH
    else:
      if self.position.x + self.radius <= 0:
        self.position.x = self.position.x + (self.radius * 2) + SCREEN_WIDTH

    if unit_vector.y > 0:
      if self.position.y - self.radius >= SCREEN_HEIGHT:
        self.position.y = self.position.y - (self.radius * 2) - SCREEN_HEIGHT
    else:
      if self.position.y + self.radius <= 0:
        self.position.y = self.position.y + (self.radius * 2) + SCREEN_HEIGHT

  def shoot(self):
    if self.shot_cooldown_timer > 0:
       return
    self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
    shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
    shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

  def update_score(self, asteroid):
    self.score += asteroid.radius * ASTEROID_SCORE_MULTIPLIER

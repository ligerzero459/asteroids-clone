import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from shot import Shot
from logger import log_state, log_event

def main():
  print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Game Initialization Start
  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  game_clock = pygame.time.Clock()
  dt = 0

  # Sprite Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  AsteroidField.containers = (updatable)
  Asteroid.containers = (updatable, drawable, asteroids)
  Player.containers = (updatable, drawable)
  Shot.containers = (updatable, drawable, shots)

  # Player Initialization
  AsteroidField()
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  # GAME LOOP
  while True:
    log_state()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return


    screen.fill("black")
    updatable.update(dt)
    for asteroid in asteroids:
      if asteroid.collides_with(player):
        log_event("player_hit")
        print("Game over!")
        sys.exit()

    for obj in drawable:
      obj.draw(screen)

    pygame.display.flip()

    dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
  main()

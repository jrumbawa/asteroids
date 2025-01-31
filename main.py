# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  clock = pygame.time.Clock()
  dt = 0
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable, drawable)
  asteroids = pygame.sprite.Group()
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable,)
  asteroid_field = AsteroidField()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)


  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        return
      
    updatable.update(dt)
      
    for asteroid in asteroids:
      if asteroid.collides_with(player):
          print("Game over!")
          sys.exit()

      for shot in shots:
          if asteroid.collides_with(shot):
              shot.kill()
              asteroid.split()
    screen.fill((0, 0, 0))
    for item in updatable:
      item.update(dt)
    for item in drawable:
      item.draw(screen)
    # player.update(dt)
    # player.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60) / 1000

if __name__ == "__main__":
  main()
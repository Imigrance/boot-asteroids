import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables)
    Shot.containers = (shots, updatables, drawables)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for updatable in updatables:
            updatable.update(dt)
        
        for drawable in drawables:
            drawable.draw(screen)

        for asteroid in asteroids:
            if asteroid.colliding(player):
                print("Game Over!")
                return
            for shot in shots:
                if asteroid.colliding(shot):
                    asteroid.split()
                    shot.kill()

        pygame.display.flip()
        
        tick = clock.tick(60)
        dt = tick/1000

if __name__ == "__main__":
    main()
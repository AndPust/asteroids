# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from Asteroid import Asteroid
from asteroidfield import AsteroidField
from Shot import Shot

def main():
    print("Starting asteroids!")
    print("Screen height:", SCREEN_HEIGHT)
    print("Screen width:", SCREEN_WIDTH)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    Shot.containers = (updatable, drawable, shots)

    while True:
        pygame.Surface.fill(screen, (255, 0, 255))
        for u in updatable:
            u.update(dt)
        for d in drawable:
            d.draw(screen)
        for a in asteroids:
            if a.collision(player):
                print("GAME OVER!")
                return
        for a in asteroids:
            for s in shots:
                if a.collision(s):
                    s.kill()
                    break
            else:
                continue
            a.split()
            break


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60)/1000
        # print(dt)


if __name__ == "__main__":
    main()

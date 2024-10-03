# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print("Screen height:", SCREEN_HEIGHT)
    print("Screen width:", SCREEN_WIDTH)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        pygame.Surface.fill(screen, (255, 0, 255))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

if __name__ == "__main__":
    main()

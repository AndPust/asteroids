import pygame

from CircleShape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt



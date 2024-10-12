import pygame
import random

from CircleShape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, r):
        super().__init__(x, y, r)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20.0, 50.0)
        radius = self.radius - ASTEROID_MIN_RADIUS

        a1 = Asteroid(self.position.x, self.position.y, radius)
        a2 = Asteroid(self.position.x, self.position.y, radius)
        a1.velocity = self.velocity.rotate(angle) * 1.2
        a2.velocity = self.velocity.rotate(-angle) * 1.2

    def draw(self, screen):
        pygame.draw.circle(screen, (0,0,0), self.position, self.radius, width=LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt


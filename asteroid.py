import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        old_radius = self.radius
        old_position = self.position
        old_velocity = self.velocity
        self.kill()
        if old_radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)

        v1 = old_velocity.rotate(angle) * 1.2
        v2 = old_velocity.rotate(-angle) * 1.2
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(old_position.x, old_position.y, new_radius)
        a2 = Asteroid(old_position.x, old_position.y, new_radius)
        a1.velocity = v1
        a2.velocity = v2

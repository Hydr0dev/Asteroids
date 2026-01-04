from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y ,radius)


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        first_ast_velocity = self.velocity.rotate(angle)
        second_ast_velocity = self.velocity.rotate(-angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_ast = Asteroid(self.position.x, self.position.y, new_radius)
        second_ast = Asteroid(self.position.x, self.position.y, new_radius)
        first_ast.velocity = first_ast_velocity * 1.2
        second_ast.velocity = second_ast_velocity


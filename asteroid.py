import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        #print("made asteroid")
        super().__init__(x, y, radius)

    def draw(self, screen):
        #print("DRAW", self.position, self.radius)
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        #print("UPDATE", self.position, self.velocity)
        self.position += (self.velocity * dt)
    
    def split(self):
        self.kill()
        #if this is the smallest asteroid, just remove it
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        #not smallest asteroid, so sparn two new ones:
        rand_angle = random.uniform(20.0, 50.0)

        new_velocity_1 = self.velocity.rotate(rand_angle)
        new_velocity_2 = self.velocity.rotate(-rand_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position

        new_asteroid_1 = Asteroid(x, y, new_radius)
        new_asteroid_2 = Asteroid(x, y, new_radius)

        new_asteroid_1.velocity = new_velocity_1 * 1.2
        new_asteroid_2.velocity = new_velocity_2 * 1.2


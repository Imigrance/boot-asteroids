from circleshape import *
from constants import ASTEROID_MIN_RADIUS
from random import uniform

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = uniform(20, 50)
        velo_1 = self.velocity.rotate(random_angle)
        velo_2 = self.velocity.rotate(-random_angle)
        radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid(self.position.x, self.position.y, radius).velocity = velo_1 * 1.2
        Asteroid(self.position.x, self.position.y, radius).velocity = velo_2 * 1.2
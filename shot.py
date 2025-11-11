from circleshape import CircleShape
from constants import SHOT_RADIUS, LINE_WIDTH
import pygame

class Shot(CircleShape):
    def __init__(self, x, y):
        #print("init containers:", getattr(self, "containers", None))
        super().__init__( x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(
            screen, 
            "white",
            (int(self.position.x), int(self.position.y)),
            SHOT_RADIUS
        )
        

    def update(self, dt):
        self.position += self.velocity * dt
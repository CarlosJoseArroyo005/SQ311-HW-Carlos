import pygame
from pygame.math import Vector2
import math

class Agent():

    def __init__(self) -> None:
        self.r = 100
        self.mass = 1
        self.force = Vector2(1, 0)

        self.position = Vector2(100, 100)
        self.velocity = Vector2(2, 3)
        self.acc = Vector2(0, 0)

    def update(self):   
        self.acc = self.force / self.mass
        self.velocity += self.acc
        self.position += self.velocity

        if self.position.x > 1280: self.position.x = 0
        if self.position.x < 0: self.position.x = 1280
        if self.position.y > 720: self.position.y = 0
        if self.position.y < 0: self.position.y = 720

    def draw(self, screen):
        animated_radius = self.r + math.sin(pygame.time.get_ticks() * 0.005) * 20
        pygame.draw.circle(screen, (255, 100, 200), (int(self.position.x), int(self.position.y)), int(animated_radius))

class SquareAgent():

    def __init__(self) -> None:
        self.size = 100
        self.position = Vector2(400, 300)
        self.velocity = Vector2(-2, 1)

    def update(self):
        self.position += self.velocity

        if self.position.x > 1280 - self.size or self.position.x < 0:
            self.velocity.x *= -1
        if self.position.y > 720 - self.size or self.position.y < 0:
            self.velocity.y *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, (100, 200, 255), (self.position.x, self.position.y, self.size, self.size), 2)

def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True

    agents = [Agent(), SquareAgent()]

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((30, 30, 30))

        for agent in agents:
            agent.update()
            agent.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
import pygame

class Pedaco():
    x = 0
    y = 0
    r = 20
    screen = 0

    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.r)
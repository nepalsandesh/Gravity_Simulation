import pygame

class Gravity:
    def __init__(self, left, top, screen, color):
        self.left = left
        self.top = top
        self.width = 50
        self.height = 50
        self.screen = screen
        self.color = color
    
    def draw(self):
        rect = pygame.Rect(self.left, self.top, self.width, self.height)
        pygame.draw.ellipse(self.screen, self.color, rect)
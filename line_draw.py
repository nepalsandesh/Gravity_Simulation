import pygame

class Curve:
    
    """ Takes input of Coordinates and having a draw function"""
    
    def __init__(self,coordinates, screen ,color, width):
        self.coordinates = coordinates
        self.screen = screen 
        self.color = color
        self.width = width
        
    def draw(self):
        if len(self.coordinates) >= 2:
            pygame.draw.lines(self.screen, self.color, False, self.coordinates, self.width)
        
        
        
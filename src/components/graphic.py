'''
Created on Nov 13, 2014

@author: Culoeperra
'''
from pygame.sprite import Sprite
import pygame
from pygame import surface

class Graphic(Sprite):
    def __init__(self, location = (0, 0), size = (0, 0), rect = None):
        self.rect = pygame.rect.Rect(location, size) if rect == None else rect
        self.image = surface.Surface(size, flags = pygame.SRCALPHA)
        
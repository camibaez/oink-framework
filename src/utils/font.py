#import pygame
#from pygame.font import SysFont
#
#pygame.font.init()
#
#class Font(Font):
#    '''
#    This class is an extension of the class SysFont.
#    This class has a new parameter wich is the color of the font.
#    '''
#    
#    def __init__(self, name, size, color = (0, 0, 0), bold=False, italic=False):
#        super(Font, self).__init__(name, size, bold, italic)
#        self.__color = color
#        
#    def render(self, text, trueType, color = None):
#        color = self.__color if (color == None) else (0, 0, 0)
#        super(Font, self).render(text, trueType, color)
#
#    def __get_color(self):
#        return self.__color
#    def __set_color(self, value):
#        self.__color = value
#    color = property(__get_color, __set_color)
#        
#    
#        
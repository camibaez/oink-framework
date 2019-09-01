'''
Created on Feb 20, 2014

@author: admin
'''
from oink.components.component import Component
import pygame
from pygame import surface, font

class TextField(Component):
    ALPHA_NUMERIC_FORM = 1
    ALPHABETIC_FORM = 2
    NUMERIC_FORM = 3
    
    
    def __init__(self, location = (0, 0), size = (0, 0), text = "", font = None):
        super(TextField, self).__init__(location, size)
        
        self.__letfToRight = False
        TextField.graphicInit(self, text, font)
        
        self.keyUp = self.__keyUpHnd
        self.keyDown = self.__keyDownHnd
    
    def graphicInit(self, text, font):
        self.__format = self.ALPHA_NUMERIC_FORM
        self.__backgroundColor = (255, 255, 255)
        self.__opaque = True
        self.__imagen = surface.Surface(self.getDimensions(), flags = pygame.SRCALPHA)
        self.__font = pygame.font.SysFont("arial", 20) if font == None else font
        self.__text = text
        self.__fontColor = (0, 0, 0)
        
        self.reDraw()
        
    def drawText(self):
        captionSurface = self.__font.render(self.text, True, self.fontColor)
        captionX = 2
        captionY = self.height /2 - captionSurface.get_rect().height/2
        self.blit(captionSurface, (captionX, captionY))
        
    
    def reDraw(self):
        self.reset()
        if self.opaque:
            self.fill(self.backgroundColor)
        
        self.drawText()

    
    #Events handling
    #Keys Handler
    def __keyUpHnd(self, evt = None):
        pass
        
    def __keyDownHnd(self, evt = None):
        if evt.key == pygame.K_BACKSPACE:
            self.text = self.text[0:-1]
        elif evt.key == pygame.K_SPACE:
            self.text += " "
        elif evt.key == pygame.K_LSHIFT:
            pass
        else:
            name = pygame.key.name(evt.key)
            if evt.mod == pygame.KMOD_LSHIFT:
                name = name.upper()
            self.text += name
    
    
    
    #property
    def get_letf_to_right(self):
        return self.__letfToRight
    def get_background_color(self):
        return self.__backgroundColor
    def get_opaque(self):
        return self.__opaque
    def get_imagen(self):
        return self.__imagen
    def get_font(self):
        return self.__font
    def get_text(self):
        return self.__text
    def get_font_color(self):
        return self.__fontColor
    def get_format(self):
        return self.__format


    def set_letf_to_right(self, value):
        self.__letfToRight = value

    def set_background_color(self, value):
        self.__backgroundColor = value
        self.reDraw()

    def set_opaque(self, value):
        self.__opaque = value
        self.reDraw()

    def set_imagen(self, value):
        self.__imagen = value
        self.reDraw()
        
    def set_font(self, value):
        self.__font = value
        self.reDraw()

    def set_text(self, value):
        self.__text = value
        self.reDraw()

    def set_font_color(self, value):
        self.__fontColor = value
        self.reDraw()
    
    def set_format(self, f):
        self.__format = f


    letfToRight = property(get_letf_to_right, set_letf_to_right)
    backgroundColor = property(get_background_color, set_background_color)
    opaque = property(get_opaque, set_opaque)
    imagen = property(get_imagen, set_imagen)
    font = property(get_font, set_font)
    text = property(get_text, set_text)
    fontColor = property(get_font_color, set_font_color)
    
    
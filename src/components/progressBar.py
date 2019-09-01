'''
Created on 12/10/2013

@author: Camilo Baez Aneiros
'''
import pygame
from oink.components.component import Component


class ProgressBar(Component):
    '''
    This class represents a progress bar.
    '''
    def __init__(self, location = (0, 0), size = (0, 0), orientation = 0):
        if orientation == 1:
            self.size = (size[1], size[0])
        
        super(ProgressBar, self).__init__(location, size)
        
        self.__minVal = 0
        self.__maxVal = 100
        self.__val = 100
        self.__orientation = orientation
        
        ProgressBar.graphicInit(self)
    
    def graphicInit(self):
        self.__backgroundColor = (0, 0, 0)
        self.__foregroundColor = (0, 255, 0)
        
        self.reDraw()
        
        
    def reDraw(self):
        self.reset()
        self.fill(self.backgroundColor)
        
        w, h = self.width, self.height
        filledPart = (self.maxVal - self.value) / float(self.maxVal - self.minVal)
        
        rect = None
        if self.__orientation == 1:
            offset = filledPart * h
            rect = pygame.Rect(0, offset, w, h)
        else:
            width =  filledPart * w
            rect =  pygame.Rect(0, 0, width, h)
        
        
        self.fill(self.foregroundColor, rect)
        
    #property
    def get_min_val(self):
        return self.__minVal
    def get_max_val(self):
        return self.__maxVal
    def get_background_color(self):
        return self.__backgroundColor
    def get_foreground_color(self):
        return self.__foregroundColor
    def get_val(self):
        return self.__val
    def get_orientation(self):
        return self.__orientation
    
    
    def set_min_val(self, value):
        self.__minVal = value
        self.reDraw()
    def set_max_val(self, value):
        self.__maxVal = value
        self.reDraw()
    def set_background_color(self, value):
        self.__backgroundColor = value
        self.reDraw()
    def set_foreground_color(self, value):
        self.__foregroundColor = value
        self.reDraw()
    def set_val(self, value):
        if self.minVal <= value <= self.maxVal:
            self.__val = value
            self.reDraw()
    def set_orientation(self, value):
        if value in [0, 1]:
            self.__orientation = value
    
    minVal = property(get_min_val, set_min_val)
    maxVal = property(get_max_val, set_max_val)
    backgroundColor = property(get_background_color, set_background_color)
    foregroundColor = property(get_foreground_color, set_foreground_color)
    value = property(get_val, set_val) 
    
    
    
        
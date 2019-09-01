'''
Created on 04/07/2014

@author: Kmilo
'''
from oink.components.component import Component
from pygame.sysfont import SysFont
from pygame import surface

class Label(Component):

    def __init__(self, location = (0, 0), size = (0, 0), caption = "", font = None, fontColor = (255, 255, 255), fixedToCaption = True):
        super(Label, self).__init__(location = location, size = size)
        
        self.__font = SysFont('arial', 20) if (font == None) else font
        self.fixedToCaption = fixedToCaption
        self.caption = caption
        self.fontColor = fontColor
        
        Label.graphicInit(self)
    
    def graphicInit(self):
        self.writeCaption()
    
    def writeCaption(self):
        if self.fixedToCaption:
            self.fixToCaption()
        else:
            self.reset()
            captionSurface = self.__font.render(self.__caption, True, self.fontColor)
            self.blit(captionSurface, (0, 0))
    
    def fixToCaption(self):    
        captionSurface = self.__font.render(self.caption, True, self.fontColor)
        self.width = captionSurface.get_size()[0]
        self.height = captionSurface.get_size()[1]
        
        self.reset()
        self.blit(captionSurface, (0, 0))

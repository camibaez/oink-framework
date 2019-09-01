import pygame
from pygame.font import SysFont
from oink.components.component import Component


class Button(Component):
    def __init__(self, size = (0, 0), caption = '', font = None):
        super(Button, self).__init__(size = size)
        
        Button.graphicInit(self, size, caption, font)
        
        
        #Default Mouse Handlers
        self.mouseEntered = self.__mouseEnteredHnd
        self.mouseExited = self.__mouseExitedHnd
        self.mouseButtonDown = self.__mouseButtonDownHnd
        self.mouseButtonUp = self.__mouseButtonUpHnd
        
        #Default Key Handlers
        self.keyUp = self.__keyUpHnd
    
    def graphicInit(self, size , caption , font):
        super(Button, self).graphicInit(self.getLocation(), size)
        
        self.__font = SysFont('arial', 20) if(font == None) else font
        self.__fontColor = (0, 0, 0)
        self.__caption = caption
        
        self.__pressedImage = pygame.Surface(size)
        self.__pressedImage.fill((150, 150, 150))
        
        self.__mouseOverImage = pygame.Surface(size)
        self.__mouseOverImage.fill((200, 200, 200))
        
        self.__normalImage = pygame.Surface(size)
        self.__normalImage.fill((100, 100, 100))
        
        self.reDraw()
        
    
    def reDraw(self):    
        self.reset()
        self.blit(self.__normalImage, (0, 0))
        self.writeCaption()
    
    #Mouse Handlers
    def __mouseEnteredHnd(self, evt = None):
        self.reset()
        self.blit(self.mouseOverImage, (0, 0))
        self.writeCaption()
    
    def __mouseExitedHnd(self, evt = None):
        self.reset()
        self.blit(self.normalImage, (0, 0))
        self.writeCaption()
    
    def __mouseButtonDownHnd(self, evt = None):
        self.reset()
        self.blit(self.pressedImage, (0, 0))
        self.writeCaption()
    
    def __mouseButtonUpHnd(self, evt = None):
        self.reset()
        self.blit(self.mouseOverImage, (0,0))
        self.writeCaption()
    
    #key handlers
    def __keyUpHnd(self, evt):
        self.actionPerformed()
    
    
    def writeCaption(self):
        captionSurface = self.__font.render(self.__caption, True, self.fontColor)
        captionX = self.get_rect().width / 2 - captionSurface.get_rect().width / 2
        captionY = self.get_rect().height / 2 - captionSurface.get_rect().height / 2
        self.blit(captionSurface, (captionX, captionY))
        
    
    #Property
    def __getFont(self): return self.__font
    def __setFont(self, font): 
        self.__font = font
        self.writeCaption()
    font = property(__getFont, __setFont)
    
    def __getCaption(self): return self.__caption
    def __setCaption(self, caption):
        self.__caption = caption
        self.writeCaption()
    caption = property(__getCaption, __setCaption)
    
    def __getFontColor(self): return self.__fontColor
    def __setFontColor(self, color): 
        self.__fontColor = color
        self.writeCaption()
    fontColor = property(__getFontColor, __setFontColor)
    
    def __getWidth(self):
        return super(Button, self).width
    def __setWidth(self, w):
        self.graphicInit((w, self.height), self.caption, self.font)
        self.reDraw()
    width = property(__getWidth, __setWidth)
    
    def __getHeight(self):
        return super(Button, self).height
    def __setHeight(self, h):
        self.graphicInit((self.width, h), self.caption, self.font)
        self.reDraw()
    height = property(__getHeight, __setHeight)
    
    def __getPressedImagen(self):
        return self.__pressedImage   
    def get_mouse_over_imagen(self):
        return self.__mouseOverImage
    def get_normal_imagen(self):
        return self.__normalImage
   
    def __setPressedImagen(self, img):
        self.__pressedImage = img
        self.blit(self.__pressedImage, (0, 0))
        self.writeCaption()
    def set_mouse_over_imagen(self, value):
        self.__mouseOverImage = value
        self.blit(self.__mouseOverImage, (0, 0))
        self.writeCaption()
    def set_normal_imagen(self, value):
        self.__normalImage = value
        self.blit(self.__normalImage, (0, 0))
        self.writeCaption()
    
    def setImages(self, imgs):
        self.normalImage = imgs[0]
        self.mouseOverImage = imgs[1]
        self.pressedImage = imgs[2]
        self.reDraw()
        
    pressedImage = property(__getPressedImagen, __setPressedImagen)
    mouseOverImage = property(get_mouse_over_imagen, set_mouse_over_imagen)
    normalImage = property(get_normal_imagen, set_normal_imagen)
        
        
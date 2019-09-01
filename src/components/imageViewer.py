

from oink.components.component import Component
from pygame import surface
import pygame

class ImageViewer(Component):

    def __init__(self, location = (0, 0), size = (0, 0), image = None):
        super(ImageViewer, self).__init__(location = location, size = size)
        self.__image = None
        self.image = image
        ImageViewer.graphicInit(self)
        
    def graphicInit(self):
        self.reDraw()
    
    def reDraw(self):
        if self.__image != None:
            self.blit(self.image, (0, 0))
    
    def getImage(self): return self.__image
    def setImage(self, image): 
        if type(image) == str:
            try:
                self.__image = pygame.image.load(image).convert_alpha()
            except:
                raise Exception("The path of the image it's not valid.")
        elif type(image) == surface.Surface:
            self.__image = image
        
        elif image == None:
            self.reset()
            self.__image = None
        else:
            raise Exception("The image attribute must be a string (representing the path of the file containing the image) or a surface.")
        self.reDraw()
        
        
    image = property(getImage, setImage)
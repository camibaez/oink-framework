'''
Created on 11/05/2013

@author: Camilo Baez Aneiros
@version: 1.0
@description: This class is related to the class menu. Represents
the element of a menu. Each element is linked to other menu (sub-menu).
'''

import pygame
from oink.button import Button
from oink.colors import WHITE, YELLOW
from oink.utils import font

class MenuElement(Button):
    '''
    Represents a element of a menu, linked to other sub-menu.
    '''

    def __init__(self, text = "", linkedMenu = None, font = None, unselectedColor = WHITE, selectedColor = YELLOW):
        '''
        MenuElemet(text[, linkedMenu = None, font = SysFont("arial", 50), color = White])
        text -> a string with the text of the menu.
        linkedMenu -> a Menu object that represents the menu to which the element is linked.
        font -> a pygame.font.Sysfont object
        '''
        if (not font): font = pygame.font.SysFont('arial', 50)
        super(MenuElement, self).__init__(font.size(text), text)
        
        self.__linkedMenu = linkedMenu
        self.font = font
        self.__selectedColor = selectedColor
        self.__unselectedColor = unselectedColor
        self.fontColor = unselectedColor
        
        self.__isSelected = False
        
        self.normalImagen = pygame.surface.Surface(font.size(text), flags = pygame.SRCALPHA)
        self.pressedImagen = pygame.surface.Surface(font.size(text), flags = pygame.SRCALPHA)
        self.mouseOverImagen = pygame.surface.Surface(font.size(text), flags = pygame.SRCALPHA)
        
        self.reset()
        self.blit(self.normalImagen, (0, 0))
        self.writeCaption()
        
        self.mouseEntered = self.__mouseEnteredHnd
        self.mouseExited = self.__mouseExitedHnd
        self.mouseButtonDown = self.__mouseButtonDownHnd
        self.mouseButtonUp = self.__mouseButtonUpHnd
    
    #Mouse Handlers
    def __mouseEnteredHnd(self, evt = None):
        self.fontColor = self.selectedColor
        self.isSelected = True
    
    def __mouseExitedHnd(self, evt = None):
        self.fontColor = self.unselectedColor
        self.isSelected = False
    
    def __mouseButtonDownHnd(self, evt = None):
        self.fontColor = self.selectedColor
        
    
    def __mouseButtonUpHnd(self, evt = None):
        self.fontColor = self.selectedColor
    
   
    def select(self, color = None, selected = True):
        if color:
            self.__color = color
        self.__isSelected = selected
        self.reset()
        self.blit(self.font.render(self.text, True, self.selectedColor), (0, 0))
        
    #properties
    def __getText(self): return self.caption
    def __setText(self, text): self.caption = text
    text = property(__getText, __setText)
    
    def __getLinkedMenu(self): return self.__linkedMenu
    def __setLinkedMenu(self, menu): self.__linkedMenu = menu
    linkedMenu = property(__getLinkedMenu, __setLinkedMenu)
    
    
    def __getIsSelected(self): return self.__isSelected
    def __setIsSelected(self, val): self.__isSelected = val
    isSelected = property(__getIsSelected, __setIsSelected)
    
    def __get_color(self): return self.__unselectedColor
    def __set_color(self, value): self.__uselectedColor = value
    unselectedColor = property(__get_color, __set_color)
    
    def __get_selectedColor(self): return self.__selectedColor
    def __set_selectedColor(self, color): self.__selectedColor = color
    selectedColor = property(__get_selectedColor, __set_selectedColor)    
    
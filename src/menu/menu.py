'''
Created on 09/05/2013

@author: Camilo Baez Aneiros
@version: 0.1

This module contains all the classes related to the menus.

The menu is a class that contains a dictionary that links a string -representing the 
text of each element of the current menu with a menu (actually a sub-menu).
This class works like a tree. The elements of the menus that don't have a sub-menu are 
linked to None (these are the leafs of the tree).
'''

import pygame.font
import oink.component as component
import oink.menu.menuModel as menuModel
import oink
from oink.utils import color

class MenuNotFoundException(Exception):
    pass

class Menu(component.Component):
    '''
    This class represents a menu. Each element of the menu is linked with other menu.
    '''
    def __init__(self, menuElements = None, pos = (0, 0), size = (0, 0), circularMenu = False, parent = None):
        '''
        Menu([menuElements = [], circularMenu = True]) -> Creates a menu containing the elements passed as parameters.
        - menuElemeznts -> a list of strings with the elements of the menu.
        ''' 
        super(Menu, self).__init__(pos, size)
        
        self.__parent = parent
        self.__menuModel = menuModel.DefaultMenuModel(self, menuElements)
        self.model.isCircular = circularMenu
        
        if len(self.model.menuElements):
            lineWidths = [e.width for e in self.menuModel.menuElements]
            self.width = max(lineWidths)
        
            lineHeights = [e.height for e in self.menuModel.menuElements]        
            self.height = sum(lineHeights)
    
        self.actionPerformed = self.__actionPerformedHnd
        self.mouseEntered = self.__mouseEnteredHnd
        self.mouseMoved = self.__mouseMovedHnd
        self.keyUp = self.__keyUpHnd
        self.keyDown = self.__keyDownHnd
        
    ###################### events handling ##############################
    #mouse handlers
    def __mouseEnteredHnd(self, evt = None):
        for ind, e in enumerate(self.model.menuElements):
            if e.isSelected:
                self.model.selectedElementIndex = ind
                break
    def __mouseMovedHnd(self, evt = None):
        self.__mouseEnteredHnd(evt)
    
    #key handler
    def __keyUpHnd(self, evt = None):
        self.selectPrevious()
    def __keyDownHnd(self, evt = None):
        self.selectNext()
    
    #action performed handler
    def __actionPerformedHnd(self, evt = None):
        self.model.selectedElement.actionPerformed()
    #################### events handling end ##############################
    
    
    def addElement(self, element):
        self.model.addElement(element)
        
        lineWidths = [e.width for e in self.model.menuElements]
        self.width = max(lineWidths)
        
        lineHeights = [e.height for e in self.model.menuElements]        
        self.height = sum(lineHeights)
           
    def getElement(self, index):
        return self.model.getElement(index) 
    def getMenu(self, elemText):
        for e in self.model.menuElements:
            if e.text == elemText:
                return e
        else:
            raise MenuNotFoundException("The element passed as parameter don't exist in this menu.")
    def removeElementFromText(self, elementText):
        for i in range(len(self.model.menuElements)):
            if self.model.menuElements[i].text == elementText:
                del self.model.menuElements[i]
                break
    def remove(self):
        oink.events.componentsList.remove(self)
        for e in self.model.menuElements:
            e.remove()
    
    def setVisible(self, bool):
        super(Menu, self).setVisible(bool)
        for e in self.model.menuElements:
            e.setVisible(bool)
    
    def __selectedElement(self):
        return self.model.selectedElement
    
    def changeSelected(self, dir):
        '''Changes the selected element.
        param dir -> the direction (+1 for the next element, -1 for the
                     previous element).
        '''
        i = self.model.selectedElementIndex
        if (i == 0) and (dir == -1):
            if self.model.isCircular:
                self.model.menuElements[i].select(selected = False)
                self.model.menuElements[-1].select()
                self.model.selectedElementIndex = len(self.model.menuElements) - 1
                return
            else:
                return
        if (i == len(self.model.menuElements) - 1) and (dir == 1):
            if self.model.isCircular:
                self.model.menuElements[i].select(selected = False)
                self.model.menuElements[0].select()
                self.model.selectedElementIndex = 0
                return
            else:
                return
        self.model.menuElements[i].select(selected = False)
        self.model.menuElements[i+dir].select()
        self.model.selectedElementIndex += dir
    
    def selectNext(self): self.changeSelected(1)
    def selectPrevious(self): self.changeSelected(-1)
    
    def selectElement(self, index):
        self.model.menuElements[index].select()
        self.model.selectedElementIndex = index
    
    def removeElement(self, index = -1):
        self.model.remove(index)
    
    #properties
    def __getIsCircular(self):
        return self.__isCircular
    def __setIsCircular(self, value):
        self.__isCircular = value
    isCircular = property(__getIsCircular, __setIsCircular)
    
    def __getLayout(self): return self.__layout
    def __setLayout(self, layout): 
        layout.parent = self
        self.__layout = layout
    layoutManager = property(__getLayout, __setLayout)
    
    def __getSelectedColor(self): return self.__selectedColor
    def __setSelectedColor(self, color): self.__selectedColor
    selectedColor = property(__getSelectedColor, __setSelectedColor)
    
    def __getUnselectedColor(self): return self.__unselectedColor
    def __setUnselectedColor(self, color): self.__unselectedColor = color
    unselectedColor = property(__getUnselectedColor, __setUnselectedColor)
    
    @property
    def parent(self): return self.__parent 
    @property
    def model(self): return self.__menuModel














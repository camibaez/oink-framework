#This module contains the class that represents the differents model
#for the differents kinds of Menus.
#The models are the classes designed for the duty of arrange the elements
#in a Menu.


from oink.layout import GridLayout
from oink.utils import color

class DefaultMenuModel(object):
    '''This is the default model for the Menus.
    It represents a vertical-like menu with one column and
    multiples rows'''
    
    def __init__(self, parent, menuElements = None):
        self.__parent = parent
        self.__layout = ColumnLayout(parent)
        self.__selectedElementIndex = -1
        
        if menuElements == None:
            self.__menuElements = []
        else:
            self.__menuElements = menuElements
            for e in menuElements:
                self.layout.addComponent(e)
        
        self.__isCircular = False
        
        if len(self.__menuElements):
            self.__menuElements[0].select(self.__selectedColor)
    
    def addElement(self, element): 
        self.menuElements.append(element)
        self.layout.addComponent(element)
    def getElment(self, pos): 
        return self.__menuElements[pos]
    def removeElement(self, index = -1):
        if len(self.menuElements) != 0:
            self.menuElements[index].remove()
            del self.menuElements[index]
        
    @property
    def layout(self): return self.__layout
    @property
    def menuElements(self): return self.__menuElements
    @property
    def selectedElement(self): return self.menuElements[self.selectedElementIndex]
    
    def __getSelectedElementIndex(self): 
        return self.__selectedElementIndex
    def __setSelectedElementIndex(self, index): 
        if index < len(self.menuElements):
            self.menuElements[index].select()
    selectedElementIndex = property(__getSelectedElementIndex, __setSelectedElementIndex)
    
    def __getIsCircular(self): return self.__isCircular
    def __setIsCircular(self, val): self.__isCircular = val
    isCircular = property(__getIsCircular, __setIsCircular)

class ColumnLayout(GridLayout):    
    def __init__(self, parent = None):
        super(ColumnLayout, self).__init__(parent = parent, colCount = 1, rowCount = 1)
    

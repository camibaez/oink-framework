"""
This module contains the layouts

-Layout (Base abstract class)

- GridLayout 
- BorderLayout
- FlowLayout
"""
from pygame import surface, rect
from oink.components.component import Component
from oink.events import componentsList

class Layout(object):    
    def __init__(self, parent = None, x = 0, y = 0, width = 0, height = 0):
        surface.Surface((1, 2))
        
        self.__parent = parent
        if parent:
            self.__width = self.parent.width
            self.__height = self.parent.height
            self.__x = self.parent.x
            self.__y = self.parent.y
        else:
            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
    
    def remove(self):
        pass
    
    def reArrangeComponents(self):
        pass
    
    def __getParent(self): return self.__parent
    def __setParent(self, p): 
        self.__parent = p
        self.width = p.width
        self.height = p.height
    parent = property(__getParent, __setParent)
    
    def __getWidth(self):
        return self.__width
    def __setWidth(self, val):
        if not self.__parent:
            self.__width = val
            self.reArrangeComponents()
    width = property(__getWidth, __setWidth)
    
    def __getHeight(self):
        return self.__height
    def __setHeight(self, val):
        if not self.parent:
            self.__height = val
            self.reArrangeComponents()
    height = property(__getHeight, __setHeight)
    
    def __getX(self):
        return self.__x
    def __setX(self, x):
        if not self.__parent:
            self.__x = x
            self.reArrangeComponents()
    x = property(__getX, __setX)
    
    def __getY(self):
        return self.__y
    def __setY(self, y):
        if not self.__parent:
            self.__y  = y
            self.reArrangeComponents()
    y = property(__getY, __setY)
    
    @property
    def rect(self): 
        return rect.Rect(self.x, self.y, self.width, self.height)
class AbsoluteLayout(object):
    def __init__(self, parent = None, x = 0, y = 0 , w = 0, h = 0):
        super(AbsoluteLayout, self).__init__(parent = parent, x = x, y = y, width = w, height = h)
        self.componentsList = []
    def addComponent(self, c, pos = None):
        self.componentsList.append(c)
        if pos != None:
            c.x, c.y =  self.x + pos[0], self.y + pos[1]
    
    def positionOfComponent(self, c):
        for comp in self.componentsList:
            if c == comp:
                return c.x - self.x, c.y - self.y
    
    def remove(self):
        for c in self.componentsList:
            c.remove()

class GridLayout(Layout):
    def __init__(self, parent = None, x = 0, y = 0, w = 0, h = 0, rowCount = 1, colCount = 1):
        super(GridLayout, self).__init__(parent, x, y, w, h)
        
        self.__hGap = 0
        self.__vGap = 0
        self.__table = [[None for j in range(colCount)] for i in range(rowCount)]
        self.__tempTable = [[None for j in range(colCount)] for i in range(rowCount)]
    
    def remove(self):
        for r in self.table:
            for c in r:
                if c != None:
                    c.remove()
    
    def addRow(self):
        self.__table.append([None for i in range(self.colCount)])
    def addColumn(self):
        for i in range(len(self.__table)):
            self.__table[i].append(None)
      
    def removeRow(self, index):
        if self.__table:
            if self.rowCount == 1:
                return
            for c in self.__table[index]:
                c.remove()
            del self.__table[index]
    def removeColumn(self, ind):
        if not self.__table:
            return
        if self.colCount == 1:
            return
        for r in self.__table:
            r[ind].remove()
            del r[ind]
    
    def getComponent(self, row, col):
        return self.__table[row][col]
    def setComponent(self, c, row, col):
        self.table[row][col] = c
        if c.layout == Component.FIX_TO_PARENT:
            c.width = self.width/self.colCount
            c.height = self.height/self.rowCount
        c.y = self.y + (self.height/self.rowCount + self.vGap) * row
        c.x = self.x + (self.width/self.colCount * col) + self.hGap
    
    def reArrangeComponents(self):
        for r in range(self.rowCount):
            for c in range(self.colCount):
                comp = self.table[r][c]
                if comp != None:
                    self.setComponent(comp, r, c)
           
    #Property
    def __getRowCount(self): return len(self.__table)
    def __setRowCount(self, count):
        if len(self.__table) <= count:
            self.__table = self.__table[:count]
        else:
            for i in range(count - len(self.__table)):
                self.addRow()
    rowCount = property(__getRowCount, __setRowCount)
    
    def __getColCount(self):
        if self.__table:
            return len(self.__table[0])
        else:
            return 0
    def __setColCount(self, count):
        if count <= self.__getColCount():
            for i in range(self.rowCount):
                del self.__table[i][count-1:]
        else:
            for i in range(count - self.colCount):
                self.addColumn()
    colCount = property(__getColCount, __setColCount)
    
    
    def getHGap(self): return self.__hGap
    def setHGap(self, g):
        self.__hGap = g
        self.reArrangeComponents()
    hGap = property(getHGap, setHGap)
    
    def getVGap(self): return self.__vGap
    def setVGap(self, g):
        self.__vGap = g
        self.reArrangeComponents()
    vGap = property(getVGap, setVGap)
    
    @property
    def tempTable(self): return self.__tempTable
    @property
    def table(self): return self.__table 

class BorderLayout(Layout):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4
    CENTER = 5
    
    def __init__(self, parent = None, x = 0, y = 0, w = 0, h = 0):
        super(BorderLayout, self).__init__(parent, x, y, w, h)
        self.__componentsDict = {self.NORTH : None, 
                                 self.SOUTH : None,
                                 self.WEST : None,
                                 self.EAST : None,
                                 self.CENTER : None}
    
    
    @property
    def componentsDict(self): return self.__componentsDict
    
    def __getNorth(self): return self.componentsDict[self.NORTH]
    def __setNorth(self, component): 
        widthPercent = 1
        xPos = self.x
        
        if self.east != None:
            widthPercent = 0.5
            
            if self.west != None:
                xPos += self.width * 0.25
                self.east.width = self.width * 0.25
                self.east.x = self.x + self.width - 0.25 * self.width 
                self.west.width = self.width * 0.25
            else:
                self.east.width = self.width * 0.5
                self.east.x = self.x + 0.5 * self.width
            
        elif self.west != None:
            xPos += self.width * 0.5
            widthPercent = 0.5
            self.west.width = self.width * 0.5
            
        heightPercent = 1
        if self.center != None:
            self.center.height = 0.5 * self.height
            if self.south != None:
                heightPercent = 0.5
                self.center.y = self.y + self.height * 0.5
            else:
                heightPercent = 0.25
                self.center.y = self.y + self.height * 0.25
                
        
        elif self.south != None:
            heightPercent = 0.5
            self.south.height = self.height * 0.5
        
        
        component.width = self.width * widthPercent
        component.height = self.height * heightPercent
        component.x = xPos
        component.y = self.y
        self.componentsDict[self.NORTH] = component
        
    north = property(__getNorth, __setNorth)
    
    def __getSouth(self): return self.componentsDict[self.SOUTH]
    def __setSouth(self, component):
        widthPercent = 1
        xPos = self.x
        
        if self.east != None:
            widthPercent -= 0.25
        if self.west != None:
            widthPercent -= 0.25
            xPos += self.width * .25
        
        heightPercent = 1
        if self.center != None:
            heightPercent -= 0.25
        
        component.width = self.width * widthPercent
        component.height = self.height * heightPercent
        component.x = xPos
        component.y = self.y + self.height - component.height
        self.componentsDict[self.SOUTH] = component
    
    south = property(__getSouth, __setSouth)
    
    def __getEast(self): return self.componentsDict[self.EAST]
    def __setEast(self, component):
        heightPercent = 1
        yPos = self.y
        
        if self.north != None:
            heightPercent -= 0.25
            yPos += self.height * 0.25
        if self.south != None:
            heightPercent -= 0.25

class FlowLayout(Layout):           
    RIGHT = 1
    LEFT = 2
    CENTER = 3
    
    def __init__(self, parent = None, xPos = 0, yPos = 0 , w = 0, h = 0, aligment = None):
        super(FlowLayout, self).__init__(parent = parent, x = xPos, y = yPos, width = w, height = h)
        self.__componentsList = []
        self.__alignment = FlowLayout.LEFT if aligment == None else aligment
        
        self.__hGap = 5
        self.__vGap = 5
        
    

    def _arrangeFromLeft(self, component):
        if self.componentsList == []:
            component.x = self.x
            if component.width > self.width:
                component.width = self.width
            component.y = self.y + self.verticalGap
            return
        
        
        
        
        lastComponent = self.componentsList[-1]
        xLast = lastComponent.x
        yLast = lastComponent.y
        wLast = lastComponent.width
        hLast = lastComponent.height
        
        nextPosX = xLast + wLast + self.horizontalGap
        if nextPosX + wLast <= self.x + self.width:
            component.x = nextPosX
            component.y = yLast
        else:
            component.x = self.x + self.horizontalGap
            component.y = yLast + self.verticalGap
            if component.width > self.width: 
                component.width = self.width
                

    def addComponent(self, component):
        arrangeDict = {self.LEFT : self._arrangeFromLeft}
        
        arrangeDict[self.alignment](component)
        
        self.__componentsList.append(component)

            
            
    def removeComponent(self, component):
        self.componentsList.remove(component)
        self.reArrangeComponents()
    
    def reArrangeComponents(self):
        temp = self.componentsList[:]
        self.__componentsList = []
        
        for c in temp:
            self.addComponent(c)
    
    @property
    def componentsList(self): return self.__componentsList
    
    def __getAlignment(self):
        return self.__alignment
    def __setAlignment(self, d):
        self.__alignment = d
        self.reArrangeComponents()
    alignment = property(__getAlignment, __setAlignment)
    
    def __getHorizontalGap(self):
        return self.__hGap
    def __setHorizontalGap(self, hgap):
        self.__hGap = hgap
        self.reArrangeComponents()
    horizontalGap = property(__getHorizontalGap, __setHorizontalGap)
    
    def __getVerticalGap(self):
        return self.__vGap
    def __setVerticalGap(self, g):
        self.__vGap = g
        self.reArrangeComponents()
    verticalGap = property(__getVerticalGap, __setVerticalGap)
        
        
        
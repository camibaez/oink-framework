"""This module contains a list of classes to represent objects in 2D.
The representation is of an object is made by a list of curves that are
delimited by tow points. The curves are parametrics (ParametricEquation).
For simplicity """



class Representation(object):
    """This class represents an 2-dimensional object
    in the plain by a group of curves delimited by points
    """
    
    def __init__(self, pointsList , functionsList, center = (0, 0)) :
        self.center = [center[0], center[1]]
        self.pointsList = pointsList
        self.functionsList = functionsList
    
    def getCenterX(self): return self.center[0]
    def setCenterX(self, x): self.center[0] = x
    centerX = property(getCenterX, setCenterX)
    
    def getCenterY(self): return self.center[1]
    def setCenterY(self, y): self.center[1] = y
    centerY = property(getCenterY, setCenterY)
    
    def getCenter(self): return self.__center
    def setCenter(self, c): self.__center = [c[0], c[1]]
    center = property(getCenter, setCenter)
    
    @property
    def pointsList(self): return self.__pointsList
    @property
    def funcsList(self): return self.__funcsList
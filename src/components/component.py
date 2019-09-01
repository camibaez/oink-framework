import pygame
import oink.events as events
from oink.components.graphic import Graphic

pygame.init()

class Component(object):
    '''Class component represents the base of all the visual elements.
    This is an abstract class, so it should not be instanciate as well.
    '''
    #These are the "constants" to represent the names
    #of the differents listeners
    ACTION_PERFORMED = 0
    KEY_UP = 1
    KEY_DOWN = 2
    MOUSE_ENTERED = 3
    MOUSE_EXITED = 4
    MOUSE_MOVED = 5
    MOUSE_BUTTON_UP = 6
    MOUSE_BUTTON_DOWN = 7
    
    #These constants represents the arrangement of the component
    WRAP_CONTENT = 8
    FIX_TO_PARENT = 9
    NORMAL = 10
    
    def __init__(self, location = (0, 0), size = (0, 0), rect = None): 
        
        Component.graphicInit(self, location, size, rect)
        
        self.__name = ''
        self.__isFocused = False
        self.__enabled = True
        self.__zOrder = 0
        
        self.invertY = 1
        
        #this are the dict that links a listener name (constant) with
        #a list of methods(listeners), that has been added during the inheritance.
        self.__actionListenerMap = {Component.ACTION_PERFORMED : []} 
        self.__keyListenerMap = {Component.KEY_UP : [], Component.KEY_DOWN : []}
        self.__mouseListenerMap = {Component.MOUSE_ENTERED : [], Component.MOUSE_EXITED : [], Component.MOUSE_MOVED : [],
                                    Component.MOUSE_BUTTON_UP : [], Component.MOUSE_BUTTON_DOWN : []}  
        
        events.componentsList.append(self)
    
    def graphicInit(self, location, size, rect = None):
        self.graphic = Graphic(location, size, rect)
        self.graphic.layout = Component.NORMAL
        
        self.__visible = True
        
        self.__rect = self.graphic.rect
        self.__x = self.__rect.left
        self.__y = self.__rect.top
        
        self.__width = self.__rect.width
        self.__height = self.__rect.height
    
    def reDraw(self):
        pass
    
    def setLocation(self, x, y):
        self.x = x
        self.y = y
    def getLocation(self):
        return self.x, self.y
    def getDimensions(self):
        return self.width, self.height
    def contains(self, x, y):
        return self.__rect.collidepoint(x, y)
    def reset(self):
        self.fill((0, 0, 0, 0))
    def remove(self):
        for i in range(len(events.componentsList)):
            if self == events.componentsList[i]:
                del events.componentsList[i]
                break
        
#        events.componentsList.remove(self)
    def setVisible(self, bool):
        self.__visible = bool
        self.isFocused = False
    
    
    #property
    def __getIsFocused(self): return self.__isFocused
    def __setIsFocused(self, v): self.__isFocused = v
    isFocused = property(__getIsFocused, __setIsFocused)
    
    def __getWidth(self): return self.rect.width
    def __setWidth(self, w): Component.graphicInit(self, (self.x, self.y), (w, self.height))
    width = property(__getWidth, __setWidth)
    
    def __getHeight(self): return self.rect.height
    def __setHeight(self, h): Component.graphicInit(self, (self.x, self.y), (self.width, h))
    height = property(__getHeight, __setHeight)
    
    def __getX(self): return self.rect.left
    def __setX(self, x): self.rect.left = x
    x = property(__getX, __setX)
    
    def __getY(self): return self.rect.top * self.invertY
    def __setY(self, y): self.rect.top = y
    y = property(__getY, __setY)
    
    def __getName(self): return self.__name
    def __setName(self, name): self.__name = name
    name = property(__getName, __setName)
    
    def __getEnabled(self): return self.__enabled
    def __setEnabled(self, bool): self.__enabled = bool
    enabled = property(__getEnabled, __setEnabled)
    
    def __getZOrder(self): return self.__zOrder
    def __setZOrder(self, v): self.__zOrder = v
    zOrder = property(__getZOrder, __setZOrder)
    
    def __getLayout(self): return self.__layout
    def __setLayout(self, l): self.__layout = l
    layout = property(__getLayout, __setLayout)
    
    
    def __getVisible(self): return self.__visible
    def __setVisible(self, v): self.__visible = v
    visible = property(__getVisible, __setVisible)

    @property
    def rect(self): return self.__rect
    
    ###########################
    # events handling properties
    ###########################
    def __listenerListExcecutor(self, evt, listenerList):
        '''This method is invoked on each listener to execute the list
        of listeners methods passing the evt as parameter to them.
        '''
        for listenerMethod in listenerList:
            listenerMethod(evt)
            
    def __getActionPerformed(self):
        def actionPerformedDecorator(evt = None):
            self.__listenerListExcecutor(evt, self.__actionListenerMap[self.ACTION_PERFORMED])
        return actionPerformedDecorator
    def __setActionPerformed(self, fnc):
        self.__actionListenerMap[self.ACTION_PERFORMED].append(fnc)
    actionPerformed = property(__getActionPerformed, __setActionPerformed)
    
    #mouse listener
    def __getMouseButtonUp(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__mouseListenerMap[self.MOUSE_BUTTON_UP])
        return decorator
    def __setMouseButtonUp(self, fnc):
        self.__mouseListenerMap[self.MOUSE_BUTTON_UP].append(fnc)
    mouseButtonUp = property(__getMouseButtonUp, __setMouseButtonUp)
    
    def __getMouseButtonDown(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__mouseListenerMap[self.MOUSE_BUTTON_DOWN])
        return decorator
    def __setMouseButtonDown(self, fnc):
        self.__mouseListenerMap[self.MOUSE_BUTTON_DOWN].append(fnc)
    mouseButtonDown = property(__getMouseButtonDown, __setMouseButtonDown)
    
    def __getMouseExited(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__mouseListenerMap[self.MOUSE_EXITED])
        return decorator
    def __setMouseExited(self, fnc):
        self.__mouseListenerMap[self.MOUSE_EXITED].append(fnc)
    mouseExited = property(__getMouseExited, __setMouseExited)
    
    def __getMouseEntered(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__mouseListenerMap[self.MOUSE_ENTERED])
        return decorator
    def __setMouseEntered(self, fnc):
        self.__mouseListenerMap[self.MOUSE_ENTERED].append(fnc)
    mouseEntered = property(__getMouseEntered, __setMouseEntered)
    
    def __getMouseMoved(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__mouseListenerMap[self.MOUSE_MOVED])
        return decorator
    def __setMouseMoved(self, fnc):
        self.__mouseListenerMap[self.MOUSE_MOVED].append(fnc)
    mouseMoved = property(__getMouseMoved, __setMouseMoved)
    
    #key listener
    def __getKeyUp(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__keyListenerMap[self.KEY_UP])
        return decorator
    def __setKeyUp(self, fnc):
        self.__keyListenerMap[self.KEY_UP].append(fnc)
    keyUp = property(__getKeyUp, __setKeyUp)
    
    def __getKeyDown(self):
        def decorator(evt = None):
            self.__listenerListExcecutor(evt, self.__keyListenerMap[self.KEY_DOWN])
        return decorator
    def __setKeyDown(self, fnc):
        self.__keyListenerMap[self.KEY_DOWN].append(fnc)
    keyDown = property(__getKeyDown, __setKeyDown)
    
    
    
    def __str__(self):
        return str(type(self))
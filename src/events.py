'''
Created on 23/08/2013

@author: Camilo Baez Aneiros
'''

import pygame


pygame.init()

class EventWrapper(object):
    def __init__(self, evt): 
        self.sender = None
        self.evt = evt
        self.type = evt.type
        
        if evt.type == pygame.MOUSEMOTION:
            self.pos = evt.pos
            self.rel = evt.rel
            self.buttons = evt.buttons
        if evt.type in [pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN]:
            self.pos = evt.pos
            self.button = evt.button
        if evt.type in [pygame.KEYUP, pygame.KEYDOWN]:
            self.key = evt.key
            self.mod = evt.mod
        if evt.type == pygame.KEYDOWN:
            self.unicode = unicode
        
        
        

class EventsHandler(object):
    @staticmethod
    def handleEvents(evts):
        for e in evts:
            e = EventWrapper(e)
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
                
            if e.type in [pygame.MOUSEMOTION, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN, pygame.KEYUP, pygame.KEYDOWN]:
                
                #Invoking first the listeners of the app
                dic = {pygame.MOUSEBUTTONDOWN: runningApp.actualState.mouseButtonDown,
                       pygame.KEYDOWN: runningApp.actualState.keyDown,
                       pygame.KEYUP: runningApp.actualState.keyUp,
                       pygame.MOUSEMOTION: runningApp.actualState.mouseMoved}
                if dic.has_key(e.type): 
                    dic[e.type](e)
                
                
                for c in componentsList:
                    if not c.visible: continue
                        
                    if e.type == pygame.MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()
                        if c.contains(*mousePos):
                            e.sender = c
                            c.mouseButtonDown(e)
                                
                    
                    if e.type == pygame.MOUSEMOTION:
                        mousePos = e.pos
                        lastPos = (e.pos[0] - e.rel[0], e.pos[1] - e.rel[1])
                        if c.contains(*mousePos):
                            
                            if not c.contains(*lastPos):
                                e.sender = c
                                c.mouseEntered(e)
                                
                            else:
                                e.sender = c
                                c.mouseMoved(e)
                                
                        else:
                            if c.contains(*lastPos):
                                e.sender = c
                                c.mouseExited(e)
                                
            
                    if e.type == pygame.MOUSEBUTTONUP:
                        mousePos = pygame.mouse.get_pos()
                        if c.contains(*mousePos):
                            
                            for i in componentsList:
                                i.isFocused = False
                            c.isFocused = True
                            e.sender = c
                            c.mouseButtonUp(e)
                            c.actionPerformed(e)
                            break
                            
                    
                    if e.type == pygame.KEYDOWN:
                        if c.isFocused:
                            e.sender = c
                            c.keyDown(e)
                    if e.type == pygame.KEYUP:
                        if c.isFocused:
                            e.sender = c
                            c.keyUp(e)
                                             
        
class ComponentsListHandler(list):
    def __init__(self, values = []):
        super(ComponentsListHandler, self).__init__(values)
        self.__maximZOrder = 0
    
    def append(self, e):
        if not e in self:
            for c in self:
                if c.rect.colliderect(e):
                    e.zOrder = c.zOrder + 1
                    self.__maximZOrder += 1
            super(ComponentsListHandler, self).append(e)
    @property
    def maximZOrder(self): return self.__maximZOrder

componentsList = ComponentsListHandler()
runningApp = None
'''
Created on 28/05/2014

@author: Kmilo
'''
import pygame
from oink import events
from pygame import rect

class App(object):
    runningApp = None
    def __init__(self, screenSize = (800, 600), depth = 16, clockTicks = 70, fillScreen = True, fullScreen = False, frame = True):
        pygame.init()
        
        self.fillScreen = fillScreen
        flags = 0
        if fullScreen : flags |= pygame.FULLSCREEN
        if not frame: flags |= pygame.NOFRAME 
        
        self.__screen = pygame.display.set_mode(screenSize, flags)
        self.__clock = pygame.time.Clock()
        self.__clockTicks = clockTicks
        
        App.runningApp = self
        events.runningApp = self
        
        self.screenColor = (0, 0, 0)
        self.screenSize = screenSize
        
        self.actualState = None
    def runApp(self):
        self.initializing()
        
        while True:
            events.EventsHandler.handleEvents(pygame.event.get())
            
            for e in events.componentsList:   
                if e.visible: 
                    self.screen.blit(e, (e.rect.x, e.rect.y))
            
            self.execute()
                    
            pygame.display.update() 
            self.clock.tick(self.clockTicks)
            
            if self.fillScreen:
                self.screen.fill(self.screenColor)
    
    
    def setFullScreen(self, v):
        pass
        
    def initializing(self): pass
    def resume(self): pass
    def pause(self): pass
    def close(self): pass
    
    def mouseButtonDown(self, evt = None): pass
    def mouseButtonUp(self, evt = None): pass
    def mouseMoved(self, evt = None): pass
    def keyDown(self, evt): pass
    
    def execute(self): pass
    @property
    def screen(self): return self.__screen
    @property
    def clock(self): return self.__clock
    
    def getClockTicks(self): return self.__clockTicks
    def setClockTicks(self, t): self.__clockTicks = t
    clockTicks = property(getClockTicks, setClockTicks)
    
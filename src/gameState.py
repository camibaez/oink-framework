'''
Created on 09/09/2014

@author: Kmilo
'''
from oink.state import State

class GameState(State):

    def __init__(self):
        super(GameState, self).__init__()
        self.layout = None
    
    def refresh(self):
        pass
    
    def mouseButtonDown(self, evt = None): pass
    def mouseButtonUp(self, evt = None): pass
    def mouseMoved(self, evt = None): pass
    
    def keyUp(self, evt = None): pass
    def keyDown(self, evt = None): pass
        
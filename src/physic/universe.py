'''
Created on 10/05/2014

@author: Kmilo
'''
import threading
from logic.threads import ParticleThread
from physic.vector import Vector2D


class Universe(object):
    class UniverseThread(threading.Thread):
        def __init__(self, universe):
            super(Universe.UniverseThread, self).__init__()
            self.__alive = True
            self.__universe = universe
            self.start()
        
        def run(self):
            while(self.__alive):
                pass
        
        def kill(self):
            self.__alive = False
    
    def __init__(self):
        self.size = (800, 600)
        self.particlesList = []
        self.threadsList = []
        
        
    def addParticle(self, p):
        self.particlesList.append(p)
        t = ParticleThread(p)
        t.start()
        self.threadsList.append(t)
    
    def checkCollisions(self, p = None):  
        particles = [p] if p != None else self.particlesList
            
        for p in particles:
            top = p.surf.rect.top
            left = p.surf.rect.left
            right = left + p.surf.rect.width
            bottom = top + p.surf.rect.height
            
            
            
            if top <= 0  or bottom >= self.size[1] : 
                p.vectVel.compY = p.vectVel.compY * -1
                p.vectVel = p.vectVel * 0.9
            if left <= 0 or right >= self.size[0]: 
                p.vectVel.compX = p.vectVel.compX * -1
                p.vectVel = p.vectVel * 0.9
                
    def calculateBounce(self, p1, p2):
        point = p1.intersectionPoint(p2)
        if point == False: return
        
        sign = point[1] - p1.posY
        
        #secant = utils.Math.LinearAlgebra.getSecant(point[0], p1.reprFunctionX(sign))
        
            
                
actualUniverse = None           
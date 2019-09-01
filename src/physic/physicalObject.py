'''
Created on 13/05/2014

@author: Kmilo
'''

from physic.particle import Particle
from physic.vector import Vector2D, Vector
from utils import mathUtils


class PhysicalObject(Particle):
    DENSITY = 1
    
    def __init__(self, pos, vel = None, m = 10):
        super(PhysicalObject, self).__init__(pos, vel)
        self.m = m

    
    def reprFunction(self):
        pass
    
    def arePointsOfObject(self, (x, y)):
        pass
    
    def pointsOfFunction(self, f):
        i = self.__funcsList.index(f)
        return self.pointsList[i], self.pointsList[i+1]
        
    
    


class Ellipse(PhysicalObject):
    def __init__(self, pos, vel = None, radix = 10, m = 10, a = 1, b = 1):
        super(Ellipse, self).__init__(pos = pos, vel = vel, m = m)
        self.radix = radix
        self.a = a
        self.b = b
    
    def containsPoint(self, pos):
        return mathUtils.LinearAlgebra.arePointsOfEllipse(self.a, self.b, pos[0], pos[1], self.radix)
        pass
    
    def intersectionPoint(self, o):
        x1 = (self.posX, self.posY)
        x2 = (o.posX, o.posY)
        r1, r2 = self.radix, o.radix
        
        v = Vector(x1, x2)
        
        if mathUtils.distaceBetweenPoints(x1, x2):
            return False
            
        
        v.magnitude = r1
        return (x1[0] + v[0], x1[1] + v[1])


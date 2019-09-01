'''
Created on 15/08/2014

@author: Kmilo
'''
import math
from physic.vector import Vector2D

class VectorialField(object):
    #The nature of the field
    ELECTRIC = 1
    GRAVITY = 2
    
    def function(self):
        pass

class ElectricField(VectorialField):
    def __init__(self, q0, center = None):
        self.nature = [VectorialField.ELECTRIC]
        self.q = q0
        self.center = center
        
    def function(self, pos, q, particle = None): 
        p = pos if particle == None else (particle.x, particle.y)
        q = q if particle == None else particle.q
        k = math.pow(10, -7)
        r = Vector2D(self.center, p)
        return k * (self.q * q)/ pow(r.magnitude, 2) * r.normalize()

        
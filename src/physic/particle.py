"""
last revision = 1/5/2014

TODO : Crear testUnits
ERRORS : No
"""
from oink.physic import G_ACCEL, PARTICLE_DENSITY
from oink.physic.vector import Vector2D



class Particle(object): 
    DENSITY = 0.01
    #The nature of the particle
    ELECTRIC = 1
    GRAVITY = 1
    
    def __init__(self, pos, vel = None, radius = 1):
        '''Particle(pos, [vel, radius])
        pos -> tuple, list - Represents the postion of the particle
        vel -> Vector2D - The original velocity represented by a two-dimensional vector (Vector2D([0, 0]) if null)
        radius -> number - The radius of the partcile (1 if null)
        '''
        
        self.__x, self.__y = pos[0], pos[1]
        self.__r = radius
        self.__vectVel = Vector2D([0, 0]) if vel == None else vel
        self.__vectorsList = []
        self.vectorialFields = []
        self.nature = []
             
    def move(self, t = 1):
        t = 1.0 / self.vectVel.magnitude
        
        res = self.vectRes
        ax = res.compX
        ay = res.compY

        
        vx = ax * t
        vy = ay * t
        
        self.x = self.x + self.vectVel.compX * t + ax * pow(t, 2) /2.0
        self.y = self.y + self.vectVel.compY * t + ay * pow(t, 2) /2.0
        
        self.__vectVel = self.__vectVel + Vector2D([vx, vy])
        
    def actualizeVect(self):
        self.__vectVel  = self.vectRes
    
    def addVectorialFied(self, field):
        field.center = self.particlePos
        self.vectorialFields.append(field)
    def actualizeFields(self):
        for f in self.vectorialFields:
            f.center = self.particlePos
    #Properties
      
    def getX(self): return self.__x
    def setX(self, pos): 
        self.__x = pos
        self.actualizeFields()
    x = property(getX, setX)
    
    def getY(self): return self.__y
    def setY(self, pos): 
        self.__y = pos
        self.actualizeFields()
    y = property(getY, setY)
    
    def getPos(self): return [self.__x, self.__y]
    particlePos = property(getPos)
    position = particlePos
    
    def getVectVel(self): return self.__vectVel
    def setVectVel(self, v): self.__vectVel = v 
    vectVel = property(getVectVel, setVectVel)
    
    @property
    def vectDir(self):
        return self.vectRes.normalize()
    
    @property
    def vectRes(self):
        v = Vector2D([0, 0])
        for vec in self.__vectorsList:
            v = v + vec
        return v
    
    @property
    def vectGravity(self): return self.__vectGrav
    
    def __getVelocity(self): return self.__vectVel.magnitude
    def __setVelocity(self, v): self.__vectVel.magnitude = v
    vel = property(__getVelocity, __setVelocity)
    
    def getRadius(self): return self.__r
    def setRadius(self, r): self.__r = r
    r = property(getRadius, setRadius)



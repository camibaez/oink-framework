"""
last revision 20/5/2014

TODO : 
    Create the exceptions of Vector (VECTOR EXEPTION)
    
"""

from math import sqrt, pow, radians, pi, degrees, asin, acos, cos, sin, atan, tan


class Vector(list):
    def __init__(self, components = None, p2 = None):
        """Vector([components|componentsCount])
        components : a list or a tuple containing the components
        componentsCount : a non-negative integer containing the number of components
        """
        super(Vector, self).__init__()
        if components != None:
            if isinstance(components, int):
                for i in range(components): self.append(0)
            elif p2 == None:
                for c in components: self.append(c)
            else:
                for c in [b - a for a, b in zip(components, p2)]: self.append(c) 
        else:
            self.append(0)
                
        self.label = ''
                
    def isNullVector(self):
        return not any(self)
    
    def normalize(self):
        m = self.magnitude
        for i in range(len(self)):
            self[i] = self[i] / m
            
        return self
    #Overriding methods
    def __add__(self, y):
        if isinstance(y, Vector) and len(self) == len(y):
            comps = [self[i] + y[i] for i in range(len(self))]
            return Vector(comps)
        else:
            raise TypeError("A vector can only be added to other vector with the same number of components.")
    def __mul__(self, y):
        if isinstance(y, Vector):
            if len(y) == len(self):
                return sum([self[i] * y[i] for i in range(len(self))])
            else:
                raise TypeError("A vector can only be added to other vector with the same number of components")
        elif isinstance(y, int) or isinstance(y, float):
            return Vector([i * y for i in self])
        else:
            raise TypeError("A vector can only be added to other vector with the same number of components")
    
    def __rmul__(self, y): return self.__mul__(y)
    def __neg__(self): return self * -1       
    def __sub__(self, y): return -y + self
        
    #Properties
    def __getComponentsCount(self): return len(self)
    def __setComponentsCount(self, value):
        if type(value) != int or value < 0:
            raise TypeError("The number of components must be a non-negative integer value")
        
        if value > len(self):
            self.extend([0 for i in range(value - len(self))])
        else:
            count  = len(self) - value
            for i in range(count):
                self.pop()  
    dimension = property(__getComponentsCount, __setComponentsCount)  
    
    def __setMagnitude(self, value):
        if not type(value) in [int, float] or value < 0:
            raise ValueError("The magnitude must be a value greater or equal than zero.")
        vect = self.__mul__(value / self.magnitude)
        for i in range(len(vect)):
            self[i] = vect[i]
    def __getMagnitude(self):
        x = sum([self[i]**2 for i in range(len(self))]) 
        return sqrt(x)
    magnitude = property(__getMagnitude, __setMagnitude)

class Vector2D(Vector):
    def __init__(self, components = None):
        components = [0, 0] if components == None else components
        
        if len(components) > 2: 
            raise ValueError("A 2D vector must have two components.")
        
        Vector.__init__(self, components)
        
    def getDirAngle(self, system = 'r'):
        """getDirAngle([system = 'r']) -> Return the angle of direction of the vector.
        @param system -> ['r'|'d'] determines the system of the angle (degrees(d) or radians(r))
        @raises -> TypeError
        """
        system = system.upper()
        if not system in ["R", "D"]: raise TypeError("The system must be radians(r) or degrees(d).")
        
        if self.isNullVector(): return None
        
        if self.compX == 0:
            if self.compY > 0: return 90 if system == 'D' else radians(90)
            else: return 270 if system == 'D' else radians(270)
        
        arcTan = atan(float(self.compY)/ self.compX) 
        dic = {1 : arcTan,
               2 : radians(180) + arcTan,
               3 : radians(180) + arcTan,
               4 : radians(360) + arcTan,
               None: None}
        
        if system == 'R':
            return dic[self.quadrant]
        else:
            return degrees(dic[self.quadrant])
        
    
    def setDirAngle(self, value, system = 'r'):
        system = system.upper()
        if not system in ['R', 'D']:
            raise TypeError("The value must be in degrees(d) or radians(r)")
        if system == 'D':
            value = radians(value)

        rad = radians   
        dic = {(0 <= value < rad(90)):  (cos(value), sin(value), '1'),
               (rad(90) <= value < rad(180)): (cos(value), sin(value), '2'),
               (rad(180) <= value < rad(270)) : (cos(value), sin(value), '3'),
               (rad(270) <= value < rad(360)) : (cos(value), sin(value), '4')}
        
        m = self.magnitude
        for k, j in dic.items():
            if k:
                self.compX = j[0] * m
                self.compY = j[1] * m
    
    
    #Overriding operator
    def __add__(self, y):
        v = super(Vector2D, self).__add__(y)
        return Vector2D(v)

    def __mul__(self, y):
        v = super(Vector2D, self).__mul__(y)
        return Vector2D(v)
    
    def __rmul__(self, y): return self.__mul__(y)
    def __neg__(self): return self * -1       
    def __sub__(self, y): return -y + self
    
    #Properties
    def __getCompX(self): return self[0]
    def __setCompX(self, value):
        if not type(value) in [int, float]:
            raise TypeError("A component must be a number.")
        else:
            self[0] = value
    compX = property(__getCompX, __setCompX)
    
    def __getCompY(self): return self[1]
    def __setCompY(self, value):
        if not type(value) in [int, float]:
            raise TypeError("A component must be a number.")
        else:
            self[1] = value
    compY = property(__getCompY, __setCompY)
    
    def __getQuadrant(self):
        if self.isNullVector():
            raise TypeError("Null vector don't have a quadrant.")
        dic = {1 : self.compX > 0 and self.compY >= 0,
               2 : self.compX <= 0 and self.compY > 0,
               3 : self.compX < 0 and self.compY <= 0,
               4 : self.compX >= 0 and self.compY < 0}
        for i in dic.keys():
            if dic[i]:
                return i
    quadrant = property(__getQuadrant)  

            
        

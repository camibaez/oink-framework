
class BodyPart(object):
    def __init__(self, father = None, name = None, surface = None):
        self.name = name
        self.father = father
        self.children = []
        self.linked = []
        self.surface = surface
        
    def addLinked(self, e):
        self.linked.append(e)
        e.linked.append(self)
    
    def addChild(self, c):
        self.children.append(c)
        c.father = self
        
    def addChildren(self, childsList):
        for c in childsList:
            self.addChild(c)
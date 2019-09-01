

class GMoveInterpreter(object):
    runingGMove = None
    
    def __init__(self):
        self.gMoveObjectsDict = {} 
    
    @staticmethod
    def getRunningGMoveInterp():
        if GMoveInterpreter.runingGMove == None:
            GMoveInterpreter.runingGMove = GMoveInterpreter()
        return GMoveInterpreter.runingGMove

    def loadMoveFile(self, path = None, moveFile = None):
        moveDict = {}
        f = file(path) if path != None else moveFile
        
        for line in f.readlines():
            movesList = line.split(' ')
            name = movesList.pop(0)
            
            for i in range(len(movesList)):
                if str.isdigit(movesList[i]):
                    movesList[i] = int(movesList[i])
            if movesList[-1][-1] == '\n':
                movesList[-1] = movesList[-1][:-1]
                    
            moveDict[name] = movesList
        f.close()
        return moveDict
    
    def addGMoveObject(self, obj, movesDict):
        self.gMoveObjectsDict[obj] = movesDict
        
            



import pygame

def loadImage(path):
    return pygame.image.load(path).convert_alpha()

def loadBodyMapO(filename):
    f = file(filename)
    
    bodyDict = {}
    tempDict = {}
    atualFacing = None
   
    for line in f.readlines():
        if line.isupper():
            if tempDict == {}:
                actualFacing = line.lower()
                continue
            else:
                bodyDict[actualFacing] = tempDict
                actualFacing = line
                tempDict = {}
                continue
                
        key = line[:line.find('(')]
        value = line[line.find('('):]
        tempDict[key] = value
    
    return bodyDict

def loadBodyMap(filename):
    f = file(filename)
    bodyDict = {}
    exec f.read()
    exec "bodyDict = rangeBoyMap"
    return bodyDict

def loadBodyPart(facing, partName, mapFileName, imageName):
    image = loadImage(imageName)
    section = loadBodyMap(mapFileName)[facing][partName]
    return image.subsurface(section)
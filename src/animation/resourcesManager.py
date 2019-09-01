import pygame
from oink.animation.bodyMap import loadBodyPart

BUTTONS_PATH = "res\\buttons\\"
MUSIC_PATH = "res\\music\\"
SOUNDS_PATH = "res\\sounds\\"
GOPA_PATH = "res\\gopa\\"
ANIMATIONS_PATH = "res\\animations\\"
    
#IMAGE SECTION
def loadImage(path):
    return pygame.image.load(path).convert_alpha()

def loadButtonImages(buttonNumber):
    dic = {0: ["foodN.png", "foodS.png", "foodP.png"], 
           1: ["playN.png", "playS.png", "playP.png"],
           2: ["showerN.png", "showerS.png", "showerP.png"],
           3: ["sleepN.png", "sleepS.png", "sleepP.png"],
           4: ["drinkN.png", "drinkS.png", "drinkP.png"],
           5: ["poopN.png", "poopS.png", "poopP.png"]
           }
    
    global BUTTONS_PATH
    return [loadImage(BUTTONS_PATH + dic[buttonNumber][i]) for i in range(3)]

def loadGopaBodyPart(facing, partName):
    return loadBodyPart(facing, partName, GOPA_PATH + 'bodymap.gmap', GOPA_PATH + 'bodymap.png')
    

    
#IMAGE SECTION END

#SOUND SECTION
def loadSound(name):
    return pygame.mixer.Sound(SOUNDS_PATH + name)


SOUNDS_DICT = {}
def loadSoundsDict():
    '''Loads a dictionary with the chanels of the most common sounds'''
    global SOUNDS_DICT
    SOUNDS_DICT['BUTTON_SELECTED'] = loadSound('buttonselected.wav')
    SOUNDS_DICT['BUTTON_SELECTED'].set_volume(0.1)
#SOUND SECTION END

#ANIMATION SECTION
def loadGMoveFile(name):
    return file(ANIMATIONS_PATH + name)

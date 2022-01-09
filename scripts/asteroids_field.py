from bge import logic, events
from scripts.asteroids_system import Asteroids

botLeftList = [ "AsteroideBotLeft0", "AsteroideBotLeft1",
                "AsteroideBotLeft2", "AsteroideBotLeft3",
                "AsteroideBotLeft4", "AsteroideBotLeft5"]

botRightList = ["AsteroideBotRight0", "AsteroideBotRight1",
                "AsteroideBotRight2", "AsteroideBotRight3",
                "AsteroideBotRight4", "AsteroideBotRight5"]

topLeftList = [ "AsteroideTopLeft0", "AsteroideTopLeft1",
                "AsteroideTopLeft2", "AsteroideTopLeft3",
                "AsteroideTopLeft4", "AsteroideTopLeft5"]

topRightList = ["AsteroideTopRight0", "AsteroideTopRight1",
                "AsteroideTopRight2", "AsteroideTopRight3",
                "AsteroideTopRight4", "AsteroideTopRight5"]
choice = 0


def SelectBotLeftAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return botLeftList[choice-1]

def SelectTopLeftAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return topLeftList[choice-1]

def SelectBotRightAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return botRightList[choice-1]

def SelectTopRightAsteroid():
    global choice
    if choice > 5:
        choice = 0
    
    choice += 1

    return topRightList[choice-1]

def Start(cont):
    own = cont.owner
    own["invoked4"] = True
    asteroid = Asteroids(own, 3)

def Update(cont):
    asteroid = cont.owner
    scene = logic.getCurrentScene()
    if asteroid["invoked4"]==True:
        botLeftAst  = SelectBotLeftAsteroid()
        topRightAst = SelectTopRightAsteroid()
        topLeftAst  = SelectTopLeftAsteroid()
        botRightAst = SelectBotRightAsteroid()
        print(topRightAst)
        asteroid["asteroid1"] = scene.addObject(botLeftAst, "BottomLeft")
        asteroid["asteroid2"] = scene.addObject(botRightAst, "BottomRight")
        asteroid["asteroid3"] = scene.addObject(topRightAst, "TopRight")
        asteroid["asteroid4"] = scene.addObject(topLeftAst, "TopLeft")
        asteroid["invoked4"]=False

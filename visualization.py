import graphics

window = graphics.GraphWin()
oval = graphics.GraphicsObject({})

def mainLoop():
    oval.draw(window)

while True:
    mainLoop()
from pygame_functions import *

screenSize(1024,768)
setAutoUpdate(False)
link = makeSprite("LinkSimple.png", 14)
showSprite(link)
Link_X = 500
Link_Y = 350
moveSprite(link, Link_X, Link_Y)
nextFrame = clock()
frame = 0
orientation = 0
Link_Speed = 6

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 100
        pause(20)
        
        if keyPressed("down"):
            changeSpriteImage(link, 0*2 + frame)
            orientation =0
            Link_Y = Link_Y + Link_Speed
            
        if keyPressed("up"):
            changeSpriteImage(link, 1*2 + frame)
            orientation =1
            Link_Y = Link_Y - Link_Speed
            
        if keyPressed("right"):
            changeSpriteImage(link, 2*2 + frame)
            orientation =2
            Link_X = Link_X + Link_Speed
            
        if keyPressed("left"):
            changeSpriteImage(link, 3*2 + frame)
            orientation =3
            Link_X = Link_X - Link_Speed
            
        if keyPressed("space"):
            changeSpriteImage(link, orientation + 8)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        moveSprite(link, Link_X, Link_Y)
        updateDisplay()


endWait()
from pygame_functions import *

screenSize(1024,768)

link = makeSprite("LinkSimple.png", 14)
showSprite(link)
moveSprite(link, 500, 350)

nextFrame = clock()
frame = 0
orientation = 0

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 100
        pause(20)
        
        if keyPressed("down"):
            changeSpriteImage(link, 0*2 + frame)
            orientation =0
        if keyPressed("up"):
            changeSpriteImage(link, 1*2 + frame)
            orientation =1
        if keyPressed("right"):
            changeSpriteImage(link, 2*2 + frame)
            orientation =2
        if keyPressed("left"):
            changeSpriteImage(link, 3*2 + frame)
            orientation =3
        if keyPressed("space"):
            changeSpriteImage(link, orientation + 8)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)

endWait()
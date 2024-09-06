from pygame_functions3 import *
import random
gUp = True
gDown = False
gLeft = False
gRight = False
def moveGororia():
    global randFrame, randDirection, frameCount, gUp, gDown, gLeft, gRight
    frameNum = 1
    spriteSpeed = 6

    randNumbers()
    if frameCount == randFrame:
        
        if randDirection == 0:
            gUp = True
            gDown = False
            gLeft = False
            gLight = False
        elif randDirection == 1:
            gUp = False
            gDown = True
            gLeft = False
            gRight = False
        elif randDirection == 2:
            gUp = False
            gDown = False
            gLeft = True
            gRight = False
        else:
            gUp = False
            gDown = False
            gLeft = False
            gRight = True
    if gororia.rect.x <= 10:
        gUp = False
        gDown = False
        gLeft = False
        gRight = True
    if gororia.rect.x >= 1014:
        gUp = False
        gDown = False
        gLeft = True
        gRight = False
    if gororia.rect.y <= 10:
        gUp = False
        gDown = True
        gLeft = False
        gRight = False
    if gororia.rect.y >= 758:
        gUp = True
        gDown = False
        gLeft = False
        gRight = False
    if gUp == True:
        moveSprite(gororia, gororia.rect.x, gororia.rect.y - spriteSpeed)
        if frame%50 == 0:
            frameNum = 2
        else:
            frameNum = 6
    if gDown == True:
        moveSprite(gororia, gororia.rect.x, gororia.rect.y + spriteSpeed)
        if frame%50 == 0:
            frameNum = 0
        else:
            frameNum = 4
    if gLeft == True:
        moveSprite(gororia, gororia.rect.x - spriteSpeed, gororia.rect.y)
        if frame%50 == 0:
            frameNum = 1
        else:
            frameNum = 5
    if gRight == True:
        moveSprite(gororia, gororia.rect.x + spriteSpeed, gororia.rect.y)
        if frame%50 == 0:
            frameNum = 3
        else:
            frameNum = 7
    changeSpriteImage(gororia, frameNum)
randFrame = 0
randDirection = 0
frameCount = 0
def randNumbers():
    global randFrame, randDirection
    randFrame = random.randint(10, 30)
    randDirection = random.randint(0, 3)

screenSize(1024,768)
setAutoUpdate(False)
link = Player()
octorok = makeSprite("Octorok.png", 4, 2)
gororia = makeSprite("gororia.png", 4, 2)
showSprite(gororia)
showSprite(link)
showSprite(octorok)
moveSprite(octorok, 200, 200)
moveSprite(gororia, 300, 200)
nextFrame = clock()
frame = 0
orientation = 0
Link_Speed = 6

while True:
    if clock() >nextFrame:
        frame= (frame + 1)%2
        nextFrame += 100
        pause(20)
        frameCount = frameCount + frame
        if frameCount >= 30:
            frameCount = 0
        if keyPressed("down"):
            changeSpriteImage(link, 0*2 + frame)
            link.orientation =0
            link.move(frame)
        if keyPressed("up"):
            changeSpriteImage(link, 1*2 + frame)
            link.orientation =1
            link.move(frame)
        if keyPressed("right"):
            changeSpriteImage(link, 2*2 + frame)
            link.orientation =2
            link.move(frame)
        if keyPressed("left"):
            changeSpriteImage(link, 3*2 + frame)
            link.orientation =3
            link.move(frame)
        if keyPressed("space"):
            changeSpriteImage(link, link.orientation + 8)
        if keyPressed("h"):
            changeSpriteImage(link, frame+12)
        moveGororia()
        
        updateDisplay()
        


endWait()
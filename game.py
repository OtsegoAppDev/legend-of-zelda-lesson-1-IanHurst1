from pygame_functions3 import *
import random
from gameClasses import *


def linkStuff():
    link.deathAnimation()
    for mon in monList:
        link.hitTest(mon)
        sword.hitSomething(mon, link)


def monsterStuff():
    for mon in monList:
        mon.direction(frameCount)
        mon.move(frame)
        if mon.dead == True:
            monList.remove(mon)






def timers():
    link.timer = link.timer + 1
    





frameCount = 0


screenSize(1024,768)
setAutoUpdate(False)
link = Player()
gororia = gororia()
sword = Sword(link)

"gororiaA = gororia()"
"'gororia' object is not callable"
"this only happens when a second gororia is being created"

octorok = octorok()
showSprite(link)
nextFrame = clock()
frame = 0
orientation = 0
Link_Speed = 6



monList = [gororia, octorok]

for mon in monList:
    showSprite(mon)



while True:
    if clock() >nextFrame:
        timers()
        frame= (frame + 1)%2
        nextFrame += 100
        pause(20)

        frameCount = frameCount + frame
        if frameCount >= 30:
            frameCount = 0
        if keyPressed("l"):
            link.unDie()
            print(link.hp)
            print(link.dead)
        if link.dead == False:
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
                sword.swing()
            if not keyPressed("space"):
                hideSprite(sword)
            if keyPressed("h"):
                changeSpriteImage(link, frame+12)
        else:
            hideSprite(sword)
        #if frameCount == gororia.randFrame:
        monsterStuff()
        linkStuff()
        updateDisplay()
        #print(link.timer)


endWait()
from pygame_functions3 import *
import random
from gameClasses import *


def linkStuff():
    global PickUpList
    link.deathAnimation()
    for Heart in HeartConList:
        if Heart.collected == True:
            HeartConList.remove(Heart)
        Heart.spawn()
        link.collectedHeart(Heart, link)
    for PickUp in PickUpList:
        link.pickedUpHeart(PickUp)
        if PickUp.collected == True:
            PickUpList.remove(PickUp)
    
    for life in lifeList:
        life.removeHeart(link)
        life.addHeart(link)
    for mon in monList:
        link.hitTest(mon)
        sword.hitSomething(mon, link)


def monsterStuff():
    for mon in monList:
        mon.direction(frameCount)
        mon.move(frame)
        mon.noGoOut()
        if mon.dead == True:
            monList.remove(mon)
            dropHeart(mon)
            
            
def dropHeart(mon):
    if random.randint(1, 5) == 5:
        newSprite = heartPickUp()
        newSprite.Spawn(mon)
        showSprite(newSprite)
        PickUpList.append(newSprite)


def spawnGororia():
    newSprite = gororia()
    newSprite.pickDirection()
    showSprite(newSprite)
    monList.append(newSprite)
    
def spawnOctorok():
    newSprite = octorok()
    showSprite(newSprite)
    monList.append(newSprite)


def timers():
    link.timer = link.timer + 1
    





frameCount = 0


screenSize(1024,768)
setAutoUpdate(False)
link = Player()
gororia1 = gororia()



sword = Sword(link)

life1 = heart()

life2 = heart()
life2.number = 1
life3 = heart()
life3.number = 2
life4 = heart()
life4.number = 3
life5 = heart()
life5.number = 4
life6 = heart()
life6.number = 5
life7 = heart()
life7.number = 6
life8 = heart()
life8.number = 7
life9 = heart()
life9.number = 8
life10 = heart()
life10.number = 9

heartCon1 = heartContainer()



lifeList = [life1, life2, life3, life4, life5, life6, life7, life8, life9, life10]

HeartConList = [heartCon1]

for life in lifeList:
    life.moveHeart()
    showSprite(life)





octorok1 = octorok()
showSprite(link)
nextFrame = clock()
frame = 0
orientation = 0
Link_Speed = 8



monList = [gororia1, octorok1]

for mon in monList:
    showSprite(mon)
    
PickUpList = []


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
        if keyPressed("m"):
            spawnGororia()
        if keyPressed("o"):
            spawnOctorok()
            
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
        monsterStuff()
        linkStuff()
        updateDisplay()


endWait()
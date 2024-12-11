from pygame_functions import *
from sprites import *
import random








def linkStuff():
    link.deathAnimation()
    if link.canGetHit == False:
        link.hitTimer += 1
        if link.hitTimer == link.invincibilityTime:
            link.canGetHit = True
            link.hitTimer = 0
    for wall in currentScene.Wall_Tiles:
            link.HitWall(wall, frame)
            
    for water in currentScene.Water_Tiles:
        link.HitWall(water, frame)

    for item in currentScene.Items:
        showSprite(item)
        link.pickUpItem(item, link)
        if item.collected == True:
            currentScene.Items.remove(item)
    for p in currentScene.Projectiles:
        if p.name == "monster":
            link.hitTest(p, "Projectile")



"""
ITEMS
"""



def dropItem(mon):
    itemDrop = dropChart(link.kills)                          
    if itemDrop == 0:
        aRupee = Rupee()
        if random.randint(1, 10) < 10:
            aRupee.spawn("red", mon)
        else:
            aRupee.spawn("blue", mon)
        currentScene.Items.append(aRupee)
        showSprite(aRupee)
    elif itemDrop == 1:
        aHeart = heartPickUp()
        aHeart.spawn("none", mon)
        currentScene.Items.append(aHeart)
        showSprite(aHeart)
    elif itemDrop == 2:
        aFairy = Fairy()
        aFairy.spawn("none", mon)
        currentScene.Items.append(aFairy)
    elif itemDrop == 3:
        pass
        #To Do Program Bomb
    elif itemDrop == 4:
        pass
        #To Do Program Timer
    elif itemDrop ==5:
        aBRupee = Rupee()
        aBRupee.spawn("blue", mon)
        currentScene.Items.append(aBRupee)
        showSprite(aBRupee)





"""
PROJECTILES
"""

       
def projectiles():
    for p in currentScene.Projectiles:
        p.move(frame)

canThrow = True
swordCooldownTime = 0
def swordThrowCooldown():
    global canThrow, swordCooldownTime
    if canThrow == False:
        if swordCooldownTime > 10:
            canThrow = True
        else:
            swordCooldownTime = swordCooldownTime + 1

def throwSword():
    global canThrow, swordCooldownTime
    if canThrow == True:
        if link.hp == link.startHp:
            aSwordProjectile = SwordProjectile()
            aSwordProjectile.orientation = link.orientation
            aSwordProjectile.rect.x = link.rect.x
            aSwordProjectile.rect.y = link.rect.y
            currentScene.Projectiles.append(aSwordProjectile)
            showSprite(aSwordProjectile)
            hideSprite(smallBlackBox)
            showSprite(smallBlackBox)
            if link.infHp == False:
                canThrow = False
                swordCooldownTime = 0
            

def linkProjectiles():
    for p in currentScene.Projectiles:
        if p.name == "link":
            p.goingOfEdgeFix()
            for mon in currentScene.Enemies:
                if p.rect.colliderect(mon.rect):
                    p.rect.y = 1
                    killSprite(p)
                    mon.hit(p, link)
                    if mon.hp == 0:
                        link.kills += 1
                        dropItem(mon)
                    
 
 
 
 
        
    for life in lifeList:
        life.removeHeart(link)
        life.addHeart(link)
    for mon in currentScene.Enemies:
        link.hitTest(mon, "NA")
        
def TektiteJump():
    for mon in currentScene.Enemies:
        if mon.type == "not normal":
            mon.Jump()

def monsterStuff():
    for mon in currentScene.Enemies:
        for wall in currentScene.Wall_Tiles:
            mon.HitWall(wall, frame)
        if mon.type == "normal":
            mon.direction(frameCount)
            mon.move(frame)
            mon.noGoOut()
        if mon.dead == True:
            currentScene.Enemies.remove(mon)
        if mon.shoots == "yes":
            mon.shoot(frame, currentScene)
        


def spawnGororia():
    newSprite = gororia()
    newSprite.pickDirection()
    showSprite(newSprite)
    currentScene.Enemies.append(newSprite)
    
def spawnOctorok():
    newSprite = octorok()
    showSprite(newSprite)
    currentScene.Enemies.append(newSprite)

def spawnTektite():
    newSprite = Tektite()
    showSprite(newSprite)
    currentScene.Enemies.append(newSprite)

def spawnTestDummy():
    newSprite = TestDummy()
    newSprite.rect.x = link.rect.x + 32
    newSprite.rect.y = link.rect.y
    showSprite(newSprite)
    currentScene.Enemies.append(newSprite)


def timers():
    link.timer = link.timer + 1
    
def reloadHud():
    hideSprite(blackBox)
    showSprite(blackBox)
    hideSprite(rupeeDisplay)
    showSprite(rupeeDisplay)
    hideSprite(DisplayRupee)
    showSprite(DisplayRupee)
    hideSprite(lifeLabel)
    showSprite(lifeLabel)
    for life in lifeList:
        hideSprite(life)
        life.removeHeart(link)
        life.addHeart(link)

frameCount = 0


screen = screenSize(1024,768)
setAutoUpdate(False)



link = Player()



scene1 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map.txt", 6, 8)
scene2 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map2.txt", 6, 8)
scene3 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map3.txt", 6, 8)
scene4 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map4.txt", 6, 8)
scene5 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map5.txt", 6, 8)
scene6 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map6.txt", 6, 8)
scene7 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map7.txt", 6, 8)
scene8 = Scene(screen, link, "ZeldaMapTilesBrown.png", "map8.txt", 6, 8)
scene9 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map9.txt", 6, 8)
scene10 = Scene(screen, link, "ZeldaMapTilesBrown.png", "map10.txt", 6, 8)
scene11 = Scene(screen, link, "ZeldaMapTilesGreen.png", "map11.txt", 6, 8)
scene12 = Scene(screen, link, "ZeldaMapTilesBrown.png", "map12.txt", 6, 8)



scenes = [[scene3, scene2], [scene4, scene1], [scene5, scene6], [scene7, scene8], [scene9, scene10], [scene11, scene12]]
currentScene = scene1

"""
3 4
2 1



"""
showBackground(currentScene)


showSprite(link)
blackBox = newLabel("..................................................................................", 90 , "Helvetica Neue", "black", 0, 0, "black")
showSprite(blackBox)

smallBlackBox = newLabel("................................................................................................................................................................................................................................................", 25 , "Helvetica Neue", "black", 0, 65, "black")



rupeeDisplay = newLabel("0", 50, "Helvetica Neue", "white", 130, 30, "black")
DisplayRupee = Rupee()
currentScene.Items.append(DisplayRupee)
DisplayRupee.display = True
DisplayRupee.SpawnDisplay(100,30)
showSprite(rupeeDisplay)
showSprite(DisplayRupee)

lifeLabel = newLabel("-LIFE-", 60, "Helvetica Neue", "red", 810, 10, "black")
showSprite(lifeLabel)

sword = Sword(link)



"Row 1 hearts"
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

"Row 2 hearts"
life11 = heart()
life11.number = 10
life11.row = 2
life12 = heart()
life12.number = 11
life12.row = 2
life13 = heart()
life13.number = 12
life13.row = 2
life14 = heart()
life14.number = 13
life14.row = 2
life15 = heart()
life15.number = 14
life15.row = 2
life16 = heart()
life16.number = 15
life16.row = 2
life17 = heart()
life17.number = 16
life17.row = 2
life18 = heart()
life18.number = 17
life18.row = 2
life19 = heart()
life19.number = 18
life19.row = 2
life20 = heart()
life20.number = 19
life20.row = 2





lifeList = [life1, life2, life3, life4, life5, life6, life7, life8, life9, life10, life11, life12, life13, life14, life15, life16, life17, life18, life19, life20]



for life in lifeList:
    life.moveHeart()
    showSprite(life)
timer = 10

def reloadItems():
    for item in currentScene.Items:
        hideSprite(item)
        showSprite(item)
    for thing in currentScene.Projectiles:
        hideSprite(thing)
        showSprite(thing)


nextFrame = clock()
frame = 0
orientation = 0
Link_Speed = 8

swordFix = True
def makeSwordWork(sword, scene):
    global swordFix
    if swordFix == True:
        swordFix = False
        for mon in currentScene.Enemies:
            mon.canGetHit = True
    
# i is the list number
# j is the element number
i = 1
j = 1


while True:
    rupeeDisplay.update(str(link.rupees), "white", "black")
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
        
        if keyPressed("m"):
            itemDrop = dropChart(link.kills)        
            if itemDrop == 0:
                aRupee = Rupee()
                if random.randint(1, 10) < 10:
                    aRupee.spawn("red", link)
                else:
                    aRupee.spawn("blue", link)
                currentScene.Items.append(aRupee)
                showSprite(aRupee)
            elif itemDrop == 1:
                aHeart = heartPickUp()
                aHeart.spawn("none", link)
                currentScene.Items.append(aHeart)
                showSprite(aHeart)
            elif itemDrop == 2:
                aFairy = Fairy()
                aFairy.spawn("none", link)
                currentScene.Items.append(aFairy)
        
        if keyPressed("g"):
            spawnGororia()
        if keyPressed("o"):
            spawnOctorok()
        if keyPressed("t"):
            spawnTektite()
        
        if keyPressed("z"):
            link.rupees += 1
            if keyPressed("1"):
                link.rupees +=9
            if keyPressed("2"):
                link.rupees += 99
            if keyPressed("3"):
                link.rupees += 999
            if keyPressed("4"):
                link.rupees += 9999
        
        if keyPressed("5"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.speed = 0
        
        if keyPressed("6"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.speed = 20
        if keyPressed("f"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        if p.orientation == 0:
                            p.orientation = 1
                        elif p.orientation == 1:
                            p.orientation = 0
                        elif p.orientation == 2:
                            p.orientation = 3
                        else:
                            p.orientation = 2
        
        if keyPressed("w"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.orientation = 1
                        
        if keyPressed("s"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.orientation = 0
                        
        if keyPressed("a"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.orientation = 3
        
        
        if keyPressed("d"):
            if link.infHp == True:
                for p in currentScene.Projectiles:
                    if p.name == "link":
                        p.orientation = 2
        
        
        if keyPressed("1"):
            if keyPressed("3"):
                if keyPressed("7"):
                    if keyPressed("0"):
                        if timer == 10:
                            timer = 0
                            if link.infHp == False:
                                link.infHp = True
                                print("on")
                            else:
                                link.infHp = False
                                print("off")
                                
        if keyPressed("r"):
            spawnTestDummy()
                        
        if keyPressed("c"):
            for item in currentScene.Items:
                link.quickPickUp(item, link)
        
        
        if timer < 10:
            timer += 1
            
        if link.dead == False:
            if keyPressed("down"):
                changeSpriteImage(link, 0*2 + frame)
                link.orientation =0
                link.move(frame)
                link.down = True
            else:
                link.down = False
            if keyPressed("up"):
                changeSpriteImage(link, 1*2 + frame)
                link.orientation =1
                link.move(frame)
                link.up = True
            else:
                link.up = False
            if keyPressed("right"):
                changeSpriteImage(link, 2*2 + frame)
                link.orientation =2
                link.move(frame)
                link.right = True
            else:
                link.right = False
            if keyPressed("left"):
                changeSpriteImage(link, 3*2 + frame)
                link.orientation =3
                link.move(frame)
                link.left = True
            else:
                link.left = False
            if keyPressed("space"):
                if link.infHp == True:
                    sword.swing()
                    throwSword()
                else:
                    if sword.canSwing == True:
                        makeSwordWork(sword, currentScene)
                        showSprite(sword)
                        sword.swing()
                        throwSword()
                    
                    
                    

                        for mon in currentScene.Enemies:
                            if touching(sword, mon):
                                sword.hitSomething(mon, link)

                                if mon.hp == 0:
                                    link.kills += 1
                                    dropItem(mon)
                    else:
                        hideSprite(sword)
            else:
                hideSprite(sword)
                sword.swingTimer = 0
                sword.step = 0
                sword.canSwing = True
                swordFix = True
            
            if keyPressed("h"):
                changeSpriteImage(link, frame+12)
        else:
            hideSprite(sword)
        for item in currentScene.Items:
            item.animate(frame)
        if link.rect.x + 32//2 > 1024:
            hideBackground(currentScene)
            i += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = 0
            showSprite(link)
            reloadHud()
            reloadItems()
        if link.rect.x - 32//2 < -32:
            hideBackground(currentScene)
            i -= 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.x = 1024 - 32
            showSprite(link)
            reloadHud()
            reloadItems()
        if link.rect.y -32//2 < 64:
            hideBackground(currentScene)
            j -= 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = 768 - 32
            showSprite(link)
            reloadHud()
            reloadItems()
        if link.rect.y + 32//2 > 768:
            hideBackground(currentScene)
            j += 1
            currentScene = scenes[i][j]
            showBackground(currentScene)
            hideSprite(link)
            link.rect.y = 96+ 0
            showSprite(link)
            reloadHud()
            reloadItems()
            
        for item in currentScene.Items:
            if item.name == "fairy":
                item.fly()
        swordThrowCooldown()
        linkProjectiles()
        projectiles()
        TektiteJump()
        monsterStuff()
        linkStuff()
        updateDisplay()


endWait()
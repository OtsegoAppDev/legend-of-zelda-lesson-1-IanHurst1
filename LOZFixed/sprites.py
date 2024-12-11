import pygame.display
from pygame_functions import *
import random
from os import path
import base64
import math


class Player(newSprite):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.type = "link"
        self.rect.x = 500
        self.rect.y = 414
        self.speed = 6
        self.hp = 3
        self.startHp = 3
        self.timer = 0
        self.dead = False
        self.deathAnim = False
        self.up = False
        self.down = False
        self.left = False
        self.right = False
        self.inWall = False
        self.kills = 0
        self.rupees = 0
        self.hitTimer = 0
        self.canGetHit = True
        self.invincibilityTime = 12
        self.infHp = False

        
    def unDie(self):
        self.dead = False
        self.deathAnim = False
        self.hp = self.startHp
        
    def die(self):
        self.dead = True
        self.deathAnim = True
        self.timer = 0

        
        
    def deathAnimation(self):
        if self.deathAnim == True:
            changeSpriteImage(self, 13)
            if self.timer >= 7:
                changeSpriteImage(self, 12)
                self.deathAnim = False
        
        
    def hit(self, thing):
        if self.dead == False:
            if self.canGetHit == True:
                self.canGetHit = False
                if self.hp >= 0:
                    if self.infHp == False:
                        self.hp = self.hp - thing.damage
                    if thing.type == "Projectile":
                        if thing.orientation == 0:
                            self.rect.y = self.rect.y + 20
                        elif thing.orientation ==1:
                            self.rect.y = self.rect.y - 20
                        elif thing.orientation ==2:
                            self.rect.x = self.rect.x - 20
                        elif thing.orientation ==3:
                            self.rect.x = self.rect.x + 20
                    else:
                        if self.orientation == 0:
                            self.rect.y = self.rect.y + 20
                        elif self.orientation ==1:
                            self.rect.y = self.rect.y - 20
                        elif self.orientation ==2:
                            self.rect.x = self.rect.x - 20
                        elif self.orientation ==3:
                            self.rect.x = self.rect.x + 20
                    
                    if self.hp <= 0:
                        self.hp = 0
                        self.die()
                else:
                    self.hp = 0
    
    
    def pickUpItem(self, item, link):
        if self.rect.colliderect(item):
            if item.name == "heart":
                item.pickUp(self)
            if item.name == "heartContainer":
                item.collecting(link)
            if item.name == "rupee":
                if item.display == False:
                    item.pickUp(self)
            if item.name == "fairy":
                item.pickUp(self)
    def quickPickUp(self, item, link):
        if item.name == "heart":
            item.pickUp(self)
        if item.name == "heartContainer":
            item.collecting(link)
        if item.name == "rupee":
            if item.display == False:
                item.pickUp(self)
        if item.name == "fairy":
            item.pickUp(self)
    
    def moveOutOfWall(self, frame):
        if self.up == True:
            self.rect.y = self.rect.y + self.speed
        if self.down == True:
            self.rect.y = self.rect.y - self.speed
        if self.right == True:
            self.rect.x = self.rect.x - self.speed
        if self.left == True:
            self.rect.x = self.rect.x + self.speed


                
            
    def hitTest(self, otherSprite, name):
        if self.rect.colliderect(otherSprite.rect):
            self.hit(otherSprite)
            if name == "Projectile":
                otherSprite.rect.x = 2000
                killSprite(otherSprite)
    
    def move(self, frame):
        if self.dead == False:
            if self.inWall == False:
                if self.orientation == 0:
                    self.rect.y = self.rect.y + self.speed
                    self.changeImage(0*2 + frame)
                elif self.orientation ==1:
                    self.rect.y = self.rect.y - self.speed
                    self.changeImage(1*2 + frame)
                elif self.orientation ==2:
                    self.rect.x = self.rect.x + self.speed
                    self.changeImage(2*2 + frame)
                else:
                    self.rect.x = self.rect.x - self.speed
                    self.changeImage(3*2 + frame)
                
    def HitWall(self, wall, frame):
        if self.rect.colliderect(wall.rect):
            self.inWall = True
            self.moveOutOfWall(frame)
        else:
            self.inWall = False
            
    def countKills(self, mon):
        self.kills += 1
            


class Sword(newSprite):
    def __init__(self, player):
        newSprite.__init__(self, "WoodSword.png", 4, 2)
        self.player = player
        self.step = 0
        self.damage = 1
        self.canSwing = True
        self.swingTimer = 0
        self.type = "sword"
    
    def swing(self):
        self.swingTimer += 1
        if self.swingTimer == 3:
            self.swingTimer = 0
            
        changeSpriteImage(self.player, self.player.orientation + 8)
        if self.player.orientation ==0:
            self.changeImage(0 + self.step*4)
            self.move(self.player.rect.x, self.player.rect.y+32)
        elif self.player.orientation ==1:
            self.changeImage(1 + self.step*4)
            self.move(self.player.rect.x, self.player.rect.y-32)
        elif self.player.orientation ==2:
            self.changeImage(2 + self.step*4)
            self.move(self.player.rect.x+32, self.player.rect.y)
        elif self.player.orientation ==3:
            self.changeImage(3 + self.step*4)
            self.move(self.player.rect.x-32, self.player.rect.y)
        showSprite(self)
        
        self.step += 1
        if self.step == 2:
            self.step = 0
            self.canSwing = False
        

            
    def hitSomething(self,monster,link):
        monster.hit(self,link)




class Projectile(newSprite):
    def __init__(self, image, tile):
        newSprite.__init__(self, image, tile)
        self.damage = 1
        self.speed = 20
        self.wall_collide = False
        
def move(self, frame):
    self.rect.x += self.speed


class Rock(Projectile):
    def __init__(self):
        Projectile.__init__(self, "Rock.png", 2)
        self.wall_collide = True
        self.speed = 6
        damage = 1
        self.name = "monster"
        self.type = "Projectile"
        
        
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y -= self.speed
        elif self.orientation == 1:
            self.rect.y += self.speed
        elif self.orientation == 3:
            self.rect.x += self.speed
        else:
            self.rect.x -= self.speed
        changeSpriteImage(self, frame)
        
    def goingOfEdgeFix(self):
        if self.rect.y < 85:
            hideSprite(self)
            killSprite(self)
            
        if self.rect.x < -50:
            killSprite(self)
        if self.rect.x > 1050:
            killSprite(self)
        if self.rect.y > 800:
            killSprite(self)
        
    def hitWall(self, currentScene):
        for wall in currentScene.Wall_Tiles:
            if self.rect.colliderect(wall.rect):
                self.rect.x = 2000
                killSprite(self)


class SwordProjectile(Projectile):
    def __init__(self):
        Projectile.__init__(self, "SwordProjectile.png", 8)
        self.orientation = 0
        self.damage = 1
        self.name = "link"
        self.type = "SwordProjectile"
        self.speed = 20
        
    def move(self, frame):
        if self.orientation == 0:
            self.rect.y += self.speed
            changeSpriteImage(self, 0*2+frame)
        elif self.orientation == 1:
            self.rect.y -= self.speed
            changeSpriteImage(self, 1*2+frame)
        elif self.orientation == 3:
            self.rect.x -= self.speed
            changeSpriteImage(self, 3*2+frame)
        else:
            self.rect.x += self.speed
            changeSpriteImage(self, 2*2+frame)
            
        


    def goingOfEdgeFix(self):
        if self.rect.y < 85:
            hideSprite(self)
            killSprite(self)
            
        if self.rect.x < -50:
            killSprite(self)
        if self.rect.x > 1050:
            killSprite(self)
        if self.rect.y > 800:
            killSprite(self)





class monster(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
        self.type = "normal"
        self.rect.x = 400
        self.rect.y = 400
        self.speed = 1
        self.hp = 1
        self.damage = 1
        self.up = False
        self.down = True
        self.left = False
        self.right = False
        self.randFrame = 10
        self.randDirection = 1
        self.frameNum = 0
        self.dead = False
        self.knockback = 10
        self.canGetHit = True
        self.name = "A"
        
    def randNumbers(self):
        if self.type == "normal":
            self.randFrame = random.randint(10, 15)
            self.randDirection = random.randint(0, 4)
    
    
    def hit(self, weapon, link):
        if weapon.type != "sword":
            if self.hp == 1:
                self.dead = True
                killSprite(self)
            self.hp = self.hp - weapon.damage
            if self.hp < 0:
                self.hp = 0
                killSprite(self)
                self.dead = True
            ''' 
            if weapon.orientation == 0:
                self.rect.y = self.rect.y + self.knockback - 15
            elif weapon.orientation ==1:
                self.rect.y = self.rect.y - self.knockback - 15
            elif weapon.orientation ==2:
                self.rect.x = self.rect.x + self.knockback - 15
            elif weapon.orientation ==3:
                self.rect.x = self.rect.x - self.knockback - 15
            '''
        else:
            if self.canGetHit == True:
                self.canGetHit = False
                if self.hp == 1:
                    self.dead = True
                    killSprite(self)
                self.hp = self.hp - weapon.damage
                if self.hp < 0:
                    self.hp = 0
                    killSprite(self)
                    self.dead = True
                if link.orientation == 0:
                    self.rect.y = self.rect.y + self.knockback
                elif link.orientation ==1:
                    self.rect.y = self.rect.y - self.knockback
                elif link.orientation ==2:
                    self.rect.x = self.rect.x + self.knockback
                elif link.orientation ==3:
                    self.rect.x = self.rect.x - self.knockback
    
    def direction(self, frameCount):
        if self.type == "normal":
            if frameCount == self.randFrame:
                self.pickDirection()
    
    def noGoOut(self):
        if self.type == "normal":
            if self.rect.x >= 992:
                self.up = False
                self.down = False
                self.left = True
                self.right = False
            if self.rect.x <= 1:
                self.up = False
                self.down = False
                self.left = False
                self.right = True
            if self.rect.y <= 64+16:
                self.up = False
                self.down = True
                self.left = False
                self.right = False
            if self.rect.y >= 736:
                self.up = True
                self.down = False
                self.left = False
                self.right = False
                
                
    def pickDirection(self):
        if self.type == "normal":
            self.randNumbers()
            if self.randDirection == 0:
                self.up = True
                self.down = False
                self.left = False
                gLight = False
            elif self.randDirection == 1:
                self.up = False
                self.down = True
                self.left = False
                self.right = False
            elif self.randDirection == 2:
                self.up = False
                self.down = False
                self.left = True
                self.right = False
            elif self.randDirection == 3:
                self.up = False
                self.down = False
                self.left = False
                self.right = True
            else:
                self.up = False
                self.down = False
                self.left = False
                self.right = False
       
                
        def move(self, frame):
            if self.type == "normal":
                if self.up == True:
                    self.rect.y = self.rect.y - self.speed
                    if frame%2 == 0:
                        self.frameNum = 2
                    else:
                        self.frameNum = 6
                if self.down == True:
                    self.rect.y = self.rect.y + self.speed
                    if frame%2 == 0:
                        self.frameNum = 0
                    else:
                        self.frameNum = 4
                if self.left == True:
                    self.rect.x = self.rect.x - self.speed
                    if frame%2 == 0:
                        self.frameNum = 1
                    else:
                        self.frameNum = 5
                if self.right == True:
                    self.rect.x = self.rect.x + self.speed
                    if frame%2 == 0:
                        self.frameNum = 3
                    else:
                        self.frameNum = 7
                changeSpriteImage(self, self.frameNum)
            
    def HitWall(self, Wall, frame):
        if self.type == "normal":
            if self.rect.colliderect(Wall.rect):
                if self.up == True:
                    self.up = False
                    self.down = True
                elif self.down == True:
                    self.down = False
                    self.up = True
                elif self.left == True:
                    self.left = False
                    self.right = True
                elif self.right == True:
                    self.right = False
                    self.left = True
                self.move(frame)
        
class TestDummy(monster):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.hp = 100
        self.name = "A"
        self.type = "test Dummy"
        self.shoots = "no"
        self.damage = 0
        self.dead = False
        self.rect.x = 500
        self.rect.y = 500
        
    def move(self, frame):
        pass
    
    def hit(self, weapon, link):
        if weapon.type != "sword":
            if self.hp == 1:
                self.dead = True
                killSprite(self)
            self.hp = self.hp - weapon.damage
            if self.hp < 0:
                self.hp = 0
                killSprite(self)
                self.dead = True
        else:
            if self.canGetHit == True:
                self.canGetHit = False
                if self.hp == 1:
                    self.dead = True
                    killSprite(self)
                self.hp = self.hp - weapon.damage
                if self.hp < 0:
                    self.hp = 0
                    killSprite(self)
                    self.dead = True
        #print(self.hp)
                







class Tektite(monster):
    def __init__(self):
        newSprite.__init__(self,"Tektite.png", 1, 2)
        self.type = "not normal"
        self.shoots = "no"
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(150, 700)
        self.hp = 2
        self.damage = 1
        self.jump_x = 0
        self.jumpend_x = 250
        self.jump_y = -0.02*(self.jump_x - 63.23)**2 + 80
        self.newRandoms = True
        self.jumpTime = 20
        self.counter = 0
        self.newRandoms2 = True
        self.dead = False
        self.knockback = 10
        self.start_x = 0
        self.start_y = 0
        self.leftOrRight = random.randint(0,1)
        self.name = "A"
        
    def Jump(self):
        if self.newRandoms2 == True:
            if self.rect.x < 50:
                self.leftOrRight = 1
                self.orientation = 2
            elif self.rect.x > 1024 - 50:
                self.leftOrRight = 0
                self.orientation = 3
            else:
                self.leftOrRight = random.randint(0,1)
            self.jumpTime = random.randint(20, 40)
            if self.rect.y < 250:
                self.jumpend_x = random.randint(127, 150)
            elif self.rect.y > 768 - 150:
                self.jumpend_x = random.randint(50, 127)
            else:
                self.jumpend_x = random.randint(50, 150)
            self.start_x = self.rect.x
            self.start_y = self.rect.y
            self.newRandoms2 = False
        if self.newRandoms == True:
            if self.counter < self.jumpTime:
                self.counter += 1
            else:
                self.newRandoms == False
                if self.leftOrRight == 1:

                    "right"
                    if self.jump_x < self.jumpend_x:
                        self.jump_x += 20
                        self.jump_y = -0.02*(self.jump_x - 63.23)**2 + 80
                        
                        if self.rect.x < 1024 - 42:
                            self.rect.x = self.start_x + self.jump_x
                            self.rect.y = self.start_y - self.jump_y
                            changeSpriteImage(self, 1)
                        else:
                            changeSpriteImage(self, 0)

                    else:
                        changeSpriteImage(self, 0)
                        self.jump_x = 0
                        self.newRandoms = True
                        self.newRandoms2 = True
                        self.counter = 0
                elif self.leftOrRight == 0:

                    "left"
                    if self.jump_x < self.jumpend_x:
                        self.jump_x += 20
                        self.jump_y = -0.02*(self.jump_x - 63.23)**2 + 80
                        
                        

                        if self.rect.x > 10:

                            self.rect.x = self.start_x - self.jump_x
                            self.rect.y = self.start_y - self.jump_y
                            changeSpriteImage(self, 1)
                        else:
                            changeSpriteImage(self, 0)

                    else:
                        changeSpriteImage(self, 0)
                        self.jump_x = 0
                        self.newRandoms2 = True
                        self.newRandoms = True
                        self.counter = 0
                
        
        

class gororia(monster):
    def __init__(self):
        newSprite.__init__(self,"gororia.png", 4, 2)
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(150, 700)
        self.speed = 3
        self.type = "normal"
        self.shoots = "no"
        self.hp = 3
        self.damage = 1
        self.up = False
        self.down = True
        self.left = False
        self.right = False
        self.randFrame = 10
        self.randDirection = 1
        self.frameNum = 0
        self.dead = False
        self.knockback = 10
        self.name = "A"
    
    def move(self, frame):
        if self.up == True:
            self.orientation = 0
            self.rect.y = self.rect.y - self.speed
            if frame%2 == 0:
                self.frameNum = 2
            else:
                self.frameNum = 6
        if self.down == True:
            self.orientation = 1
            self.rect.y = self.rect.y + self.speed
            if frame%2 == 0:
                self.frameNum = 0
            else:
                self.frameNum = 4
        if self.left == True:
            self.orientation = 2
            self.rect.x = self.rect.x - self.speed
            if frame%2 == 0:
                self.frameNum = 1
            else:
                self.frameNum = 5
        if self.right == True:
            self.orientation = 3
            self.rect.x = self.rect.x + self.speed
            if frame%2 == 0:
                self.frameNum = 3
            else:
                self.frameNum = 7
        changeSpriteImage(self, self.frameNum)

        
        
        
        
        
class octorok(monster):
    def __init__(self):
        newSprite.__init__(self, "Octorok.png", 4, 2)
 
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(150, 700)
        self.speed = 2
        self.hp = 2
        self.type = "normal"
        self.shoots = "yes"
        self.damage = 1
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.randFrame = 10
        self.randDirection = 1
        self.frameNum = 0
        self.dead = False
        self.knockback = 10
        self.name = "A"
        self.time = 0
        self.orientation = 0
        self.shootCooldown = 20
        
    def move(self, frame):
        if self.up == True:
            self.orientation = 0
            self.rect.y = self.rect.y - self.speed
            if frame%2 == 0:
                self.frameNum = 2
            else:
                self.frameNum = 6
        if self.down == True:
            self.orientation = 1
            self.rect.y = self.rect.y + self.speed
            if frame%2 == 0:
                self.frameNum = 0
            else:
                self.frameNum = 4
        if self.left == True:
            self.orientation = 2
            self.rect.x = self.rect.x - self.speed
            if frame%2 == 0:
                self.frameNum = 1
            else:
                self.frameNum = 5
        if self.right == True:
            self.orientation = 3
            self.rect.x = self.rect.x + self.speed
            if frame%2 == 0:
                self.frameNum = 3
            else:
                self.frameNum = 7
        changeSpriteImage(self, self.frameNum)


    def shoot(self, frame, currentScene):
        if frame%2 == 0:
            self.time = self.time+1
        if self.time == self.shootCooldown:
            self.time = 0
            if random.randint(0,2) == 1:
                aRock = Rock()
                aRock.orientation = self.orientation
                aRock.rect.x = self.rect.x
                aRock.rect.y = self.rect.y
                if aRock.orientation == 0:
                    aRock.rect.y -= 32
                elif aRock.orientation == 1:
                    aRock.rect.y += 32
                elif aRock.orientation == 3:
                    aRock.rect.x += 32
                else:
                    aRock.rect.x -= 32
                currentScene.Projectiles.append(aRock)
                showSprite(aRock)

class heartContainer(newSprite):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        self.name = "heartContainer"
        self.rect.x = 500
        self.rect.y = 300
        self.collected = False
        
    def spawn(self):
        changeSpriteImage(self, 2)
        
        
    def collecting(self, link):
        self.rect.x = 2000
        self.rect.y = 2000
        killSprite(self)
        self.collected = True
        if link.startHp < 20:
            link.startHp = link.startHp + 1
            link.hp = link.startHp
        else:
            link.hp = link.startHp
            
    def animate(self, frame):
        pass
        











        
class heart(newSprite):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        
        self.rect.x = 800
        self.rect.y = 40
        self.number = 0
        self.distance = 17
        self.row = 1
        
    def removeHeart(self, link):
        if link.hp <= self.number:
            hideSprite(self)
            
    def addHeart(self, link):
        if link.hp > self.number:
            showSprite(self)
    
    def moveHeart(self):
        self.rect.x = self.rect.x + (self.number * self.distance)
        if self.row == 2:
            self.rect.y = 60
            self.rect.x = self.rect.x - 170

class Item(newSprite):
    def __init__(self):
        newSprite.__init__(self, image, x, y)
        self.name = "heart"
        self.rect.x = 2000
        self.rect.y = 2000
        self.value = 0
        self.collected = False
        
        
    def spawn(self,color, mon):
        if mon.type != "link":
            self.rect.x = mon.rect.x
            self.rect.y = mon.rect.y
        else:
            if random.randint(0,1) == 1:
                self.rect.x = mon.rect.x + random.randint(0, 64)
            else:
                self.rect.x = mon.rect.x - random.randint(0, 64)
            if random.randint(0,1) == 1:
                if self.rect.x - mon.rect.x > 32:
                    self.rect.y = mon.rect.y + random.randint(0, 64)
                else:
                    self.rect.y = mon.rect.y + random.randint(32, 64)
            else:
                if self.rect.x - mon.rect.x < -32:
                    self.rect.y = mon.rect.y - random.randint(0, 64)
                else:
                    self.rect.y = mon.rect.y - random.randint(32, 64)
        if self.name == "heart":
            if random.randint(1, 4) == 4:
                self.value = 5
                changeSpriteImage(self, 1)
        if self.name == "rupee":
            if color == "red":
                self.value = 1
                changeSpriteImage(self, 0)
            elif color == "blue":
                self.value = 5
                changeSpriteImage(self, 1)
            
        
    def animate(self, frame):
        pass







        
class heartPickUp(Item):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        self.name = "heart"
        self.rect.x = 2000
        self.rect.y = 2000
        self.value = 1
        self.collected = False
        
    def pickUp(self, link):
        if link.hp < link.startHp:
            link.hp = link.hp + self.value
            if link.hp > link.startHp:
                link.hp = link.startHp
        self.collected = True
        self.rect.x = 2000
        self.rect.y = 2000
        killSprite(self)
        
    def animate(self, frame):
        pass
    
    
class Rupee(Item):
    def __init__(self):
        newSprite.__init__(self, "rupee.png", 2, 1)
        self.name = "rupee"
        self.rect.x = 2000
        self.rect.y = 2000
        self.value = 1
        self.collected = False
        self.display = False
        
            
    def pickUp(self, link):
        link.rupees += self.value
        moveSprite(self, 2000, 2000)
        self.collected = True
        killSprite(self)
    
    def SpawnDisplay(self, x, y):
        moveSprite(self, x, y)
        self.display = True
        

class Fairy(Item):
    def __init__(self):
        newSprite.__init__(self, "Fairy.png", 2, 1)
        self.name = "fairy"
        self.rect.x = 2000
        self.rect.y = 2000
        self.collected = False
        self.orientation = 0
        self.changeDirection = True
        self.speed = 6
        self.timer = 0
        self.timerMax = 10
        
        
    def pickUp(self, link):
        link.hp = link.startHp
        moveSprite(self, 2000, 2000)
        self.collected = True
        killSprite(self)
        
    def animate(self, frame):
        self.changeImage(frame)
    
    def fly(self):
        self.wentOut()
        if self.changeDirection == True:
            self.orientation = random.randint(0,7)
            self.timerMax = random.randint(4,10)
            self.speed = random.randint(5,8)
            self.changeDirection = False
        if self.orientation == 0:
            #up
            self.rect.y -= self.speed
            self.runTimer()
        if self.orientation == 1:
            #up right
            self.rect.y -= self.speed/2
            self.rect.x += self.speed/2
            self.runTimer()
        if self.orientation == 2:
            #right
            self.rect.x += self.speed
            self.runTimer()
        if self.orientation == 3:
            #down right
            self.rect.y += self.speed/2
            self.rect.x += self.speed/2
            self.runTimer()
        if self.orientation == 4:
            #down
            self.rect.y += self.speed
            self.runTimer()
        if self.orientation == 5:
            #down left
            self.rect.y += self.speed/2
            self.rect.x -= self.speed/2
            self.runTimer()
        if self.orientation == 6:
            #left
            self.rect.x -= self.speed
            self.runTimer()
        if self.orientation == 7:
            #up left
            self.rect.y -= self.speed/2
            self.rect.x -= self.speed/2
            self.runTimer()   
                
    def runTimer(self):
        if self.timer >= self.timerMax:
            self.changeDirection = True
            self.timer = 0
        else:
            self.timer += 1
    def wentOut(self):
        if self.rect.x <= -10:
            self.rect.x = -60
            killSprite(self)
        if self.rect.y <= 86:
            self.rect.x = -60
            killSprite(self)
        if self.rect.x >= 1034:
            self.rect.x = -60
            killSprite(self)
        if self.rect.y >= 778:
            self.rect.x = -60
            killSprite(self)
            
class Tile(pygame.sprite.Sprite):
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.images = []
        self.images.append(self.image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 9
        self.scale = 1
        self.x = self.rect.x
        self.y = self.rect.y
        self.passThrough = False

    def addImage(self, aImage):
        self.images.append(aImage)

    def changeImage(self, index=0):
        self.image = self.images[index]

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]


# Note that Wall inherits from pygame sprite not newSprite
class Wall(Tile):
    """
    Walls are Scene Objects that most sprites cannot pass through
    """

    def __init__(self, image):
        Tile.__init__(self, image)
        self.passThrough = False
        self.choppable = False

    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]


class Scene:
    """
    A Scene is a background that does interact with the sprites.  For instance
    there are walls that the sprites cannot pass through
    """
    passTiles = ["C", "W", "b", "c", "d", "h", "i", "j", "n", "o", "p", "d", "q", "r", "s", "t", "k", "v"]

    def __init__(self, screen, player, spriteSheetFileName, mapFileName, framesX=1, framesY=1):
        global background

        self.player = player
        print("Loading: "+str(spriteSheetFileName))
        spriteSheet = loadImage(spriteSheetFileName)
        self.originalWidth = spriteSheet.get_width() // framesX
        self.originalHeight = spriteSheet.get_height() // framesY
        frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
        x = 0
        y = 0
        self.images = []
        for column in range(framesY):
            for frameNo in range(framesX):
                frameSurf = pygame.Surface((self.originalWidth, self.originalHeight), pygame.SRCALPHA, 32)
                frameSurf.blit(spriteSheet, (x, y))
                self.images.append(frameSurf.copy())
                x -= self.originalWidth
            y -= self.originalHeight
            x = 0
        # Other initialized parameters
        self.Wall_Tiles = []
        self.Ground_Tiles = []
        self.Water_Tiles = []
        self.Enemies = []
        self.Projectiles = []
        self.Items = []
        # Populate the lists
        game_folder = os.getcwd()
        map_data = []
        with open(path.join(game_folder, mapFileName), 'rt') as f:
            for line in f:
                map_data.append(line)

        i = 0
        for row, tiles in enumerate(map_data):
            for col, tile in enumerate(tiles):
                if tile in base64dict:
                    if tile in Scene.passTiles:
                        passTile = Tile(self.images[base64dict[tile]])
                        passTile.move(col * 32, row * 32)
                        self.Ground_Tiles.append(passTile)
                    else:
                        thisWall = Wall(self.images[base64dict[tile]])
                        thisWall.move(col * 32, row * 32)
                        if tile == 'Y' or tile == 'Z' or tile == 'a' or tile == 'e' or tile == 'f' or tile == 'g' or tile == 'k' or tile == 'l' or tile == 'm':
                            self.Water_Tiles.append(thisWall)
                        else:
                            self.Wall_Tiles.append(thisWall)
                            if tile == 'H':
                                thisWall.choppable = True
                                thisWall.addImage(self.images[base64dict['i']])
                            
                elif tile == "@":
                    enemy = octorok()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                    
                elif tile == "#":
                    enemy = gororia()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                    
                elif tile == "$":
                    item = heartContainer()
                    item.rect.x = col * 32
                    item.rect.y = row * 32
                    self.Items.append(item)
                    item.spawn()
                
                elif tile == "^":
                    enemy = Tektite()
                    enemy.rect.x = col * 32
                    enemy.rect.y = row * 32
                    self.Enemies.append(enemy)
                
                if tile not in base64dict:
                    thisGround = Tile(self.images[2])
                    thisGround.move(col * 32, row * 32)
                    self.Ground_Tiles.append(thisGround)
        self.surface = screen.copy()
        background = self.surface
        # Methods for Scrolling the Scene

    def scroll(self, x, y):
        for enemy in self.Enemies:
            enemy.speed = 0
            hideSprite(enemy)
        for projectile in self.Projectiles:
            killSprite(projectile)
        self.Projectiles = []
        for item in self.Items:
            killSprite(item)
        self.Items = []
        for tile in self.all_wall_panels:
            tile.move(tile.rect.x + x, tile.rect.y + y)
        for tile in self.all_ground_tiles:
            tile.move(tile.rect.x + x, tile.rect.y + y)
            
            
            
            
            
def dropChart(kills, type="A"):
    #0 is Rupee, 1 is heart, 2 is fairy, 3 is bomb, 4 is time, 5 is blue rupee
    A = [0,1,0,2,0,1,1,0,0,1]
    B = [3,0,4,0,1,3,0,3,1,1]
    C = [0,1,0,5,1,4,0,0,0,5]
    D = [1,3,0,1,3,1,1,1,0,1]
    kills -= 1
    kills = kills%10
    if random.randint(0,1) == 0:
        return None
    else:
        if type == "A":
            return A[kills]
        elif type == "B":
            return B[kills]
        elif type == "C":
            return C[kills]
        elif type == "D":
            return D[kills]
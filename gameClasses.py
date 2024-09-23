from pygame_functions3 import *
import random
from pygame import *







class Player(newSprite):
    def __init__(self):
        newSprite.__init__(self, "LinkSimple.png", 14)
        self.rect.x = 500
        self.rect.y = 350
        self.speed = 4
        self.hp = 3
        self.startHp = 3
        self.timer = 0
        self.dead = False
        self.deathAnim = False
        print(self.rect)
        
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
        
        
    def hit(self, damage):
        if self.dead == False:
            if self.hp >= 0:
                self.hp = self.hp - damage
                if self.orientation == 0:
                    self.rect.y = self.rect.y - 40
                elif self.orientation ==1:
                    self.rect.y = self.rect.y + 40
                elif self.orientation ==2:
                    self.rect.x = self.rect.x - 40
                elif self.orientation ==3:
                    self.rect.x = self.rect.x + 40 
                if self.hp <= 0:
                    self.hp = 0
                    self.die()
                print(self.hp)
            else:
                self.hp = 0
            
            
    def hitTest(self, otherSprite):
        
        if self.rect.colliderect(otherSprite.rect):
            self.hit(otherSprite.damage)
    
    def move(self, frame):
        if self.dead == False:
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


class Sword(newSprite):
    def __init__(self, player):
        newSprite.__init__(self, "WoodSword.png", 4, 2)
        self.player = player
        self.step = 0
        self.damage = 1
    
    def swing(self):
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
            
    def hitSomething(self,monster,link):
        if self.rect.colliderect(monster.rect):
            monster.hit(self.damage,link)
        
class monster(newSprite):
    def __init__(self, filename, framesX=1, framesY=1):
        newSprite.__init__(self, filename, framesX, framesY)
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
        
    def randNumbers(self):
        self.randFrame = random.randint(10, 15)
        self.randDirection = random.randint(0, 5)
    
    
    def hit(self, damage, link):
        self.hp = self.hp - damage
        if self.hp < 0:
            self.hp = 0
            killSprite(self)
            self.dead = True
        if link.orientation == 0:
            self.rect.y = self.rect.y + 20
        elif link.orientation ==1:
            self.rect.y = self.rect.y - 20
        elif link.orientation ==2:
            self.rect.x = self.rect.x + 20
        elif link.orientation ==3:
            self.rect.x = self.rect.x - 20
    
    def direction(self, frameCount):
        if frameCount == self.randFrame:
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
            if self.rect.x <= 10:
                self.up = False
                self.down = False
                self.left = False
                self.right = True
            if self.rect.x >= 1004:
                self.up = False
                self.down = False
                self.left = True
                self.right = False
            if self.rect.y <= 10:
                self.up = False
                self.down = True
                self.left = False
                self.right = False
            if self.rect.y >= 748:
                self.up = True
                self.down = False
                self.left = False
                self.right = False
                
        def move(self, frame):
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
            
        

class gororia(monster):
    def __init__(self):
        newSprite.__init__(self,"gororia.png", 4, 2)
        self.rect.x = 400
        self.rect.y = 400
        self.speed = 4
        self.hp = 4
        self.damage = 2
        self.up = False
        self.down = True
        self.left = False
        self.right = False
        self.randFrame = 10
        self.randDirection = 1
        self.frameNum = 0
        self.dead = False
    
    def move(self, frame):
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

        
        
        
        
        
class octorok(monster):
    def __init__(self):
        newSprite.__init__(self, "Octorok.png", 4, 2)
 
        self.rect.x = 200
        self.rect.y = 200
        self.speed = 3
        self.hp = 2
        self.damage = 1
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.randFrame = 10
        self.randDirection = 1
        self.frameNum = 0
        self.dead = False
               
    def move(self, frame):
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
    

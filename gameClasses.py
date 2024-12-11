from pygame_functions3 import *
#from pygame_functions3 import newSprite
import random
from pygame import *
from os import path
import base64


base64dict = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "I":8, "J":9, "K":10, "L":11, "M":12, "N":13, "O":14, "P":15,
              "Q":16, "R":17, "S":18, "T":19, "U":20, "V":21, "W":22, "X":23, "Y":24, "Z":25, "a":26, "b":27, "c":28, "d":29, "e":30,
              "f":31, "g":32, "h":33, "i":34, "j":35, "k":36, "l":37, "m":38, "n":39, "o":40, "p":41, "q":42, "r":43, "s":44, "t":45, "u":46,
              "v":47, "w":48, "x":49, "y":50, "z":51, "0":52, "1":53, "2":54, "3":55, "4":56, "5":57, "6":58, "7":59, "8":60, "9":61, "+":62, "/":63}
'''

class Background():
    """
    The Background class creates a background that does not interact with the sprites.  It can scroll.
    """
    def __init__(self):
        self.colour = pygame.Color("black")

    def setTiles(self, tiles):
        if type(tiles) is str:
            self.tiles = [[loadImage(tiles)]]
        elif type(tiles[0]) is str:
            self.tiles = [[loadImage(i) for i in tiles]]
        else:
            self.tiles = [[loadImage(i) for i in row] for row in tiles]
        self.stagePosX = 0
        self.stagePosY = 0
        self.tileWidth = self.tiles[0][0].get_width()
        self.tileHeight = self.tiles[0][0].get_height()
        screen.blit(self.tiles[0][0], [0, 0])
        self.surface = screen.copy()

    def scroll(self, x, y):
        self.stagePosX -= x
        self.stagePosY -= y
        col = (self.stagePosX % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        xOff = (0 - self.stagePosX % self.tileWidth)
        row = (self.stagePosY % (self.tileHeight * len(self.tiles))) // self.tileHeight
        yOff = (0 - self.stagePosY % self.tileHeight)

        col2 = ((self.stagePosX + self.tileWidth) % (self.tileWidth * len(self.tiles[0]))) // self.tileWidth
        row2 = ((self.stagePosY + self.tileHeight) % (self.tileHeight * len(self.tiles))) // self.tileHeight
        screen.blit(self.tiles[row][col], [xOff, yOff])
        screen.blit(self.tiles[row][col2], [xOff + self.tileWidth, yOff])
        screen.blit(self.tiles[row2][col], [xOff, yOff + self.tileHeight])
        screen.blit(self.tiles[row2][col2], [xOff + self.tileWidth, yOff + self.tileHeight])

        self.surface = screen.copy()

    def setColour(self, colour):
        self.colour = parseColour(colour)
        screen.fill(self.colour)
        pygame.display.update()
        self.surface = screen.copy()
'''
class Scene:
    """
    A Scene is a background that does interact with the sprites.  For instance
    there are walls that the sprites cannot pass through
    """
    def __init__(self, player, spriteSheetFileName, mapFileName, framesX=1, framesY=1):
        global background
        self.player = player
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
            y -=self.originalHeight
            x = 0
        #Other initialized parameters
        self.Wall_Tiles = []
        self.Ground_Tiles = []
        self.Enemies = []
        self.Projectiles = []
        self.Items=[]
        #Populate the lists
        game_folder = os.getcwd()
        map_data = []
        with open(path.join(game_folder, mapFileName), 'rt') as f:
            for line in f:
                map_data.append(line)
                
        i = 0
        for row, tiles in enumerate(map_data):
                for col, tile in enumerate(tiles):
                    if tile in base64dict:
                        thisWall = Wall(self.images[base64dict[tile]])
                        thisWall.move(col*32, row*32)
                        self.Wall_Tiles.append(thisWall)    
                    elif tile == "@":
                        enemy = octorok()
                        enemy.rect.x=col*32
                        enemy.rect.y=row*32
                        self.Enemies.append(enemy)
                    if tile not in base64dict:
                        thisGround = Wall(self.images[2])
                        thisGround.move(col*32, row*32)
                        self.Ground_Tiles.append(thisGround)
        self.surface=screen.copy()
        background=self.surface
        #Methods for Scrolling the Scene
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
            tile.move(tile.rect.x+x, tile.rect.y+y)
        for tile in self.all_ground_tiles:
            tile.move(tile.rect.x+x, tile.rect.y+y)



class Wall(pygame.sprite.Sprite):
    """
    Walls are Scene Objects that most sprites cannot pass through
    """
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (0,0)
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 9
        self.scale = 1
        self.x = self.rect.x
        self.y = self.rect.y
    def move(self, xpos, ypos, centre=False):
        if centre:
            self.rect.center = [xpos, ypos]
        else:
            self.rect.topleft = [xpos, ypos]





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
                
                
    def collectedHeart(self, Heart, link):
        if self.rect.colliderect(Heart):
            Heart.collecting(link)
            
    def pickedUpHeart(self, heart):
        if self.rect.colliderect(heart):
            heart.pickUp(self)
            
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
            self.pickDirection()
    
    def noGoOut(self):
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
        if self.rect.y <= 1:
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
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(100, 500)
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
 
        self.rect.x = random.randint(100, 900)
        self.rect.y = random.randint(100, 500)
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


class heartContainer(newSprite):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        self.rect.x = 500
        self.rect.y = 300
        self.collected = False
        
    def spawn(self):
        changeSpriteImage(self, 2)
        showSprite(self)
        
        
    def collecting(self, link):
        self.rect.x = 2000
        self.rect.y = 2000
        killSprite(self)
        self.collected = True
        if link.startHp < 10:
            link.startHp = link.startHp + 1
            link.hp = link.startHp
        else:
            link.hp = link.startHp
        











        
class heart(newSprite):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        
        self.rect.x = 800
        self.rect.y = 80
        self.number = 0
        self.distance = 17
        
    def removeHeart(self, link):
        if link.hp <= self.number:
            hideSprite(self)
            
    def addHeart(self, link):
        if link.hp > self.number:
            showSprite(self)
    
    def moveHeart(self):
        self.rect.x = self.rect.x + (self.number * self.distance)
        
        
class heartPickUp(newSprite):
    def __init__(self):
        newSprite.__init__(self, "Hearts.png", 3, 1)
        self.rect.x = 400
        self.rect.y = 400
        self.heal = 1
        self.collected = False
        
    def pickUp(self, link):
        if link.hp < link.startHp:
            link.hp = link.hp + self.heal
            if link.hp > link.startHp:
                link.hp = link.startHp
        self.collected = True
        self.rect.x = 2000
        self.rect.y = 2000
        killSprite(self)
        
    def Spawn(self, mon):
        self.rect.x = mon.rect.x
        self.rect.y = mon.rect.y
        if random.randint(1 ,5) == 5:
            self.heal = 2
            changeSpriteImage(self, 1)
        
        
        
#class live(heart):
 #   def __init__(self):
  #      newSprite.__init__(self, "Hearts.png", 3, 1)
        
        
        
        
    

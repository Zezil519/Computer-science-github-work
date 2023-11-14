import pygame
import random
 
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

moveTimer = 0
bulletTimer = 1
lr = 2
down = False
keya = False
keyd = False
keyspace = False
gamestate = 0
gamelevel = 1
levelPause = 0
endPause = 0


class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
       
 
        super().__init__()
 
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.Turn = False
        self.rect = self.image.get_rect()



class Barrier(Block):
    def __init__(self, color, width, height, health):
        super().__init__(color, width, height)
        self.life = health

    def decHealth(self):
        self.life = self.life - 1

    def checkAlive(self):
        if self.life == 0:
            return True
        else:
            return False
            
class Enemy(Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def ready2Shoot(self, diff):
        if random.randrange(1,700-diff*5) == 2:
            return True
        else:
            return False
             
         
pygame.init()
 
screen_width = 700
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
 

laser_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()
temp_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
barrier_list = pygame.sprite.Group()
 
clock = pygame.time.Clock()
 
score = 0

done = False
 
while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                keya = True
            if event.key == pygame.K_d:
                keyd = True
            if event.key == pygame.K_SPACE:
                keyspace = True
                if gamestate == 0:
                    gamestate = 1
                    levelPause = 0
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                keya = False
            if event.key == pygame.K_d:
                keyd = False
            if event.key == pygame.K_SPACE:
                keyspace = False
 
    screen.fill(BLACK)
 
    if gamestate == 0:
        font = pygame.font.SysFont("Comic Sans MC", 50)
        textStart = font.render("START GAME",True,WHITE)
        font = pygame.font.SysFont("Comic Sans MC", 80)
        textTitle = font.render("SPACE INVADER",True,WHITE)
        screen.blit(textStart, (240, 400))
        screen.blit(textTitle, (140,10))
        
    elif gamestate == 1:
        font = pygame.font.SysFont("Comic Sans MC", 70)
        textLevel = font.render("LEVEL " + str(gamelevel),True,WHITE)
        screen.blit(textLevel, (260, 270))
        levelPause = levelPause + 1
        if levelPause == 120:
            gamestate = 2

            blockX = 140   
            for i in range(5):
                block = Enemy(WHITE, 20, 15)
 
                block.rect.x = blockX
                blockX = blockX + 100
                block.rect.y = 50
                enemy_list.add(block)
                all_sprites_list.add(block)
            
            blockX= 140
            for i in range(5):
                block = Enemy(WHITE, 20, 15)
         
                block.rect.x = blockX
                blockX = blockX + 100
                block.rect.y = 150
                enemy_list.add(block)
                all_sprites_list.add(block)
            
            blockX = 190
            for i in range(4):
                block = Enemy(WHITE, 20, 15)
             
                block.rect.x = blockX
                blockX = blockX + 100
                block.rect.y = 100
                enemy_list.add(block)
                all_sprites_list.add(block)
             
            blockX = 110
            for i in range(3):
                barrier = Barrier(GREEN, 80, 50, 10)
             
                barrier.rect.x = blockX
                blockX = blockX + 200
                barrier.rect.y = 490
                all_sprites_list.add(barrier)
                barrier_list.add(barrier)
        
        
        
            player = Block(RED, 20, 15)
            all_sprites_list.add(player)
            player.rect.x = 340
            player.rect.y = 585
    elif gamestate == 2:
        if keya == True:
            player.rect.x = player.rect.x - 5
        if keyd == True:
            player.rect.x = player.rect.x + 5
 

 
        for mybullet in bullet_list:
            for block in enemy_list:
                if block.rect.colliderect(mybullet.rect):
                    score = score + 1
                    block.kill()
                    mybullet.kill()
                    if score == 14:
                        for block in all_sprites_list:
                            block.kill()
                        gamelevel = gamelevel + 1
                        gamestate = 1
                        score = 0
                        levelPause = 0
                        if gamelevel == 11:
                            gamestate == 4
            for barrier in barrier_list:
                if barrier.rect.colliderect(mybullet.rect):
                    Barrier.decHealth(barrier)
                    mybullet.kill()
                if not(Barrier.checkAlive(barrier)) == False:
                    barrier.kill()


        for laser in laser_list:
            for barrier in barrier_list:
                if barrier.rect.colliderect(laser.rect):
                    Barrier.decHealth(barrier)
                    laser.kill()
                if not(Barrier.checkAlive(barrier)) == False:
                    barrier.kill()
            if laser.rect.colliderect(player.rect):
                gamestate = 3
                for block in all_sprites_list:
                    block.kill()
            
       

                       
        down = False
        for block in enemy_list:
            if block.rect.x > 630:
                lr = 1
                down = True
            if block.rect.x < 30:
                lr = 2
                down = True
            if Enemy.ready2Shoot(block,gamelevel):
                laser = Block(YELLOW, 2, 10)
                laser.rect.x = block.rect.x + 9
                laser.rect.y = block.rect.y + 8
                laser_list.add(laser)
                all_sprites_list.add(laser)
        
        for laser in laser_list:
            if laser.rect.y < 720:
                laser.rect.y = laser.rect.y + 2 + gamelevel*1/10
            else:
                laser.kill()

        if moveTimer == 10:
            moveTimer = 0
            for block in enemy_list:
                block.rect.x = block.rect.x + gamelevel*3*(-1)**lr
                if down == True:
                    block.rect.x = block.rect.x + gamelevel*3*(-1)**lr
                    block.rect.y = block.rect.y + 10
                if block.rect.y >= 700 or block.rect.colliderect(player.rect):
                    gamestate = 3
        
        if bulletTimer == 30:
            bulletTimer = 0
    
        if keyspace == True and bulletTimer == 0:
            bulletTimer = 1
            mybullet = Block(BLUE, 6, 10)
            mybullet.rect.x = player.rect.x + 7
            mybullet.rect.y = player.rect.y - 6
            bullet_list.add(mybullet)
            all_sprites_list.add(mybullet)
        
        for mybullet in bullet_list:
            if mybullet.rect.y > 30:
                mybullet.rect.y = mybullet.rect.y - 2
            else:
                mybullet.kill()
            for laser in laser_list:
                if mybullet.rect.colliderect(laser.rect):
                    mybullet.kill()
                    laser.kill()
        moveTimer = moveTimer + 1
        
        if bulletTimer != 0:
            bulletTimer = bulletTimer + 1
        all_sprites_list.draw(screen)
        
        for barrier in barrier_list:
            font = pygame.font.SysFont("Comic Sans MC", 30)
            textBarrier = font.render(str(barrier.life),True,BLACK)
            screen.blit(textBarrier, (barrier.rect.x + 5, barrier.rect.y + 2))
            
    elif gamestate == 3:
        font = pygame.font.SysFont("Comic Sans MC", 80)
        textLost = font.render("YOU LOST",True,WHITE)
        screen.blit(textLost, (220, 280))
        if endPause == 120:
            gamestate = 0
        else:
            endPause = endPause + 1
    elif gamestate == 4:
        font = pygame.font.SysFont("Comic Sans MC", 80)
        textLost = font.render("YOU WON",True,WHITE)
        screen.blit(textLost, (230, 280))
        if endPause == 120:
            gamestate = 0
        else:
            endPause = endPause + 1
    pygame.display.flip()
     
    clock.tick(60)
 
pygame.quit()

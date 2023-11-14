import pygame
import math
import random

pygame.font.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ballx = 340
bally = 240
ud = 1 # up 1 down 2
lr = 2 #left 1 right 2
highscores = []
username = []

diff = 5
pada = 220
#padb = 220
scorea = 0
scoreb = 0
scoreboard = False
savescore= False
done = False
keyw = False
keys = False

#keyo = False
#keyl = False
stoptimer = 0
PI = 3.141592653589793
angle = 1

def load_highscores():
    try:
        with open("highscores.txt", "r") as file:
            return [line.strip().split(":") for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_highscores():
    with open("highscores.txt", "w") as file:
        for entry in highscores:
            file.write(f"{entry[0]}:{entry[1]}\n")

def display_highscores():
    font = pygame.font.SysFont("Comic Sans MC", 30)
    y = 100
    for entry in highscores:
        text = font.render(f"{entry[0]}: {entry[1]}", True, WHITE)
        screen.blit(text, (250, y))
        y += 30
    
    


def calcxvelo(angle, speed):
    return speed*math.cos(angle)
def calcyvelo(angle, speed):
    return speed*math.sin(angle)
 
clock = pygame.time.Clock()
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                    keyw = True
            if event.key == pygame.K_s:
                    keys = True
            #if event.key == pygame.K_o:
             #       keyo = True
            #if event.key == pygame.K_l:
             #       keyl = True
            if event.key == pygame.K_h:
                    scoreboard = True
            if event.key == pygame.K_g:
                    savescore = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                    keyw = False
            if event.key == pygame.K_s:
                    keys = False
            #if event.key == pygame.K_o:
             #       keyo = False
            #if event.key == pygame.K_l:
             #       keyl = False
            if event.key == pygame.K_h:
                    scoreboard = False
            if event.key == pygame.K_g:
                    savescore = False
    screen.fill(BLACK)
            
    font = pygame.font.SysFont("Comic Sans MC", 100)
    text = font.render(str(scorea),True,WHITE)
    text2 = font.render(str(scoreb),True,WHITE)
    screen.blit(text, (250, 10))
    screen.blit(text2, (440,10))


    if stoptimer >= 0:
        stoptimer = stoptimer + 1
    if stoptimer > 120:
        stoptimer = -1
    if stoptimer == -1:
        ballx = ballx + calcxvelo(angle,diff)*(-1)**lr
        bally = bally + calcyvelo(angle,diff)*(-1)**ud

    if diff < 10:
        diff = diff + 0.001
    
    if ballx > 670 and lr == 2:
        lr = 1
        if bally + 10 <= padb - 10 or bally + 10 >= padb + 70:
            scorea = 0
            scoreb = 0
            ballx = 340
            bally = 240
            diff = 5
            stoptimer = 0
            angle = 1
        else:
            scoreb = scoreb + 1
         #   if keyo == True:
          #      if ud == 1:
           #         angle = angle * 0.7
            #    if ud == 2:
             #       angle = angle * 1.3
            #if keyl == True:
               # if ud == 2:
             #       angle = angle * 0.7
              #  if ud == 1:
               #     angle = angle * 1.3 
                
    if ballx < -10 and lr == 1:
        lr = 2
        if bally + 10 <= pada - 10 or bally + 10 >= pada + 70:
            scorea = 0
            scoreb = 0
            ballx = 340
            bally = 240
            diff = 5
            stoptimer = 0
            angle = 1
        else:
            scorea = scorea + 1
            if keyw == True:
                if ud == 1:
                    angle = angle * 0.7
                if ud == 2:
                    angle = angle * 1.3
            if keys == True:
                if ud == 2:
                    angle = angle * 0.7
                if ud == 1:
                    angle = angle * 1.3 
    if bally > 470 and ud == 2:
        ud = 1
    if bally < -10 and ud == 1:
        ud = 2
    
    if keyw == True:
        if pada > 0:
            pada = pada - diff*1.5
    if keys == True:
        if pada < 440:
            pada = pada + diff*1.5
    #if keyo == True:
     #   if padb > 0:
     #       padb = padb - diff*1.5
    #if keyl == True:
    #    if padb < 440:
    #        padb = padb + diff*1.5
    padb = bally 
    
    if savescore:
        username = input("Enter your username: ")
        highscores.append((username, scorea))
        highscores.sort(key=lambda x: x[1], reverse=True)
        save_highscores()

    if scoreboard:
         display_highscores()
   
    pygame.draw.ellipse(screen,WHITE,[ballx+10,bally+10,20,20],0)
    pygame.draw.rect(screen,RED,[0,pada,5,60],0)
    pygame.draw.rect(screen,RED,[695,padb,5,60],0)
    pygame.display.flip()
    
  

    clock.tick(60)
 
pygame.quit()

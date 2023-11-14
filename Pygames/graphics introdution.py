"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255,255,0)

PI=3.14159265
sunx=600
suny=100
lr = 0 #0 left 1 right
pygame.init()
 

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 

done = False
 
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if sunx == 600 and lr == 1:
        lr = 0
    if sunx == 100 and lr == 0:
        lr = 1
    if lr == 0:
        sunx=sunx-10
    if lr == 1:
        sunx=sunx+10
    suny = (sunx-350)**2/500+70
    
    screen.fill(BLUE)
    pygame.draw.rect(screen,GREEN,[0,300,700,200],0)
    pygame.draw.rect(screen,WHITE,[200,200,300,300],0)
    pygame.draw.rect(screen,BLACK,[200,200,300,300],2)
    pygame.draw.rect(screen,BLACK,[240,240,60,60],2)
    pygame.draw.rect(screen,BLACK,[400,240,60,60],2)
    pygame.draw.rect(screen,BLACK,[320,380,60,120],2)
    pygame.draw.ellipse(screen,BLACK,[325,435,10,10],0)
    pygame.draw.polygon(screen, WHITE, [[200,200], [500,200], [350,150]], 0)
    pygame.draw.polygon(screen, BLACK, [[200,200], [500,200], [350,150]], 2)
    pygame.draw.ellipse(screen,YELLOW,[sunx-50,suny-50,100,100],0)
    pygame.draw.ellipse(screen,BLACK,[sunx-50,suny-50,100,100],2)
    pygame.draw.ellipse(screen,BLACK,[sunx-25,suny-25,10,10],0)
    pygame.draw.ellipse(screen,BLACK,[sunx+15,suny-25,10,10],0)
    pygame.draw.arc(screen, BLACK, [sunx-50,suny-70,100,100],  5*PI/4, 7*PI/4, 2)
    
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(120)
 
pygame.quit()

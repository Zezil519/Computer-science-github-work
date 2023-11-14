import pygame

pygame.font.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
LIGHT_GREY = (200,200,200)


def displayBg():
    for i in range(3):
        pygame.draw.rect(screen,RED,[155,200+100*i,90,90],0)
    for i in range(3):
        for k in range(2):
            pygame.draw.rect(screen,LIGHT_GREY,[255+100*k,200+100*i,90,90],0)
    for i in range(3):
        pygame.draw.rect(screen,GREEN,[455,200+100*i,90,90],0)

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.color = color
    #def highlightBlock(self):
        
        
       
class Zu(Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def showBlock(self):      
        pygame.draw.rect(screen,self.color,[self.rect.x,self.rect.y,70,70],5)
        pygame.draw.rect(screen,WHITE,[self.rect.x,self.rect.y,70,70],2)
        font = pygame.font.SysFont("Comic Sans MC", 30)
        textShown = font.render('Z',True,BLACK)
        screen.blit(textShown, (self.rect.x+28, self.rect.y+26))

class Wang(Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def showBlock(self):
        pygame.draw.rect(screen,self.color,[self.rect.x,self.rect.y,70,70],5)
        pygame.draw.rect(screen,WHITE,[self.rect.x,self.rect.y,70,70],2)
        font = pygame.font.SysFont("Comic Sans MC", 30)
        textShown = font.render('W',True,BLACK)
        screen.blit(textShown, (self.rect.x+25, self.rect.y+26))

class Xiang(Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def showBlock(self):
        pygame.draw.rect(screen,self.color,[self.rect.x,self.rect.y,70,70],5)
        pygame.draw.rect(screen,WHITE,[self.rect.x,self.rect.y,70,70],2)
        font = pygame.font.SysFont("Comic Sans MC", 30)
        textShown = font.render('X',True,BLACK)
        screen.blit(textShown, (self.rect.x+28, self.rect.y+26))

class Jiang(Block):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)
    def showBlock(self):
        pygame.draw.rect(screen,self.color,[self.rect.x,self.rect.y,70,70],5)
        pygame.draw.rect(screen,WHITE,[self.rect.x,self.rect.y,70,70],2)
        font = pygame.font.SysFont("Comic Sans MC", 30)
        textShown = font.render('J',True,BLACK)
        screen.blit(textShown, (self.rect.x+28, self.rect.y+26))

all_list = pygame.sprite.Group()
red_list = pygame.sprite.Group()
green_list = pygame.sprite.Group()

zu_list = pygame.sprite.Group()
zu = Zu(RED, 70, 70)
zu.rect.x = 265
zu.rect.y = 310
zu_list.add(zu)
all_list.add(zu)
red_list.add(zu)
zu = Zu(GREEN, 70, 70)
zu.rect.x = 365
zu.rect.y = 310
zu_list.add(zu)
all_list.add(zu)
green_list.add(zu)

wang_list = pygame.sprite.Group()
wang = Wang(RED, 70, 70)
wang.rect.x = 165
wang.rect.y = 310
wang_list.add(wang)
all_list.add(wang)
red_list.add(wang)
wang = Wang(GREEN, 70, 70)
wang.rect.x = 465
wang.rect.y = 310
wang_list.add(wang)
all_list.add(wang)
green_list.add(wang)

xiang_list = pygame.sprite.Group()
xiang = Xiang(RED, 70, 70)
xiang.rect.x = 165
xiang.rect.y = 210
xiang_list.add(xiang)
all_list.add(xiang)
red_list.add(xiang)
xiang = Xiang(GREEN, 70, 70)
xiang.rect.x = 465
xiang.rect.y = 410
xiang_list.add(xiang)
all_list.add(xiang)
green_list.add(xiang)

jiang_list = pygame.sprite.Group()
jiang = Jiang(RED, 70, 70)
jiang.rect.x = 165
jiang.rect.y = 410
jiang_list.add(jiang)
all_list.add(jiang)
red_list.add(jiang)
jiang = Jiang(GREEN, 70, 70)
jiang.rect.x = 465
jiang.rect.y = 210
jiang_list.add(jiang)
all_list.add(jiang)
green_list.add(jiang)

chessBoard = ["X","","","J","W","Z","Z","W","J","","","X"]
      
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    screen.fill(BLACK)

    displayBg()
    
    all_list.draw(screen)
    
    for zu in zu_list:
        Zu.showBlock(zu)
    for wang in wang_list:
        Wang.showBlock(wang)
    for xiang in xiang_list:
        Xiang.showBlock(xiang)
    for jiang in jiang_list:
        Jiang.showBlock(jiang)
    #for all in all_list:
     #   Block.highlightBlock(block)
    pygame.display.flip()
 
    clock.tick(60)

pygame.quit()

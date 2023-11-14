import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

currentNumber = 0
stop = True
pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Timer")

def displayNumber(time):
    ROM = [11110111,10010010,11011101,11011011,10111010,11101011,11101111,11010010,11111111,11111011]
    x = 350
    y = 250
    for i in range(7):
        currentDigit = int(str(time)[i:i+1])
        temp = str(ROM[currentDigit])
        if temp[1:2] == "1":
            pygame.draw.rect(screen,WHITE,[x-130+(i)*40,y-27.5,20,5],0)
        if temp[2:3] == "1":
            pygame.draw.rect(screen,WHITE,[x-135+(i)*40,y-22.5,5,20],0) 
        if temp[3:4] == "1":
            pygame.draw.rect(screen,WHITE,[x-110+(i)*40,y-22.5,5,20],0)
        if temp[4:5] == "1":
            pygame.draw.rect(screen,WHITE,[x-130+(i)*40,y-2.5,20,5],0)
        if temp[5:6] == "1":
            pygame.draw.rect(screen,WHITE,[x-135+(i)*40,y+2.5,5,20],0)
        if temp[6:7] == "1":
            pygame.draw.rect(screen,WHITE,[x-110+(i)*40,y+2.5,5,20],0)
        if temp[7:8] == "1":
            pygame.draw.rect(screen,WHITE,[x-130+(i)*40,y+22.5,20,5],0)
        
    pygame.draw.rect(screen,WHITE,[x-103,y+12.5,5,5],0)
    pygame.draw.rect(screen,WHITE,[x-103,y-7.5,5,5],0)
    pygame.draw.rect(screen,WHITE,[x-23,y+12.5,5,5],0)
    pygame.draw.rect(screen,WHITE,[x-23,y-7.5,5,5],0)
    pygame.draw.rect(screen,WHITE,[x+57,y+12.5,5,5],0)
    pygame.draw.rect(screen,WHITE,[x+57,y-7.5,5,5],0)

def getTime(currentNumber):
    digits = []
    digits.append(int(currentNumber % 100))
    currentNumber = (currentNumber - digits[0])/100
    digits.append(int(currentNumber % 60))
    currentNumber = (currentNumber - digits[1])/60
    digits.append(int(currentNumber % 60))
    currentNumber = (currentNumber - digits[2])/60
    digits.append(int(currentNumber))
    return digits[0] + digits[1]*100 + digits[2]*10000 + digits[3]*1000000
    
def convertToStr(time):
    if len(str(time)) == 7:
        return str(time)
    else:
        counter = 7-len(str(time))
        newstr = ""
        for i in range(counter):
            newstr = newstr + "0"
        newstr = newstr + str(time)
    return newstr

def incrementTimer(currentNumber):
    if currentNumber == 3599999:
        return 0
    else:
        return currentNumber + 1
        
done = False
 
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                stop = not(stop)
            if event.key == pygame.K_r:
                stop = True
                currentNumber = 0
    
    if stop == False:
        currentNumber = incrementTimer(currentNumber)
    
    screen.fill(BLACK)
    
    displayNumber(convertToStr(getTime(currentNumber)))
    
    pygame.display.flip()
 
    clock.tick(100)
 
pygame.quit()


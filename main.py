import pygame
import random
import math
from person import player
from obstacle import rock
from obstacle import zombie
from obstacle import crate
from obstacle import barrel
pygame.init()

win = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("PyTime")

bg = pygame.image.load('pics/bg.jpg')
fem = pygame.image.load('pics/female.png')
adv = pygame.image.load('pics/adv.png')
sold = pygame.image.load('pics/sold.png')

error = pygame.mixer.Sound('sound/error.wav')
pygame.mixer.music.load('sound/back.wav')
pygame.mixer.music.play(-1)



def draw():
    if Start:
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        text = font.render('Press ENTER to start ', 1, (138, 43, 226))
        pers = font1.render('Default', 1, (138, 43, 226))
        pers1 = font1.render('Press 1', 1, (138, 43, 226))
        pers2 = font1.render('Press 2', 1, (138, 43, 226))

        win.blit(fem, (220, 300))
        win.blit(adv, (470, 300))
        win.blit(sold, (710, 300))

        win.blit(text, (255, 150))
        win.blit(pers, (205, 420))
        win.blit(pers1, (460, 420))
        win.blit(pers2, (700, 420))

    if End == False and Start == False:
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        man.draw(win)
        text = font.render('Score: ' + str(round(score)), 1, (138, 43, 226))
        win.blit(text, (0, 0))
    
        for obstacle in obstacles:
            obstacle.draw(win)

    if End and Start == False:
        text = font.render('Your score is: ' + str(round(score)), 1, (138, 43, 226))
        text1 = font.render('Press ENTER to play again ', 1, (138, 43, 226))
        win.blit(text, (300, 150))
        win.blit(text1, (220, 300))
        
    pygame.display.update()

    
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT+1, random.randrange(1800, 2200))
pygame.time.set_timer(pygame.USEREVENT+2, random.randrange(1500, 2000))
pygame.time.set_timer(pygame.USEREVENT+3, random.randrange(1000, 1500))
pygame.time.set_timer(pygame.USEREVENT+4, random.randrange(500, 1000))
pygame.time.set_timer(pygame.USEREVENT+5, random.randrange(400, 700))
font = pygame.font.SysFont('comicsans', 60, True)
font1 = pygame.font.SysFont('comicsans', 40, True)
score = 0
obstacles = []
bg1 = 4
bgX = 0
n = 0
bgX2 = bg.get_width()
Start = True
run = True
End = False
man = player(200, 385, 80, 110)
while run:
    clock.tick(120)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if Start == False:
            if score < 100:
                if event.type == pygame.USEREVENT + 1:
                    r = random.randrange(0, 4)
                    if r == 0:
                        obstacles.append(rock(1000, 430, 64, 64))
                    if r == 1:
                        obstacles.append(zombie(1000, 395, 64, 64))
                    if r == 2:
                        obstacles.append(crate(1000, 440, 64, 64))
                    if r == 3:
                        obstacles.append(barrel(1000, 440, 64, 64))


        if score > 100 and score < 250:
            bg1 = 6
            if event.type == pygame.USEREVENT + 2:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1000, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1000, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1000, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1000, 440, 64, 64))

        if score > 250 and score < 350:
            bg1 = 8
            if event.type == pygame.USEREVENT + 3:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1000, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1000, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1000, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1000, 440, 64, 64))

        if score > 350:
            bg1 = 10
            if event.type == pygame.USEREVENT + 4:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1000, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1000, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1000, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1000, 440, 64, 64))

        if score > 500:
            bg1 = 15
            if event.type == pygame.USEREVENT + 5:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1000, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1000, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1000, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1000, 440, 64, 64))

    bgX -= bg1
    bgX2 -= bg1
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    if Start == False and End == False:
        score += 1 * 0.1

    if End == False:
        for obstacle in obstacles:
            if obstacle.collide(man.hitbox):
                error.play()
                End = True
            obstacle.x -= bg1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        man.jump = True
    if keys[pygame.K_RETURN]:
        Start = False
    if keys[pygame.K_ESCAPE]:
        run = False

    if Start:
        if keys[pygame.K_1]:
            man.switch = True
            n = 1
        if keys[pygame.K_2]:
            man.switch2 = True
            n = 2

    if n == 1:
        man.switch = True
    if n == 2:
        man.switch2 = True


    if End:
        if keys[pygame.K_RETURN]:
            man = player(200, 385, 80, 110)
            score = 0
            bg1 = 4
            obstacles = []
            End = False
        
    draw()
pygame.quit()
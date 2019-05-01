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

error = pygame.mixer.Sound('sound/error.wav')
pygame.mixer.music.load('sound/back.wav')
pygame.mixer.music.play(-1)



def draw():
    if Start:
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        text = font.render('Press ENTER to start ', 1, (138, 43, 226))
        win.blit(text, (255, 255))

    if End == False and Start == False:
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
        man.draw(win)
        text = font.render('Score: ' + str(round(score)), 1, (138, 43, 226))
        win.blit(text, (0, 0))
    
        for obstacle in obstacles:
            obstacle.draw(win)

    if End and Start == False:
        win.blit(bg, (bgX, 0))
        win.blit(bg, (bgX2, 0))
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
font = pygame.font.SysFont('comicsans', 60, True)
score = 0
obstacles = []
bg1 = 4
bgX = 0
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

        if score < 100:
            if event.type == pygame.USEREVENT + 1:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1024, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1024, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1024, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1024, 440, 64, 64))


        if score > 100 and score < 250:
            bg1 = 6
            if event.type == pygame.USEREVENT + 2:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1024, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1024, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1024, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1024, 440, 64, 64))

        if score > 250 and score < 350:
            bg1 = 8
            if event.type == pygame.USEREVENT + 3:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1024, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1024, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1024, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1024, 440, 64, 64))

        if score > 350:
            bg1 = 10
            if event.type == pygame.USEREVENT + 4:
                r = random.randrange(0, 4)
                if r == 0:
                    obstacles.append(rock(1024, 430, 64, 64))
                if r == 1:
                    obstacles.append(zombie(1024, 395, 64, 64))
                if r == 2:
                    obstacles.append(crate(1024, 440, 64, 64))
                if r == 3:
                    obstacles.append(barrel(1024, 440, 64, 64))

    bgX -= bg1
    bgX2 -= bg1
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    if End == False:
        score += 1 * 0.1
        for obstacle in obstacles:
            if obstacle.collide(man.hitbox):
                error.play()
                End = True

            obstacle.x -= bg1
            if obstacle.x < obstacle.width * -1:
                obstacles.pop(obstacles.index(obstacle))


    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN]:
        pygame.time.delay(10)
    if keys[pygame.K_SPACE]:
        man.jump = True
    if keys[pygame.K_RETURN]:
        Start = False
    if keys[pygame.K_ESCAPE]:
        run = False

    if End:
        if keys[pygame.K_RETURN]:
            man = player(200, 385, 80, 110)
            score = 0
            bg1 = 4
            obstacles = []
            End = False
        
    draw()
pygame.quit()
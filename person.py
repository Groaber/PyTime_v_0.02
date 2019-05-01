import pygame
pygame.init()


class player(object):
    left1 = [pygame.image.load('pics/walk2.png'), pygame.image.load('pics/walk1.png')]
    jump1 = pygame.image.load('pics/jump.png')
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.jump = False
        self.left = True
        self.switch = False
        self.switch2 = False
        self.first = True
        self.walkCount = 0
        self.jumpCount = 25
        self.hitbox = (self.x + 5, self.y + 10, self.width - 10, self.height - 20)

    def move(self):
        if self.jump:
            self.left = False
            if self.jumpCount >= -25:
                self.y -= self.jumpCount / 2
                self.jumpCount -= 1
            else:
                self.jumpCount = 25
                self.jump = False
                self.left = True


    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 60:
            self.walkCount = 0

        if self.left:
            win.blit(self.left1[self.walkCount // 30], (self.x, self.y))
            self.walkCount += 1

        if self.jump:
            win.blit(self.jump1, (self.x, self.y))

        if self.switch:
            self.left1 = [pygame.image.load('pics/walk_2.png'), pygame.image.load('pics/walk_1.png')]
            self.jump1 = pygame.image.load('pics/jump1.png')

        if self.switch2:
            self.left1 = [pygame.image.load('pics/walk2_2.png'), pygame.image.load('pics/walk1_1.png')]
            self.jump1 = pygame.image.load('pics/jump2.png')

        self.hitbox = (self.x + 5, self.y + 10, self.width - 10, self.height - 20)


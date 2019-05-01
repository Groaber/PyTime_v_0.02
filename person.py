import pygame
pygame.init()

left = [pygame.image.load('pics/walk2.png'), pygame.image.load('pics/walk1.png')]
jump = pygame.image.load('pics/jump.png')

class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.jump = False
        self.left = True
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
            win.blit(left[self.walkCount // 30], (self.x, self.y))
            self.walkCount += 1

        if self.jump:
            win.blit(jump, (self.x, self.y))

        self.hitbox = (self.x + 5, self.y + 10, self.width - 10, self.height - 20)

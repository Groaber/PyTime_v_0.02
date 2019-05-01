import pygame
pygame.init()

rock1 = pygame.image.load('pics/rock.png')
zombie1 = pygame.image.load('pics/zstand.png')
crate1 = pygame.image.load('pics/crate.png')
barrel1 = pygame.image.load('pics/barrel.png')

class rock(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = 1.4
        self.hitbox = (self.x, self.y, self.width, self.height)

    def draw(self, win):
        win.blit(pygame.transform.scale(rock1, (64, 64)), (self.x, self.y))
        self.hitbox = (self.x + 5, self.y + 5, self.width - 10, self.height)

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class zombie(rock):
    def draw(self,win):
        self.hitbox = (self.x + 18, self.y + 23, self.width - 18, self.height)
        win.blit(zombie1, (self.x,self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class crate(rock):
    def draw(self,win):
        self.hitbox = (self.x + 2, self.y + 2, self.width - 10, self.height)
        win.blit(pygame.transform.scale(crate1, (60, 60)), (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

class barrel(rock):
    def draw(self,win):
        self.hitbox = (self.x, self.y, self.width - 25, self.height - 5)
        win.blit(pygame.transform.scale(barrel1, (42, 64)), (self.x, self.y))


    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

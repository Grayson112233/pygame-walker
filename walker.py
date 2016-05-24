import pygame
import globals
import random

class Walker():

    def __init__(self, x=0, y=0, color=None):

        self.x = x
        self.y = y

        if(color == None):
            self.color = (0, 0, 0)
        else:
            self.color = color

    def update(self):
        rand = random.randint(0, 3)
        if rand == 0:
            self.x += 1
        elif rand == 1:
            self.x -= 1
        elif rand == 2:
            self.y += 1
        elif rand == 3:
            self.y -= 1

    def draw(self):
        pygame.draw.rect(globals.window, self.color, pygame.Rect(self.x, self.y, 2, 2))
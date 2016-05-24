# Random walker program by Grayson Pike
# Originally written December 2014
# Rewritten May 2016
# No controls, press escape to close window

import sys
import pygame
import random
import globals
from walker import Walker

globals.WIDTH = 600
globals.HEIGHT = 600

BACKGROUND_COLOR = (255, 255, 255)
NUM_WALKERS = 20
RANDOM_COLORS = True # If true, walkers will be assigned random colors, otherwise they will default to black

def main():

    # Initialize pygame
    pygame.init()
    clock = pygame.time.Clock()
    globals.window = pygame.display.set_mode((globals.WIDTH, globals.HEIGHT), False)
    globals.window.fill(BACKGROUND_COLOR)

    loop = True

    # Create the walkers
    walkers = []
    for i in range(NUM_WALKERS):
        if RANDOM_COLORS:
            color = (random.randint(0, 255), random.randint(0, 150), random.randint(100, 255))
        else:
            color = (0, 0, 0) # Default to black if no random colors
        walkers.append(Walker(globals.WIDTH / 2, globals.HEIGHT / 2, color))

    while(loop):

        clock.tick(60)

        for i in range(len(walkers)):
            walkers[i].update()
            walkers[i].draw()

        # Check if the escape key has been pressed
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        pygame.display.flip()


main()

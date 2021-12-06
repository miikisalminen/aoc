# This program was not made with speed in mind, rather
# the visual aspect of seeing how a recursive backtracking
# algorithm works.

import pygame
import numpy as np
import time

lines = []
tmp = []

pygame.init()
pygame.display.set_caption("Advent of Code Day 5 Visualisation")

screen = pygame.display.set_mode((1200,1000))

running = True
setup = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while(setup):	# General setup, drawing grids
        screen.blit(pygame.image.load("ocean_bg.png"), (0,0))
        f = open("input.txt", "r")
        for x in f:
            for y in x.strip().split(" -> "):
                tmp.append((int(y.split(",")[0]),int(y.split(",")[1])))
                if len(tmp) == 2:
                    lines.append(tmp)
                    tmp = []
        for line in lines:
            print(line)
            pygame.draw.line(screen,(255,0,0),(line[0][0]+200,line[0][1]),(line[1][0]+200,line[1][1]),(1))	
            pygame.display.update()
            time.sleep(0.005)

        setup = False # End the setup loop
pygame.quit()
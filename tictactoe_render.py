#!/usr/bin/python3
import re
import pygame, sys
import numpy as np

pygame.init()
zz = np.array([12, 3])

screen = pygame.display.set_mode((640, 480))

#cross = pygame.image.load("cross")
#oh = pygame.image.load("oh")
def render_grid(surface):
	pygame.draw.line(surface, white, )


def render_board(string_state):
	xes = [i.start() for i in re.finditer("x", strinf_state)]
	ohs = [i.start() for i in re.finditer("o", strinf_state)]


	

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	screen.fill((0,0,0))
	render_grid()


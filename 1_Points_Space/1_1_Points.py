__author__ = 'gollahalli'

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

data = open('mapping.txt', 'r')
vertices = tuple(tuple(int(j) for j in i.split()) for i in data.readlines())


def cube():
	glBegin(GL_POINTS)

	for vertex in vertices:
		glVertex3fv(vertex)

	glEnd()


def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
	gluPerspective(50, (display[0]/display[1]), 5, 500.0)  # field of view in y-axis, aspect ratio, viewer to near
	# clipping angle and far clipping angle
	glTranslatef(0.0, 0.0, -350)  # translate against x-axis, y-axis and z-axis
	glRotatef(0, 0, 0, 0)
	glPointSize(3.0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		(x, y) = pygame.mouse.get_pos()
		glRotatef(10, x, y, 0)   # angel, x-axis, y-axis and z-axis
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		cube()
		pygame.display.flip()
		pygame.time.wait(10)

main()

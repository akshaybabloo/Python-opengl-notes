__author__ = 'gollahalli'

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
	(-30, 50, 30),
	(-50, 30, 0),
	(-40, 30, 40),
	(-60, 0, 30),
	(-60, 20, 0),
	(-60, -60, 0),
	(-30, -80, 10),
	(30, -80, 10),
	(60, -60, 0),
	(60, 20, 0),
	(60, 0, 30),
	(40, 30, 40),
	(50, 30, 0),
	(30, 50, 30),
	(-60, -60, 0),
	(-60, -60, 10),
	(-60, -60, 20),
	(-60, -60, 30),
	(-60, -50, -10),
	(-60, -50, 0),
	(-60, -50, 10),
	(-60, -50, 20),
	(-60, -50, 30),
	(-60, -40, -10),
	(-60, -40, 0),
	(-60, -40, 10),
	(-60, -40, 20),
	(-60, -40, 30),
	(-60, -40, 40),
	(-60, -30, -10),
	(-60, -30, 0),
	(-60, -30, 10),
	(-60, -30, 20),
	(-60, -30, 30),
	(-60, -30, 40),
	(-60, -20, -20),
	(-60, -20, -10),
	(-60, -20, 0),
	(-60, -20, 10),
	(-60, -20, 20),
	(-60, -20, 30),
	(-60, -20, 40),
	(-60, -10, -20),
	(-60, -10, -10),
	(-60, -10, 0),
	(-60, -10, 10),
	(-60, -10, 20),
	(-60, -10, 30),
	(-60, -10, 40),
	(-60, 0, -20),
	(-60, 0, -10),
	(-60, 0, 0),
	(-60, 0, 10),
	(-60, 0, 20),
	(-60, 0, 30),
	(-60, 10, -10),
	(-60, 10, 0),
	(-60, 10, 10),
	(-60, 10, 20),
	(-60, 10, 30),
	(-60, 20, -10),
	(-60, 20, 0),
	(-60, 20, 10),
	(-60, 20, 20),
	(-60, 30, 0),
	(-50, -80, -30),
	(-50, -80, -20),
	(-50, -80, 0),
	(-50, -80, 10),
	(-50, -70, -40),
	(-50, -70, -30),
	(-50, -70, -20),
	(-50, -70, -10),
	(-50, -70, 0),
	(-50, -70, 10),
	(-50, -70, 20),
	(-50, -70, 30),
	(-50, -60, -40),
	(-50, -60, -30),
	(-50, -60, -20),
	(-50, -60, -10),
	(-50, -60, 0),
	(-50, -60, 10),
	(-50, -60, 20),
	(-50, -60, 30),
	(-50, -60, 40),
	(-50, -50, -30),
	(-50, -50, -20),
	(-50, -50, -10),
	(-50, -50, 0),
	(-50, -50, 10),
	(-50, -50, 20),
	(-50, -50, 30),
	(-50, -50, 40),
	(-50, -50, 50),
	(-50, -40, -20),
	(-50, -40, -10),
	(-50, -40, 0),
	(-50, -40, 10),
	(-50, -40, 20),
	(-50, -40, 30),
	(-50, -40, 40),
	(-50, -40, 50),
	(-50, -30, -20),
	(-50, -30, -10),
	(-50, -30, 0),
	(-50, -30, 10),
	(-50, -30, 20),
	(-50, -30, 30),
	(-50, -30, 40),
	(-50, -30, 50),
	(-50, -20, -30),
	(-50, -20, -20),
	(-50, -20, -10),
	(-50, -20, 0),
	(-50, -20, 10),
	(-50, -20, 20),
	(-50, -20, 30),
	(-50, -20, 40),
	(-50, -20, 50),
	(-50, -10, -30),
	(-50, -10, -20),
	(-50, -10, -10),
	(-50, -10, 0),
	(-50, -10, 10),
	(-50, -10, 20),
	(-50, -10, 30),
	(-50, -10, 40),
	(-50, -10, 50),
	(-50, 0, -30),
	(-50, 0, -20),
	(-50, 0, -10),
	(-50, 0, 0),
	(-50, 0, 10),
	(-50, 0, 20),
	(-50, 0, 30),
	(-50, 0, 40),
	(-50, 0, 50),
	(-50, 10, -30),
	(-50, 10, -20),
	(-50, 10, -10),
	(-50, 10, 0),
	(-50, 10, 10),
	(-50, 10, 20),
	(-50, 10, 30),
	(-50, 10, 40),
	(-50, 10, 50),
	(-50, 20, -20),
	(-50, 20, -10),
	(-50, 20, 0),
	(-50, 20, 10),
	(-50, 20, 20),
	(-50, 20, 30),
	(-50, 20, 40),
	(-50, 30, -10),
	(-50, 30, 0),
	(-50, 30, 10),
	(-50, 30, 20),
	(-50, 30, 30),
	(-50, 40, -10),
	(-50, 40, 0),
	(-50, 40, 10),
	(-50, 40, 20),
	(-50, 50, -10),
	(-50, 50, 0),
	(-50, 50, 10),
	(-40, -80, -40),
	(-40, -80, -30),
	(-40, -80, -20),
	(-40, -80, -10),
	(-40, -80, 0),
	(-40, -80, 10),
	(-40, -80, 20),
	(-40, -80, 30),
	(-40, -70, -40),
	(-40, -70, -30),
	(-40, -70, -20),
	(-40, -70, -10),
	(-40, -70, 0),
	(-40, -70, 10),
	(-40, -70, 20),
	(-40, -70, 30),
	(-40, -70, 40),
	(-40, -60, -40),
	(-40, -60, -30),
	(-40, -60, -20),
	(-40, -60, -10),
	(-40, -60, 0),
	(-40, -60, 10),
	(-40, -60, 20),
	(-40, -60, 30),
	(-40, -60, 40),
	(-40, -60, 50),
	(-40, -50, -40),
	(-40, -50, -30),
	(-40, -50, -20),
	(-40, -50, -10),
	(-40, -50, 0),
	(-40, -50, 10),
	(-40, -50, 20),
	(-40, -50, 30),
	(-40, -50, 40),
	(-40, -50, 50),
	(-40, -40, -30),
	(-40, -40, -20),
	(-40, -40, -10),
	(-40, -40, 0),
	(-40, -40, 10),
	(-40, -40, 20),
	(-40, -40, 30),
	(-40, -40, 40),
	(-40, -40, 50),
	(-40, -40, 60),
	(-40, -30, -20),
	(-40, -30, -10),
	(-40, -30, 0),
	(-40, -30, 10),
	(-40, -30, 20),
	(-40, -30, 30),
	(-40, -30, 40),
	(-40, -30, 50),
	(-40, -30, 60),
	(-40, -20, -30),
	(-40, -20, -20),
	(-40, -20, -10),
	(-40, -20, 0),
	(-40, -20, 10),
	(-40, -20, 20),
	(-40, -20, 30),
	(-40, -20, 40),
	(-40, -20, 50),
	(-40, -20, 60),
	(-40, -10, -30),
	(-40, -10, -20),
	(-40, -10, -10),
	(-40, -10, 0),
	(-40, -10, 10),
	(-40, -10, 20),
	(-40, -10, 30),
	(-40, -10, 40),
	(-40, -10, 50),
	(-40, -10, 60),
	(-40, 0, -30),
	(-40, 0, -20),
	(-40, 0, -10),
	(-40, 0, 0),
	(-40, 0, 10),
	(-40, 0, 20),
	(-40, 0, 30),
	(-40, 0, 40),
	(-40, 0, 50),
	(-40, 10, -30),
	(-40, 10, -20),
	(-40, 10, -10),
	(-40, 10, 0),
	(-40, 10, 10),
	(-40, 10, 20),
	(-40, 10, 30),
	(-40, 10, 40),
	(-40, 10, 50),
	(-40, 20, -30),
	(-40, 20, -10),
	(-40, 20, 0),
	(-40, 20, 10),
	(-40, 20, 20),
	(-40, 20, 30),
	(-40, 20, 40),
	(-40, 20, 50),
	(-40, 30, -10),
	(-40, 30, 0),
	(-40, 30, 10),
	(-40, 30, 20),
	(-40, 30, 30),
	(-40, 30, 40),
	(-40, 40, -10),
	(-40, 40, 0),
	(-40, 40, 10),
	(-40, 40, 20),
	(-40, 40, 30),
	(-40, 50, -10),
	(-40, 50, 0),
	(-40, 50, 10),
	(-40, 50, 20),
	(-40, 60, 0),
	(-40, 60, 10),
	(-30, -80, -40),
	(-30, -80, -30),
	(-30, -80, -20),
	(-30, -80, -10),
	(-30, -80, 0),
	(-30, -80, 10),
	(-30, -80, 20),
	(-30, -80, 30),
	(-30, -80, 40),
	(-30, -70, -40),
	(-30, -70, -30),
	(-30, -70, -20),
	(-30, -70, -10),
	(-30, -70, 0),
	(-30, -70, 10),
	(-30, -70, 20),
	(-30, -70, 30),
	(-30, -70, 40),
	(-30, -60, -40),
	(-30, -60, -30),
	(-30, -60, -20),
	(-30, -60, -10),
	(-30, -60, 0),
	(-30, -60, 10),
	(-30, -60, 20),
	(-30, -60, 30),
	(-30, -60, 40),
	(-30, -60, 50),
	(-30, -50, -40),
	(-30, -50, -30),
	(-30, -50, -20),
	(-30, -50, -10),
	(-30, -50, 0),
	(-30, -50, 10),
	(-30, -50, 20),
	(-30, -50, 30),
	(-30, -50, 40),
	(-30, -50, 50),
	(-30, -50, 60),
	(-30, -40, -40),
	(-30, -40, -30),
	(-30, -40, -20),
	(-30, -40, -10),
	(-30, -40, 0),
	(-30, -40, 10),
	(-30, -40, 20),
	(-30, -40, 30),
	(-30, -40, 40),
	(-30, -40, 50),
	(-30, -40, 60),
	(-30, -30, -20),
	(-30, -30, -10),
	(-30, -30, 0),
	(-30, -30, 10),
	(-30, -30, 20),
	(-30, -30, 30),
	(-30, -30, 40),
	(-30, -30, 50),
	(-30, -30, 60),
	(-30, -20, -20),
	(-30, -20, -10),
	(-30, -20, 0),
	(-30, -20, 10),
	(-30, -20, 20),
	(-30, -20, 30),
	(-30, -20, 40),
	(-30, -20, 50),
	(-30, -20, 60),
	(-30, -10, -30),
	(-30, -10, -20),
	(-30, -10, -10),
	(-30, -10, 0),
	(-30, -10, 10),
	(-30, -10, 20),
	(-30, -10, 30),
	(-30, -10, 40),
	(-30, -10, 50),
	(-30, -10, 60),
	(-30, 0, -40),
	(-30, 0, -30),
	(-30, 0, -20),
	(-30, 0, -10),
	(-30, 0, 0),
	(-30, 0, 10),
	(-30, 0, 20),
	(-30, 0, 30),
	(-30, 0, 40),
	(-30, 0, 50),
	(-30, 0, 60),
	(-30, 10, -30),
	(-30, 10, -20),
	(-30, 10, -10),
	(-30, 10, 0),
	(-30, 10, 10),
	(-30, 10, 20),
	(-30, 10, 30),
	(-30, 10, 40),
	(-30, 10, 50),
	(-30, 10, 60),
	(-30, 20, -20),
	(-30, 20, -10),
	(-30, 20, 0),
	(-30, 20, 10),
	(-30, 20, 20),
	(-30, 20, 30),
	(-30, 20, 40),
	(-30, 20, 50),
	(-30, 30, -10),
	(-30, 30, 0),
	(-30, 30, 10),
	(-30, 30, 20),
	(-30, 30, 30),
	(-30, 30, 40),
	(-30, 30, 50),
	(-30, 40, -10),
	(-30, 40, 0),
	(-30, 40, 10),
	(-30, 40, 20),
	(-30, 40, 30),
	(-30, 40, 40),
	(-30, 50, -10),
	(-30, 50, 0),
	(-30, 50, 10),
	(-30, 50, 20),
	(-30, 50, 30),
	(-30, 60, -10),
	(-30, 60, 0),
	(-30, 60, 10),
	(-30, 60, 20),
	(-20, -80, -30),
	(-20, -80, -20),
	(-20, -80, -10),
	(-20, -80, 0),
	(-20, -80, 10),
	(-20, -80, 20),
	(-20, -80, 30),
	(-20, -80, 40),
	(-20, -70, -40),
	(-20, -70, -30),
	(-20, -70, -20),
	(-20, -70, -10),
	(-20, -70, 0),
	(-20, -70, 10),
	(-20, -70, 20),
	(-20, -70, 30),
	(-20, -70, 40),
	(-20, -70, 50),
	(-20, -60, -40),
	(-20, -60, -30),
	(-20, -60, -20),
	(-20, -60, -10),
	(-20, -60, 0),
	(-20, -60, 10),
	(-20, -60, 20),
	(-20, -60, 30),
	(-20, -60, 40),
	(-20, -60, 50),
	(-20, -60, 60),
	(-20, -50, -40),
	(-20, -50, -30),
	(-20, -50, -20),
	(-20, -50, -10),
	(-20, -50, 0),
	(-20, -50, 10),
	(-20, -50, 20),
	(-20, -50, 30),
	(-20, -50, 40),
	(-20, -50, 50),
	(-20, -50, 60),
	(-20, -40, -40),
	(-20, -40, -30),
	(-20, -40, -20),
	(-20, -40, -10),
	(-20, -40, 0),
	(-20, -40, 10),
	(-20, -40, 20),
	(-20, -40, 30),
	(-20, -40, 40),
	(-20, -40, 50),
	(-20, -40, 60),
	(-20, -30, -30),
	(-20, -30, -20),
	(-20, -30, -10),
	(-20, -30, 0),
	(-20, -30, 10),
	(-20, -30, 20),
	(-20, -30, 30),
	(-20, -30, 40),
	(-20, -30, 50),
	(-20, -30, 60),
	(-20, -20, -10),
	(-20, -20, 0),
	(-20, -20, 10),
	(-20, -20, 20),
	(-20, -20, 30),
	(-20, -20, 40),
	(-20, -20, 50),
	(-20, -20, 60),
	(-20, -10, -30),
	(-20, -10, -20),
	(-20, -10, -10),
	(-20, -10, 0),
	(-20, -10, 10),
	(-20, -10, 20),
	(-20, -10, 30),
	(-20, -10, 40),
	(-20, -10, 50),
	(-20, -10, 60),
	(-20, 0, -30),
	(-20, 0, -20),
	(-20, 0, -10),
	(-20, 0, 0),
	(-20, 0, 10),
	(-20, 0, 20),
	(-20, 0, 30),
	(-20, 0, 40),
	(-20, 0, 50),
	(-20, 0, 60),
	(-20, 10, -10),
	(-20, 10, 0),
	(-20, 10, 10),
	(-20, 10, 20),
	(-20, 10, 30),
	(-20, 10, 40),
	(-20, 10, 50),
	(-20, 10, 60),
	(-20, 20, -20),
	(-20, 20, -10),
	(-20, 20, 0),
	(-20, 20, 10),
	(-20, 20, 20),
	(-20, 20, 30),
	(-20, 20, 40),
	(-20, 20, 50),
	(-20, 20, 60),
	(-20, 30, -20),
	(-20, 30, -10),
	(-20, 30, 0),
	(-20, 30, 10),
	(-20, 30, 20),
	(-20, 30, 30),
	(-20, 30, 40),
	(-20, 30, 50),
	(-20, 40, -20),
	(-20, 40, -10),
	(-20, 40, 0),
	(-20, 40, 10),
	(-20, 40, 20),
	(-20, 40, 30),
	(-20, 40, 40),
	(-20, 50, -20),
	(-20, 50, -10),
	(-20, 50, 0),
	(-20, 50, 10),
	(-20, 50, 20),
	(-20, 50, 30),
	(-20, 50, 40),
	(-20, 60, -20),
	(-20, 60, -10),
	(-20, 60, 0),
	(-20, 60, 10),
	(-20, 60, 20),
	(-10, -80, -30),
	(-10, -80, -20),
	(-10, -80, -10),
	(-10, -80, 0),
	(-10, -80, 10),
	(-10, -80, 20),
	(-10, -80, 30),
	(-10, -80, 40),
	(-10, -70, -40),
	(-10, -70, -30),
	(-10, -70, -20),
	(-10, -70, -10),
	(-10, -70, 0),
	(-10, -70, 10),
	(-10, -70, 20),
	(-10, -70, 30),
	(-10, -70, 40),
	(-10, -70, 50),
	(-10, -60, -40),
	(-10, -60, -30),
	(-10, -60, -20),
	(-10, -60, -10),
	(-10, -60, 0),
	(-10, -60, 10),
	(-10, -60, 20),
	(-10, -60, 30),
	(-10, -60, 40),
	(-10, -60, 50),
	(-10, -60, 60),
	(-10, -50, -40),
	(-10, -50, -30),
	(-10, -50, -20),
	(-10, -50, -10),
	(-10, -50, 0),
	(-10, -50, 10),
	(-10, -50, 20),
	(-10, -50, 30),
	(-10, -50, 40),
	(-10, -50, 50),
	(-10, -50, 60),
	(-10, -40, -30),
	(-10, -40, -20),
	(-10, -40, -10),
	(-10, -40, 0),
	(-10, -40, 10),
	(-10, -40, 20),
	(-10, -40, 30),
	(-10, -40, 40),
	(-10, -40, 50),
	(-10, -40, 60),
	(-10, -30, -30),
	(-10, -30, -20),
	(-10, -30, -10),
	(-10, -30, 10),
	(-10, -30, 20),
	(-10, -30, 30),
	(-10, -30, 40),
	(-10, -30, 50),
	(-10, -30, 60),
	(-10, -20, -30),
	(-10, -20, -20),
	(-10, -20, -10),
	(-10, -20, 0),
	(-10, -20, 10),
	(-10, -20, 20),
	(-10, -20, 30),
	(-10, -20, 40),
	(-10, -20, 50),
	(-10, -20, 60),
	(-10, -10, -10),
	(-10, -10, 0),
	(-10, -10, 10),
	(-10, -10, 20),
	(-10, -10, 30),
	(-10, -10, 40),
	(-10, -10, 50),
	(-10, -10, 60),
	(-10, 0, -10),
	(-10, 0, 0),
	(-10, 0, 10),
	(-10, 0, 20),
	(-10, 0, 30),
	(-10, 0, 40),
	(-10, 0, 50),
	(-10, 0, 60),
	(-10, 10, -10),
	(-10, 10, 0),
	(-10, 10, 10),
	(-10, 10, 20),
	(-10, 10, 30),
	(-10, 10, 40),
	(-10, 10, 50),
	(-10, 10, 60),
	(-10, 20, -20),
	(-10, 20, -10),
	(-10, 20, 0),
	(-10, 20, 10),
	(-10, 20, 20),
	(-10, 20, 30),
	(-10, 20, 40),
	(-10, 20, 50),
	(-10, 20, 60),
	(-10, 30, -20),
	(-10, 30, -10),
	(-10, 30, 0),
	(-10, 30, 10),
	(-10, 30, 20),
	(-10, 30, 30),
	(-10, 30, 40),
	(-10, 30, 50),
	(-10, 40, -30),
	(-10, 40, -20),
	(-10, 40, -10),
	(-10, 40, 0),
	(-10, 40, 10),
	(-10, 40, 20),
	(-10, 40, 30),
	(-10, 40, 40),
	(-10, 40, 50),
	(-10, 50, -20),
	(-10, 50, -10),
	(-10, 50, 0),
	(-10, 50, 10),
	(-10, 50, 20),
	(-10, 50, 30),
	(-10, 50, 40),
	(-10, 60, -20),
	(-10, 60, -10),
	(-10, 60, 0),
	(-10, 60, 10),
	(-10, 60, 20),
	(-10, 60, 30),
	(0, -80, -30),
	(0, -80, -20),
	(0, -80, 0),
	(0, -80, 10),
	(0, -80, 20),
	(0, -80, 30),
	(0, -80, 40),
	(0, -70, -30),
	(0, -70, -20),
	(0, -70, -10),
	(0, -70, 0),
	(0, -70, 10),
	(0, -70, 20),
	(0, -70, 30),
	(0, -70, 40),
	(0, -70, 50),
	(0, -60, -30),
	(0, -60, -20),
	(0, -60, -10),
	(0, -60, 0),
	(0, -60, 10),
	(0, -60, 20),
	(0, -60, 30),
	(0, -60, 40),
	(0, -60, 50),
	(0, -60, 60),
	(0, -50, -30),
	(0, -50, -20),
	(0, -50, -10),
	(0, -50, 0),
	(0, -50, 10),
	(0, -50, 20),
	(0, -50, 30),
	(0, -50, 40),
	(0, -50, 50),
	(0, -50, 60),
	(0, -40, -40),
	(0, -40, -30),
	(0, -40, -20),
	(0, -40, -10),
	(0, -40, 10),
	(0, -40, 20),
	(0, -40, 30),
	(0, -40, 40),
	(0, -40, 50),
	(0, -40, 60),
	(0, -30, -30),
	(0, -30, -20),
	(0, -30, -10),
	(0, -30, 0),
	(0, -30, 10),
	(0, -30, 20),
	(0, -30, 30),
	(0, -30, 40),
	(0, -30, 50),
	(0, -30, 60),
	(0, -20, -30),
	(0, -20, -20),
	(0, -20, -10),
	(0, -20, 0),
	(0, -20, 10),
	(0, -20, 20),
	(0, -20, 30),
	(0, -20, 40),
	(0, -20, 50),
	(0, -20, 60),
	(0, -10, -10),
	(0, -10, 0),
	(0, -10, 10),
	(0, -10, 20),
	(0, -10, 30),
	(0, -10, 40),
	(0, -10, 50),
	(0, -10, 60),
	(0, 0, -10),
	(0, 0, 0),
	(0, 0, 10),
	(0, 0, 20),
	(0, 0, 30),
	(0, 0, 40),
	(0, 0, 50),
	(0, 0, 60),
	(0, 10, -10),
	(0, 10, 0),
	(0, 10, 10),
	(0, 10, 20),
	(0, 10, 30),
	(0, 10, 40),
	(0, 10, 50),
	(0, 10, 60),
	(0, 20, -20),
	(0, 20, -10),
	(0, 20, 0),
	(0, 20, 10),
	(0, 20, 20),
	(0, 20, 30),
	(0, 20, 40),
	(0, 20, 50),
	(0, 20, 60),
	(0, 30, -20),
	(0, 30, -10),
	(0, 30, 0),
	(0, 30, 10),
	(0, 30, 20),
	(0, 30, 30),
	(0, 30, 40),
	(0, 30, 50),
	(0, 40, -30),
	(0, 40, -20),
	(0, 40, -10),
	(0, 40, 0),
	(0, 40, 10),
	(0, 40, 20),
	(0, 40, 30),
	(0, 40, 40),
	(0, 40, 50),
	(0, 50, -20),
	(0, 50, -10),
	(0, 50, 0),
	(0, 50, 10),
	(0, 50, 20),
	(0, 50, 30),
	(0, 50, 40),
	(0, 60, -20),
	(0, 60, -10),
	(0, 60, 0),
	(0, 60, 10),
	(0, 60, 20),
	(0, 60, 30),
	(10, -80, -30),
	(10, -80, -20),
	(10, -80, -10),
	(10, -80, 0),
	(10, -80, 10),
	(10, -80, 20),
	(10, -80, 30),
	(10, -80, 40),
	(10, -70, -40),
	(10, -70, -30),
	(10, -70, -20),
	(10, -70, -10),
	(10, -70, 0),
	(10, -70, 10),
	(10, -70, 20),
	(10, -70, 30),
	(10, -70, 40),
	(10, -70, 50),
	(10, -60, -40),
	(10, -60, -30),
	(10, -60, -20),
	(10, -60, -10),
	(10, -60, 0),
	(10, -60, 10),
	(10, -60, 20),
	(10, -60, 30),
	(10, -60, 40),
	(10, -60, 50),
	(10, -60, 60),
	(10, -50, -40),
	(10, -50, -30),
	(10, -50, -20),
	(10, -50, -10),
	(10, -50, 0),
	(10, -50, 10),
	(10, -50, 20),
	(10, -50, 30),
	(10, -50, 40),
	(10, -50, 50),
	(10, -50, 60),
	(10, -40, -30),
	(10, -40, -20),
	(10, -40, -10),
	(10, -40, 0),
	(10, -40, 10),
	(10, -40, 20),
	(10, -40, 30),
	(10, -40, 40),
	(10, -40, 50),
	(10, -40, 60),
	(10, -30, -30),
	(10, -30, -20),
	(10, -30, -10),
	(10, -30, 10),
	(10, -30, 20),
	(10, -30, 30),
	(10, -30, 40),
	(10, -30, 50),
	(10, -30, 60),
	(10, -20, -30),
	(10, -20, -20),
	(10, -20, -10),
	(10, -20, 0),
	(10, -20, 10),
	(10, -20, 20),
	(10, -20, 30),
	(10, -20, 40),
	(10, -20, 50),
	(10, -20, 60),
	(10, -10, -10),
	(10, -10, 0),
	(10, -10, 10),
	(10, -10, 20),
	(10, -10, 30),
	(10, -10, 40),
	(10, -10, 50),
	(10, -10, 60),
	(10, 0, -10),
	(10, 0, 0),
	(10, 0, 10),
	(10, 0, 20),
	(10, 0, 30),
	(10, 0, 40),
	(10, 0, 50),
	(10, 0, 60),
	(10, 10, -10),
	(10, 10, 0),
	(10, 10, 10),
	(10, 10, 20),
	(10, 10, 30),
	(10, 10, 40),
	(10, 10, 50),
	(10, 10, 60),
	(10, 20, -20),
	(10, 20, -10),
	(10, 20, 0),
	(10, 20, 10),
	(10, 20, 20),
	(10, 20, 30),
	(10, 20, 40),
	(10, 20, 50),
	(10, 20, 60),
	(10, 30, -20),
	(10, 30, -10),
	(10, 30, 0),
	(10, 30, 10),
	(10, 30, 20),
	(10, 30, 30),
	(10, 30, 40),
	(10, 30, 50),
	(10, 40, -30),
	(10, 40, -20),
	(10, 40, -10),
	(10, 40, 0),
	(10, 40, 10),
	(10, 40, 20),
	(10, 40, 30),
	(10, 40, 40),
	(10, 40, 50),
	(10, 50, -20),
	(10, 50, -10),
	(10, 50, 0),
	(10, 50, 10),
	(10, 50, 20),
	(10, 50, 30),
	(10, 50, 40),
	(10, 60, -20),
	(10, 60, -10),
	(10, 60, 0),
	(10, 60, 10),
	(10, 60, 20),
	(10, 60, 30),
	(20, -80, -30),
	(20, -80, -20),
	(20, -80, -10),
	(20, -80, 0),
	(20, -80, 10),
	(20, -80, 20),
	(20, -80, 30),
	(20, -80, 40),
	(20, -70, -40),
	(20, -70, -30),
	(20, -70, -20),
	(20, -70, -10),
	(20, -70, 0),
	(20, -70, 10),
	(20, -70, 20),
	(20, -70, 30),
	(20, -70, 40),
	(20, -70, 50),
	(20, -60, -40),
	(20, -60, -30),
	(20, -60, -20),
	(20, -60, -10),
	(20, -60, 0),
	(20, -60, 10),
	(20, -60, 20),
	(20, -60, 30),
	(20, -60, 40),
	(20, -60, 50),
	(20, -60, 60),
	(20, -50, -40),
	(20, -50, -30),
	(20, -50, -20),
	(20, -50, -10),
	(20, -50, 0),
	(20, -50, 10),
	(20, -50, 20),
	(20, -50, 30),
	(20, -50, 40),
	(20, -50, 50),
	(20, -50, 60),
	(20, -40, -40),
	(20, -40, -30),
	(20, -40, -20),
	(20, -40, -10),
	(20, -40, 0),
	(20, -40, 10),
	(20, -40, 20),
	(20, -40, 30),
	(20, -40, 40),
	(20, -40, 50),
	(20, -40, 60),
	(20, -30, -30),
	(20, -30, -20),
	(20, -30, -10),
	(20, -30, 0),
	(20, -30, 10),
	(20, -30, 20),
	(20, -30, 30),
	(20, -30, 40),
	(20, -30, 50),
	(20, -30, 60),
	(20, -20, -10),
	(20, -20, 0),
	(20, -20, 10),
	(20, -20, 20),
	(20, -20, 30),
	(20, -20, 40),
	(20, -20, 50),
	(20, -20, 60),
	(20, -10, -30),
	(20, -10, -20),
	(20, -10, -10),
	(20, -10, 0),
	(20, -10, 10),
	(20, -10, 20),
	(20, -10, 30),
	(20, -10, 40),
	(20, -10, 50),
	(20, -10, 60),
	(20, 0, -30),
	(20, 0, -20),
	(20, 0, -10),
	(20, 0, 0),
	(20, 0, 10),
	(20, 0, 20),
	(20, 0, 30),
	(20, 0, 40),
	(20, 0, 50),
	(20, 0, 60),
	(20, 10, -10),
	(20, 10, 0),
	(20, 10, 10),
	(20, 10, 20),
	(20, 10, 30),
	(20, 10, 40),
	(20, 10, 50),
	(20, 10, 60),
	(20, 20, -20),
	(20, 20, -10),
	(20, 20, 0),
	(20, 20, 10),
	(20, 20, 20),
	(20, 20, 30),
	(20, 20, 40),
	(20, 20, 50),
	(20, 20, 60),
	(20, 30, -20),
	(20, 30, -10),
	(20, 30, 0),
	(20, 30, 10),
	(20, 30, 20),
	(20, 30, 30),
	(20, 30, 40),
	(20, 30, 50),
	(20, 40, -20),
	(20, 40, -10),
	(20, 40, 0),
	(20, 40, 10),
	(20, 40, 20),
	(20, 40, 30),
	(20, 40, 40),
	(20, 40, 50),
	(20, 50, -20),
	(20, 50, -10),
	(20, 50, 0),
	(20, 50, 10),
	(20, 50, 20),
	(20, 50, 30),
	(20, 50, 40),
	(20, 60, -20),
	(20, 60, -10),
	(20, 60, 0),
	(20, 60, 10),
	(20, 60, 20),
	(30, -80, -40),
	(30, -80, -30),
	(30, -80, -20),
	(30, -80, -10),
	(30, -80, 0),
	(30, -80, 10),
	(30, -80, 20),
	(30, -80, 30),
	(30, -80, 40),
	(30, -70, -40),
	(30, -70, -30),
	(30, -70, -20),
	(30, -70, -10),
	(30, -70, 0),
	(30, -70, 10),
	(30, -70, 20),
	(30, -70, 30),
	(30, -70, 40),
	(30, -70, 50),
	(30, -60, -40),
	(30, -60, -30),
	(30, -60, -20),
	(30, -60, -10),
	(30, -60, 0),
	(30, -60, 10),
	(30, -60, 20),
	(30, -60, 30),
	(30, -60, 40),
	(30, -60, 50),
	(30, -50, -40),
	(30, -50, -30),
	(30, -50, -20),
	(30, -50, -10),
	(30, -50, 0),
	(30, -50, 10),
	(30, -50, 20),
	(30, -50, 30),
	(30, -50, 40),
	(30, -50, 50),
	(30, -50, 60),
	(30, -40, -40),
	(30, -40, -30),
	(30, -40, -20),
	(30, -40, -10),
	(30, -40, 0),
	(30, -40, 10),
	(30, -40, 20),
	(30, -40, 30),
	(30, -40, 40),
	(30, -40, 50),
	(30, -40, 60),
	(30, -30, -10),
	(30, -30, 0),
	(30, -30, 10),
	(30, -30, 20),
	(30, -30, 30),
	(30, -30, 40),
	(30, -30, 50),
	(30, -30, 60),
	(30, -20, -20),
	(30, -20, -10),
	(30, -20, 0),
	(30, -20, 10),
	(30, -20, 20),
	(30, -20, 30),
	(30, -20, 40),
	(30, -20, 50),
	(30, -20, 60),
	(30, -10, -30),
	(30, -10, -20),
	(30, -10, -10),
	(30, -10, 0),
	(30, -10, 10),
	(30, -10, 20),
	(30, -10, 30),
	(30, -10, 40),
	(30, -10, 50),
	(30, -10, 60),
	(30, 0, -40),
	(30, 0, -30),
	(30, 0, -20),
	(30, 0, -10),
	(30, 0, 0),
	(30, 0, 10),
	(30, 0, 20),
	(30, 0, 30),
	(30, 0, 40),
	(30, 0, 50),
	(30, 0, 60),
	(30, 10, -30),
	(30, 10, -20),
	(30, 10, -10),
	(30, 10, 0),
	(30, 10, 10),
	(30, 10, 20),
	(30, 10, 30),
	(30, 10, 40),
	(30, 10, 50),
	(30, 10, 60),
	(30, 20, -20),
	(30, 20, -10),
	(30, 20, 0),
	(30, 20, 10),
	(30, 20, 20),
	(30, 20, 30),
	(30, 20, 40),
	(30, 20, 50),
	(30, 30, -20),
	(30, 30, -10),
	(30, 30, 0),
	(30, 30, 10),
	(30, 30, 20),
	(30, 30, 30),
	(30, 30, 40),
	(30, 30, 50),
	(30, 40, -10),
	(30, 40, 0),
	(30, 40, 10),
	(30, 40, 20),
	(30, 40, 30),
	(30, 40, 40),
	(30, 50, -10),
	(30, 50, 0),
	(30, 50, 10),
	(30, 50, 20),
	(30, 50, 30),
	(30, 60, -10),
	(30, 60, 0),
	(30, 60, 10),
	(30, 60, 20),
	(40, -80, -40),
	(40, -80, -30),
	(40, -80, -20),
	(40, -80, -10),
	(40, -80, 0),
	(40, -80, 10),
	(40, -80, 20),
	(40, -80, 30),
	(40, -70, -40),
	(40, -70, -30),
	(40, -70, -20),
	(40, -70, -10),
	(40, -70, 0),
	(40, -70, 10),
	(40, -70, 20),
	(40, -70, 30),
	(40, -70, 40),
	(40, -60, -40),
	(40, -60, -30),
	(40, -60, -20),
	(40, -60, -10),
	(40, -60, 0),
	(40, -60, 10),
	(40, -60, 20),
	(40, -60, 30),
	(40, -60, 40),
	(40, -60, 50),
	(40, -50, -40),
	(40, -50, -30),
	(40, -50, -20),
	(40, -50, -10),
	(40, -50, 0),
	(40, -50, 10),
	(40, -50, 20),
	(40, -50, 30),
	(40, -50, 40),
	(40, -50, 50),
	(40, -40, -30),
	(40, -40, -10),
	(40, -40, 0),
	(40, -40, 10),
	(40, -40, 20),
	(40, -40, 30),
	(40, -40, 40),
	(40, -40, 50),
	(40, -40, 60),
	(40, -30, -20),
	(40, -30, -10),
	(40, -30, 0),
	(40, -30, 10),
	(40, -30, 20),
	(40, -30, 30),
	(40, -30, 40),
	(40, -30, 50),
	(40, -30, 60),
	(40, -20, -30),
	(40, -20, -20),
	(40, -20, -10),
	(40, -20, 0),
	(40, -20, 10),
	(40, -20, 20),
	(40, -20, 30),
	(40, -20, 40),
	(40, -20, 50),
	(40, -20, 60),
	(40, -10, -30),
	(40, -10, -20),
	(40, -10, -10),
	(40, -10, 0),
	(40, -10, 10),
	(40, -10, 20),
	(40, -10, 30),
	(40, -10, 40),
	(40, -10, 50),
	(40, -10, 60),
	(40, 0, -30),
	(40, 0, -20),
	(40, 0, -10),
	(40, 0, 0),
	(40, 0, 10),
	(40, 0, 20),
	(40, 0, 30),
	(40, 0, 40),
	(40, 0, 50),
	(40, 10, -30),
	(40, 10, -20),
	(40, 10, -10),
	(40, 10, 0),
	(40, 10, 10),
	(40, 10, 20),
	(40, 10, 30),
	(40, 10, 40),
	(40, 10, 50),
	(40, 20, -30),
	(40, 20, -10),
	(40, 20, 0),
	(40, 20, 10),
	(40, 20, 20),
	(40, 20, 30),
	(40, 20, 40),
	(40, 20, 50),
	(40, 30, -10),
	(40, 30, 0),
	(40, 30, 10),
	(40, 30, 20),
	(40, 30, 30),
	(40, 30, 40),
	(40, 40, -10),
	(40, 40, 0),
	(40, 40, 10),
	(40, 40, 20),
	(40, 40, 30),
	(40, 50, -10),
	(40, 50, 0),
	(40, 50, 10),
	(40, 50, 20),
	(40, 60, -10),
	(40, 60, 0),
	(40, 60, 10),
	(50, -80, -30),
	(50, -80, -20),
	(50, -80, -10),
	(50, -80, 0),
	(50, -80, 10),
	(50, -80, 20),
	(50, -70, -40),
	(50, -70, -30),
	(50, -70, -20),
	(50, -70, -10),
	(50, -70, 0),
	(50, -70, 10),
	(50, -70, 20),
	(50, -70, 30),
	(50, -60, -40),
	(50, -60, -30),
	(50, -60, -20),
	(50, -60, -10),
	(50, -60, 0),
	(50, -60, 10),
	(50, -60, 20),
	(50, -60, 30),
	(50, -60, 40),
	(50, -50, -30),
	(50, -50, -20),
	(50, -50, -10),
	(50, -50, 0),
	(50, -50, 10),
	(50, -50, 20),
	(50, -50, 30),
	(50, -50, 40),
	(50, -50, 50),
	(50, -40, -20),
	(50, -40, -10),
	(50, -40, 0),
	(50, -40, 10),
	(50, -40, 20),
	(50, -40, 30),
	(50, -40, 40),
	(50, -40, 50),
	(50, -30, -20),
	(50, -30, -10),
	(50, -30, 0),
	(50, -30, 10),
	(50, -30, 20),
	(50, -30, 30),
	(50, -30, 40),
	(50, -30, 50),
	(50, -20, -30),
	(50, -20, -20),
	(50, -20, -10),
	(50, -20, 0),
	(50, -20, 10),
	(50, -20, 20),
	(50, -20, 30),
	(50, -20, 40),
	(50, -20, 50),
	(50, -10, -30),
	(50, -10, -20),
	(50, -10, -10),
	(50, -10, 0),
	(50, -10, 10),
	(50, -10, 20),
	(50, -10, 30),
	(50, -10, 40),
	(50, -10, 50),
	(50, 0, -30),
	(50, 0, -20),
	(50, 0, -10),
	(50, 0, 0),
	(50, 0, 10),
	(50, 0, 20),
	(50, 0, 30),
	(50, 0, 40),
	(50, 0, 50),
	(50, 10, -30),
	(50, 10, -20),
	(50, 10, -10),
	(50, 10, 0),
	(50, 10, 10),
	(50, 10, 20),
	(50, 10, 30),
	(50, 10, 40),
	(50, 10, 50),
	(50, 20, -20),
	(50, 20, -10),
	(50, 20, 0),
	(50, 20, 10),
	(50, 20, 20),
	(50, 20, 30),
	(50, 20, 40),
	(50, 30, -10),
	(50, 30, 0),
	(50, 30, 10),
	(50, 30, 20),
	(50, 30, 30),
	(50, 40, -10),
	(50, 40, 0),
	(50, 40, 10),
	(50, 40, 20),
	(50, 40, 30),
	(50, 50, -10),
	(50, 50, 0),
	(50, 50, 10),
	(60, -70, 10),
	(60, -60, -10),
	(60, -60, 0),
	(60, -60, 10),
	(60, -60, 20),
	(60, -60, 30),
	(60, -50, -10),
	(60, -50, 0),
	(60, -50, 10),
	(60, -50, 20),
	(60, -50, 30),
	(60, -50, 40),
	(60, -40, -10),
	(60, -40, 0),
	(60, -40, 10),
	(60, -40, 20),
	(60, -40, 30),
	(60, -40, 40),
	(60, -30, -10),
	(60, -30, 0),
	(60, -30, 10),
	(60, -30, 20),
	(60, -30, 30),
	(60, -30, 40),
	(60, -20, -20),
	(60, -20, -10),
	(60, -20, 0),
	(60, -20, 10),
	(60, -20, 20),
	(60, -20, 30),
	(60, -20, 40),
	(60, -10, -20),
	(60, -10, -10),
	(60, -10, 0),
	(60, -10, 10),
	(60, -10, 20),
	(60, -10, 30),
	(60, -10, 40),
	(60, 0, -20),
	(60, 0, -10),
	(60, 0, 0),
	(60, 0, 10),
	(60, 0, 20),
	(60, 0, 30),
	(60, 0, 40),
	(60, 10, -10),
	(60, 10, 0),
	(60, 10, 10),
	(60, 10, 20),
	(60, 10, 30),
	(60, 20, -10),
	(60, 20, 0),
	(60, 20, 10),
	(60, 20, 20),
	(60, 20, 30),
	(60, 30, 0),
	(60, 30, 10),
	(60, 30, 20),
	(-30, 50, 30),
	(-50, 30, 0),
	(-40, 30, 40),
	(-60, 0, 30),
	(-60, 20, 0),
	(-60, -60, 0),
	(-30, -80, 10),
	(30, -80, 10),
	(60, -60, 0),
	(60, 20, 0),
	(60, 0, 30),
	(40, 30, 40),
	(50, 30, 0),
	(30, 50, 30)
	)


# f = open('mapping.txt','r')
#
# f1 = f.readlines()
# f2 = [w.replace('\n', '') for w in f1]
# f3 = [w.replace('\t', ',') for w in f2]
# f4 = tuple(f3)

def cube():
	glBegin(GL_POINTS)

	# for i in f4:
	# 	d = "("+i+")"
	# 	# glVertex3fv(d)
	# 	print(d)

	for vertex in vertices:
		glVertex3fv(vertex)

	# for edge in edges:
	# 	for vertex in edge:
	# 		glVertex3fv(vertices[vertex])

	glEnd()


def main():
	pygame.init()
	display = (800, 600)
	pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
	gluPerspective(300, (display[0]/display[1]), 5, 500.0)  # field of view in y-axis, aspect ratio, viewer to near
	# clipping angle and far clipping angle
	glTranslatef(0.0, 0.0, -50)  # translate against x-axis, y-axis and z-axis
	glRotatef(0, 0, 0, 0)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		glRotatef(1, 6, 9, 0)   # angel, x-axis, y-axis and z-axis
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		cube()
		pygame.display.flip()
		pygame.time.wait(10)

main()

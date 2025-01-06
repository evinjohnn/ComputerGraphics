from OpenGL.GL import *
from OpenGL.GLUT import *
from sys import argv
from math import sin,cos,radians
from time import sleep
from random import random

SIZE=1

def update():
	global SIZE
	if SIZE<9.6:
		SIZE+=0.1
	sleep(0.1)

def display():
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	glTranslatef(0,-10,0)
	glTranslatef(0,10,0)
	drawTree()
	glutPostRedisplay()
	glutSwapBuffers()
	update()

def drawTree():
	global SIZE
	
	glPushMatrix()
	glTranslatef(0,-200,0)

	glPushMatrix()
	glScalef(SIZE,2*SIZE,1)
	glTranslatef(0,10,0)
	glColor3f(0,0.69,0)
	drawStump()
	glPopMatrix()
	
	glPushMatrix()
	glTranslatef(0,20*SIZE,0)
	glScalef(10,10,1)
	for angle in range(180,-30,-30):
		
		glPushMatrix()
		x=cos(radians(angle))
		y=sin(radians(angle))
		glColor3f(0,0.96,0)	
		glScalef(SIZE*(1+random()/3),SIZE*(1+random()/5),1)
		glTranslatef(x,y,random())
		drawDisk()
		glPopMatrix()
	
	glPopMatrix()
	
	glPopMatrix()
	
def drawStump():
	glBegin(GL_QUADS)
	glVertex2f(1,10)
	glVertex2f(1,-10)
	glVertex2f(-1,-10)
	glVertex2f(-1,10)
	glEnd()

def drawDisk():
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(0,0)
	for theta in range(0,361):
		x= cos( radians( theta))
		y= sin( radians( theta))
		glVertex2f(x,y)

	glEnd()

glutInit(argv)
glutInitDisplayMode(GLUT_RGB|GLUT_DEPTH|GLUT_DOUBLE)
glutInitWindowSize(500,500)
glutCreateWindow("ball rolling downhill to a rest")
glutInitWindowPosition(500,500)
glClear(GL_COLOR_BUFFER_BIT)
glClearColor(0.5,0.5,0.5,0)
glPointSize(2.4)
glColor3f(1,1,1)
glOrtho(-250,250,-250,250,-250,250)
glutDisplayFunc(display)
glutMainLoop()
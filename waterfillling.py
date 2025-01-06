#BUCKET FILLING

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
on=0
time=0
color=1
level=0
def mainfn():
    global on,color,level
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glPointSize(3)
    glBegin(GL_QUADS)

    glVertex2f(-40,0)
    glVertex2f(-50,0)
    glVertex2f(-50,100)
    glVertex2f(-40,100)

    glVertex2f(-40,100)
    glVertex2f(20,100)
    glVertex2f(20,90)
    glVertex2f(-40,90)

    glVertex2f(20,100)
    glVertex2f(20,110)
    glVertex2f(40,on+110)
    glVertex2f(40,on+100)

    glVertex2f(20,110)
    glVertex2f(10,110)
    glVertex2f(10,80)
    glVertex2f(20,80)

    glColor3f(color,color,1)
    glVertex2f(20,80)
    glVertex2f(10,80)
    glVertex2f(0,0)
    glVertex2f(30,0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,1)
    for i in range (0,level,1):
        glVertex2f(-10,i)
        glVertex2f(40,i)
    glEnd()
    
    glBegin(GL_LINES)
    glColor3f(1,0,1)
    glVertex2f(-10,0)
    glVertex2f(40,0)
    glVertex2f(-10,70)
    glVertex2f(-10,0)
    glVertex2f(40,0)
    glVertex2f(40,70)
    glEnd()
    glutSwapBuffers()

def timer(value):
    global on,time,color,level
    time+=1
    if time==10:
        on=10
        color=0
        level=1
    if level>=1:
        if level<60:
            level+=1

    if level==60:
        on=0
        color=1
        
    glutPostRedisplay()
    glutTimerFunc(200,timer,0)
    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB)
glutInitWindowPosition(500,500)
glutInitWindowSize(500,500)
glutCreateWindow("EVERYTHING")
glClearColor(1,1,1,1)
gluOrtho2D(-250,250,-250,250)
glutDisplayFunc(mainfn)
glutTimerFunc(0,timer,0)
glutMainLoop()
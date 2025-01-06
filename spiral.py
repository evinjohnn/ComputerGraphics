from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
r=250
angle=0
def mainfn():
    global r,angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glPointSize(3)
    x1=r*math.cos(angle)
    y1=r*math.sin(angle)
    glBegin(GL_LINE_STRIP)
    angle1=0
    r1=250
    while r1>=0:
        x2=r1*math.cos(angle1)
        y2=r1*math.sin(angle1)
        glVertex2f(x2,y2)
        angle1-=0.1
        r1-=1
    glEnd()
    glPushMatrix()
    glTranslatef(x1,y1,0)
    glBegin(GL_TRIANGLE_FAN)
    
    theta=0
    glColor3f(0,0,0)
    while theta<=6.28:
        x=10*math.cos(theta)
        y=10*math.sin(theta)
        glVertex2f(x,y)
        theta+=0.01
    glEnd()
    glPopMatrix()
    glutSwapBuffers()
def timer(value):
    global r,angle
    if r>0:
        angle-=0.1
        r-=1
    glutPostRedisplay()
    glutTimerFunc(10,timer,0)
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowPosition(500,500)
glutInitWindowSize(500,500)
glutCreateWindow("EVERYTHING")
glClearColor(1,1,1,1)
gluOrtho2D(-250,250,-250,250)
glClear(GL_COLOR_BUFFER_BIT)
glColor3f(1,0,0)
glPointSize(3)
glutDisplayFunc(mainfn)
glutTimerFunc(0,timer,0)
glutMainLoop()
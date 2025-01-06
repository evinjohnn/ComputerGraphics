
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
change1=0
change2=0
angle=0
def mainfn():
    global change1,change2,angle
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    glPointSize(3)
    glBegin(GL_LINES)
    glVertex2f(-460,420)
    glVertex2f(-10,-30)
    glVertex2f(-10,-30)
    glVertex2f(250,-30)
    glEnd()
    glPushMatrix()
    glTranslatef(change1,change2,0)
    glRotatef(angle,0,0,1)
    glBegin(GL_POINTS)
    theta=0
    glVertex2f(15,0)
    glColor3f(1,0,1)
    while theta<=6.30:
        x=30*math.cos(theta)
        y=30*math.sin(theta)
        glVertex2f(x,y)
        theta+=0.1
    glEnd()
    glPopMatrix()
    glutSwapBuffers()
    
def timer(value):
    global change1,change2,angle
    change1+=1
    angle-=3
    if change1 >=250:
        change1=-250
        change2=250
    elif change1<=0:
        change2-=1
    glutPostRedisplay()
    glutTimerFunc(10,timer,0)

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
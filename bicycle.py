from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
angle=0
motion=0
def mainfn():
    global angle,motion
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslate(motion,0,0)
    glPushMatrix()
    glRotatef(angle,0,0,1)
    glBegin(GL_TRIANGLE_FAN)
    theta=0
    glColor3f(0,0,0)
    while theta<=6.28:
        x=30*math.cos(theta)
        y=30*math.sin(theta)
        glVertex2f(x,y)
        theta+=0.01
    glEnd()
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    glVertex2f(10,0)
    glEnd()
    glPopMatrix()

    glPushMatrix()
    glTranslatef(100,0,0)
    glRotatef(angle,0,0,1)
    glTranslatef(-100,0,0)
    glBegin(GL_TRIANGLE_FAN)
    theta1=0
    glColor3f(0,0,0)
    while theta1<=6.28:
        x=30*math.cos(theta1)
        y=30*math.sin(theta1)
        glVertex2f(x+100,y)
        theta1+=0.01
    glEnd()
    glColor3f(1,0,0)
    glBegin(GL_POINTS)
    glVertex2f(110,0)
    glEnd()
    glPopMatrix()

    glColor3f(1,0,1)
    glPointSize(3)

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(-10,60)
    glVertex2f(-10,70)
    glVertex2f(100,70)
    glVertex2f(100,60)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0,70)
    glVertex2f(10,70)
    glVertex2f(10,0)
    glVertex2f(0,0)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(110,0)
    glVertex2f(100,0)
    glVertex2f(100,100)
    glVertex2f(110,100)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(100,100)
    glVertex2f(100,90)
    glVertex2f(80,90)
    glVertex2f(80,100)
    glEnd()


    glPopMatrix()
    glutSwapBuffers()
def timer(value):
    global angle,motion
    angle+=30
    motion+=1
    if angle>=360:
        angle=0
    if motion>=250:
        motion=-250
    glutPostRedisplay()
    glutTimerFunc(3,timer,0) 
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowPosition(500,500)
glutInitWindowSize(500,500)
glutCreateWindow("EVERYTHING")
glClearColor(1,1,1,1)
gluOrtho2D(-250,250,-250,250)
glutDisplayFunc(mainfn)
glutTimerFunc(0,timer,0)
glutMainLoop()
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import math
angle1=0
angle2=0
angle3=0
def mainfn():
    global angle1,angle2,angle3
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(0,0)
    glEnd()
    glBegin(GL_POINTS)
    theta=0
    glColor3f(0,0,0)
    while theta<=6.30:
        x=100*math.cos(theta)
        y=100*math.sin(theta)
        glVertex2f(x,y)
        theta+=0.01
    glEnd()
    glPushMatrix()
    glRotatef(-angle2,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(0,80)
    glEnd()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-angle1,0,0,1)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(50,0)
    glEnd()
    glPopMatrix()
    glPushMatrix()
    glRotatef(-angle3,0,0,1)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex2f(0,0)
    glVertex2f(0,70)
    glEnd()
    glPopMatrix()
    glutSwapBuffers()

def timer(value):
    global angle1,angle2,angle3
    angle3+=1
    if angle3==360:
        angle2+=1
        angle3=0
    if angle2==360:
        angle1+=1
        angle2=0
    glutPostRedisplay()
    glutTimerFunc(120,timer,0)
    
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowPosition(500,500)
glutInitWindowSize(500,500)
glutCreateWindow("EVERYTHING")
glClearColor(1,1,1,1)
gluOrtho2D(-250,250,-250,250)
glutDisplayFunc(mainfn)
glutTimerFunc(0,timer,0)
glutMainLoop()
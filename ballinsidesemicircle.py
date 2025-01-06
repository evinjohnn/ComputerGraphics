from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
from math import*
from sys import*

win = 500
r=20
t=0
c=60
f=0
angle=0

def ball(r):
	glBegin(GL_TRIANGLE_FAN)
	for i in range(0,360):
		xc=r*cos(pi*i/180)
		yc=r*sin(pi*i/180)
		glVertex2f(xc,yc)
	glEnd()
	
def line(r):
	glLineWidth(3)
	glBegin(GL_LINES)
	glVertex2f(-r*cos(t),r*sin(t))
	glVertex2f(r*cos(t),-r*sin(t))
	glEnd()
	
def bowl(r):
	glLineWidth(2)
	glBegin(GL_LINE_STRIP)
	theta=0
	for i in range(0,180):
		glVertex2f(r*cos(pi*theta/180),r*sin(pi*theta/180))
		theta-=1
	glEnd()
	
def draw():
	glClear(GL_COLOR_BUFFER_BIT)
	glPushMatrix()
	glScalef(2,2,0)
	glPushMatrix()
	glRotatef(angle,0,0,1)
	glTranslatef(0,-100,0)
	glColor3f(1,0,0)
	ball(r)
	glColor3f(0,0,0)
	line(r)
	glPopMatrix()
	glColor3f(0,1,0)
	bowl(r+100)
	glPopMatrix()
	glFlush()
	
def animate(n):
	global t,c,angle,f
	glutPostRedisplay()
	if c<=5:
		c=0
		return
	if angle>=c:
		f=1
	if angle<=-c:
		f=0
	if f==0:
		angle+=n
		t+=n-0.8
	if f==1:
		angle-=n
		t-=n-0.8
	if angle==0:
		c-=2
	glutTimerFunc(16,animate,1)
			

def main():
	glutInit(argv)
	glutInitWindowSize(win,win)
	glutInitDisplayMode(GLUT_RGB)
	glutCreateWindow("Ball in Bowl")
	glutDisplayFunc(draw)
	glutTimerFunc(0,animate,0)
	glClearColor(1,1,1,1)
	gluOrtho2D(-win,win,-win,win)
	glutMainLoop()
	
main()
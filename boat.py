from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

# Boat parameters
boat_x = 0.0
boat_y = -0.5
oar_angle = 0.0
oar_speed = 2.0
water_level = -0.6
boat_speed = 0.005  # Speed of the boat

def draw_boat():
    glColor3f(0.5, 0.3, 0.1)  # Brown boat
    glBegin(GL_POLYGON)
    glVertex2f(-0.3, 0.1)  # Reversed boat shape
    glVertex2f(0.3, 0.1)
    glVertex2f(0.2, -0.1)
    glVertex2f(-0.2, -0.1)
    glEnd()

def draw_person():
    glColor3f(0.0, 0.0, 0.0)  # Black person
    # Head
    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 360, 10):
        glVertex2f(0.0 + 0.05 * math.cos(math.radians(i)), 0.2 + 0.05 * math.sin(math.radians(i)))  # Adjusted position
    glEnd()
    # Body
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.2)
    glVertex2f(0.0, 0.0)
    glEnd()
    # Arms
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.1)
    glVertex2f(-0.1, 0.2)
    glVertex2f(0.0, 0.1)
    glVertex2f(0.1, 0.2)
    glEnd()
    # Legs
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(-0.1, -0.1)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.1, -0.1)
    glEnd()

def draw_oar(x, y, angle):
    glPushMatrix()
    glTranslatef(x, y, 0.0)
    glRotatef(angle, 0.0, 0.0, 1.0)
    glColor3f(0.0, 0.0, 0.0)  # Black oar
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)
    glVertex2f(0.0, -0.3)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-0.02, -0.3)
    glVertex2f(0.02, -0.3)
    glVertex2f(0.02, -0.5)
    glVertex2f(-0.02, -0.5)
    glEnd()
    glPopMatrix()

def draw_water():
    glColor3f(0.0, 0.0, 1.0)  # Blue water
    glBegin(GL_POLYGON)
    glVertex2f(-1.0, water_level)
    glVertex2f(1.0, water_level)
    glVertex2f(1.0, -1.0)
    glVertex2f(-1.0, -1.0)
    glEnd()

def update(value):
    global oar_angle, boat_x

    # Animate oars
    oar_angle = 30 * math.sin(math.radians(time.time() * oar_speed * 100))

    # Move boat forward when oars are in the correct position
    if oar_angle > 0:  # Move boat when oars are pushing water
        boat_x += boat_speed

    # Reset boat position if it goes off-screen
    if boat_x > 1.0:
        boat_x = -1.0

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # Draw water
    draw_water()

    # Draw boat
    glPushMatrix()
    glTranslatef(boat_x, boat_y, 0.0)
    draw_boat()
    draw_person()

    # Draw oars (only above water)
    if oar_angle > -15:  # Only draw oars when not submerged
        draw_oar(-0.2, 0.1, oar_angle)  # Adjusted position
        draw_oar(0.2, 0.1, -oar_angle)  # Adjusted position
    glPopMatrix()

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set orthogonal projection

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Boat Rowing with Movement")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
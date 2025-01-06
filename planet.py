from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initialize variables
planet_angle = 0  # Angle of the planet's orbit
planet_distance = 0.7  # Distance from the sun
planet_speed = 1  # Speed of the planet's orbit

def draw_sun():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color for the sun
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Center of the sun
    for i in range(0, 361, 10):
        glVertex2f(0.2 * math.cos(math.radians(i)), 0.2 * math.sin(math.radians(i)))
    glEnd()

def draw_planet():
    global planet_angle
    glPushMatrix()
    glRotatef(planet_angle, 0, 0, 1)  # Rotate the planet around the sun
    glTranslatef(planet_distance, 0, 0)  # Position the planet
    glColor3f(0.0, 0.0, 1.0)  # Blue color for the planet
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Center of the planet
    for i in range(0, 361, 10):
        glVertex2f(0.1 * math.cos(math.radians(i)), 0.1 * math.sin(math.radians(i)))
    glEnd()
    glPopMatrix()

def update(value):
    global planet_angle
    planet_angle += planet_speed
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_sun()  # Draw the sun
    draw_planet()  # Draw the planet
    glutSwapBuffers()  # Swap buffers for double buffering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering
    glutInitWindowSize(500, 500)
    glutCreateWindow("Planet Rotating Around the Sun")
    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set orthogonal projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
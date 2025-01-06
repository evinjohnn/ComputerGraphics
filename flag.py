from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Initialize variables
flag_width = 0.5
flag_height = 0.3
wave_amplitude = 0.05
wave_frequency = 0.1
time = 0

def draw_pole():
    # Draw the flag pole
    glColor3f(0.5, 0.5, 0.5)  # Gray color for the pole
    glLineWidth(5.0)  # Thicker line for the pole
    glBegin(GL_LINES)
    glVertex2f(-0.8, -1.0)  # Bottom of the pole
    glVertex2f(-0.8, 1.0)   # Top of the pole
    glEnd()

def draw_flag():
    # Draw the flag attached to the pole
    glBegin(GL_QUAD_STRIP)
    for x in range(0, 100):
        x_norm = x / 100.0
        y_wave = wave_amplitude * math.sin(2 * math.pi * (x_norm - time))
        glColor3f(1.0, 0.0, 0.0)  # Red color for the flag
        glVertex2f(-0.8 + x_norm * flag_width, y_wave)
        glVertex2f(-0.8 + x_norm * flag_width, y_wave + flag_height)
    glEnd()

def update(value):
    global time
    time += wave_frequency
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_pole()  # Draw the flag pole
    draw_flag()  # Draw the fluttering flag
    glutSwapBuffers()  # Swap buffers for double buffering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering
    glutInitWindowSize(500, 500)
    glutCreateWindow("Flag Fluttering on a Pole")
    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set orthogonal projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
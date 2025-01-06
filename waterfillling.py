# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
import sys  # For command-line arguments
import math  # For mathematical functions (not used in this code)

# Global variables
on = 0  # Flag to control the animation
time = 0  # Timer for the animation
color = 1  # Color of the bucket
level = 0  # Water level in the bucket

# Main rendering function
def mainfn():
    """Render the bucket and the water."""
    global on, color, level  # Access global variables
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(0, 0, 0)  # Set the color to black
    glPointSize(3)  # Set the point size

    # Draw the bucket using quads
    glBegin(GL_QUADS)

    # Left side of the bucket
    glVertex2f(-40, 0)
    glVertex2f(-50, 0)
    glVertex2f(-50, 100)
    glVertex2f(-40, 100)

    # Top of the bucket
    glVertex2f(-40, 100)
    glVertex2f(20, 100)
    glVertex2f(20, 90)
    glVertex2f(-40, 90)

    # Right side of the bucket
    glVertex2f(20, 100)
    glVertex2f(20, 110)
    glVertex2f(40, on + 110)
    glVertex2f(40, on + 100)

    # Handle of the bucket
    glVertex2f(20, 110)
    glVertex2f(10, 110)
    glVertex2f(10, 80)
    glVertex2f(20, 80)

    # Bottom of the bucket (colored based on the animation)
    glColor3f(color, color, 1)  # Set the color to a shade of blue
    glVertex2f(20, 80)
    glVertex2f(10, 80)
    glVertex2f(0, 0)
    glVertex2f(30, 0)
    glEnd()

    # Draw the water level using lines
    glBegin(GL_LINES)
    glColor3f(0, 0, 1)  # Set the color to blue
    for i in range(0, level, 1):  # Loop to draw multiple horizontal lines
        glVertex2f(-10, i)  # Start point of the line
        glVertex2f(40, i)  # End point of the line
    glEnd()

    # Draw the outline of the water container
    glBegin(GL_LINES)
    glColor3f(1, 0, 1)  # Set the color to magenta
    glVertex2f(-10, 0)  # Bottom-left corner
    glVertex2f(40, 0)  # Bottom-right corner
    glVertex2f(-10, 70)  # Top-left corner
    glVertex2f(-10, 0)  # Bottom-left corner
    glVertex2f(40, 0)  # Bottom-right corner
    glVertex2f(40, 70)  # Top-right corner
    glEnd()

    glutSwapBuffers()  # Swap buffers for double buffering

# Timer function for animation
def timer(value):
    """Update the animation parameters."""
    global on, time, color, level  # Access global variables
    time += 1  # Increment the timer

    # Start the animation after 10 timer ticks
    if time == 10:
        on = 10  # Activate the animation
        color = 0  # Change the bucket color
        level = 1  # Start filling the water

    # Increase the water level
    if level >= 1:
        if level < 60:  # Stop filling when the water reaches the top
            level += 1

    # Reset the animation when the bucket is full
    if level == 60:
        on = 0  # Stop the animation
        color = 1  # Reset the bucket color

    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(200, timer, 0)  # Call this function again after 200 milliseconds

# Initialize OpenGL and create the window
glutInit(sys.argv)  # Initialize GLUT
glutInitDisplayMode(GLUT_RGB)  # Set the display mode to RGB
glutInitWindowPosition(500, 500)  # Set the window position
glutInitWindowSize(500, 500)  # Set the window size
glutCreateWindow("EVERYTHING")  # Create the window with a title
glClearColor(1, 1, 1, 1)  # Set the background color to white
gluOrtho2D(-250, 250, -250, 250)  # Set up a 2D orthographic projection
glutDisplayFunc(mainfn)  # Register the main rendering function
glutTimerFunc(0, timer, 0)  # Start the animation timer
glutMainLoop()  # Enter the GLUT main loop
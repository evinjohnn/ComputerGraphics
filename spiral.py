# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
import sys  # For command-line arguments
import math  # For trigonometric functions (e.g., cos, sin)

# Initialize variables
r = 250  # Initial radius of the spiral
angle = 0  # Initial angle for the spiral

# Main rendering function
def mainfn():
    """Render the spiral and the moving circle."""
    global r, angle  # Access global variables
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1, 0, 0)  # Set the color to red
    glPointSize(3)  # Set the point size

    # Calculate the position of the moving circle
    x1 = r * math.cos(angle)  # X-coordinate of the circle
    y1 = r * math.sin(angle)  # Y-coordinate of the circle

    # Draw the spiral
    glBegin(GL_LINE_STRIP)  # Start drawing a connected line strip
    angle1 = 0  # Initialize the angle for the spiral
    r1 = 250  # Initialize the radius for the spiral
    while r1 >= 0:  # Loop until the radius reaches 0
        x2 = r1 * math.cos(angle1)  # X-coordinate of the spiral point
        y2 = r1 * math.sin(angle1)  # Y-coordinate of the spiral point
        glVertex2f(x2, y2)  # Add the point to the spiral
        angle1 -= 0.1  # Decrease the angle
        r1 -= 1  # Decrease the radius
    glEnd()  # End drawing the spiral

    # Draw the moving circle
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(x1, y1, 0)  # Move to the circle's position
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    theta = 0  # Initialize the angle for the circle
    glColor3f(0, 0, 0)  # Set the color to black
    while theta <= 6.28:  # Loop through 360 degrees (in radians)
        x = 10 * math.cos(theta)  # X-coordinate of the circle's edge
        y = 10 * math.sin(theta)  # Y-coordinate of the circle's edge
        glVertex2f(x, y)  # Add the point to the circle
        theta += 0.01  # Increment the angle
    glEnd()  # End drawing the circle
    glPopMatrix()  # Restore the previous transformation matrix

    glutSwapBuffers()  # Swap buffers for double buffering

# Timer function for animation
def timer(value):
    """Update the spiral's radius and angle for animation."""
    global r, angle  # Access global variables
    if r > 0:  # If the radius is greater than 0
        angle -= 0.1  # Decrease the angle
        r -= 1  # Decrease the radius
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(10, timer, 0)  # Call this function again after 10 milliseconds (~100 FPS)

# Initialize OpenGL and create the window
glutInit(sys.argv)  # Initialize GLUT
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)  # Set the display mode to RGB with double buffering
glutInitWindowPosition(500, 500)  # Set the window position
glutInitWindowSize(500, 500)  # Set the window size
glutCreateWindow("EVERYTHING")  # Create the window with a title
glClearColor(1, 1, 1, 1)  # Set the background color to white
gluOrtho2D(-250, 250, -250, 250)  # Set up a 2D orthographic projection
glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
glColor3f(1, 0, 0)  # Set the color to red
glPointSize(3)  # Set the point size
glutDisplayFunc(mainfn)  # Register the main rendering function
glutTimerFunc(0, timer, 0)  # Start the animation timer
glutMainLoop()  # Enter the GLUT event processing loop
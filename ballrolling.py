# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
import sys  # For command-line arguments
import math  # For trigonometric functions (e.g., cos, sin)

# Global variables
change1 = 0  # Horizontal position of the circle
change2 = 0  # Vertical position of the circle
angle = 0  # Rotation angle of the circle

# Main rendering function
def mainfn():
    """Render the scene."""
    global change1, change2, angle  # Access global variables
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(1, 0, 0)  # Set the color to red
    glPointSize(3)  # Set the point size

    # Draw the path (two connected lines)
    glBegin(GL_LINES)
    glVertex2f(-460, 420)  # Start point of the first line
    glVertex2f(-10, -30)  # End point of the first line
    glVertex2f(-10, -30)  # Start point of the second line
    glVertex2f(250, -30)  # End point of the second line
    glEnd()

    # Draw the rotating circle
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(change1, change2, 0)  # Move the circle to its current position
    glRotatef(angle, 0, 0, 1)  # Rotate the circle by the current angle
    glBegin(GL_POINTS)  # Start drawing points
    theta = 0  # Initialize the angle for drawing the circle
    glVertex2f(15, 0)  # Draw a point at the center of the circle
    glColor3f(1, 0, 1)  # Set the color to magenta
    while theta <= 6.30:  # Loop through 360 degrees (in radians)
        x = 30 * math.cos(theta)  # Calculate x-coordinate of the circle's edge
        y = 30 * math.sin(theta)  # Calculate y-coordinate of the circle's edge
        glVertex2f(x, y)  # Draw a point on the circle's edge
        theta += 0.1  # Increment the angle
    glEnd()  # End drawing points
    glPopMatrix()  # Restore the previous transformation matrix

    glutSwapBuffers()  # Swap buffers to display the rendered frame

# Timer function for animation
def timer(value):
    """Update the circle's position and rotation."""
    global change1, change2, angle  # Access global variables
    change1 += 1  # Move the circle horizontally
    angle -= 3  # Rotate the circle counterclockwise
    if change1 >= 250:  # If the circle reaches the end of the second line
        change1 = -250  # Reset the horizontal position
        change2 = 250  # Move the circle to the top of the first line
    elif change1 <= 0:  # If the circle is on the first line
        change2 -= 1  # Move the circle downward
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(10, timer, 0)  # Call this function again after 10 milliseconds (~100 FPS)

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
glutMainLoop()  # Enter the GLUT event processing loop
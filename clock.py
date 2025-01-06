# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
import sys  # For command-line arguments
import math  # For trigonometric functions (e.g., cos, sin)

# Global variables for rotation angles
angle1 = 0  # Rotation angle for the first line (hour hand)
angle2 = 0  # Rotation angle for the second line (minute hand)
angle3 = 0  # Rotation angle for the third line (second hand)

# Main rendering function
def mainfn():
    """Render the scene."""
    global angle1, angle2, angle3  # Access global variables
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glColor3f(0, 0, 0)  # Set the color to black
    glPointSize(3)  # Set the point size

    # Draw a point at the origin
    glBegin(GL_POINTS)
    glVertex2f(0, 0)  # Draw a point at (0, 0)
    glEnd()

    # Draw a circle (for reference)
    glBegin(GL_POINTS)
    theta = 0  # Initialize the angle for drawing the circle
    glColor3f(0, 0, 0)  # Set the color to black
    while theta <= 6.30:  # Loop through 360 degrees (in radians)
        x = 100 * math.cos(theta)  # Calculate x-coordinate of the circle's edge
        y = 100 * math.sin(theta)  # Calculate y-coordinate of the circle's edge
        glVertex2f(x, y)  # Draw a point on the circle's edge
        theta += 0.01  # Increment the angle
    glEnd()

    # Draw the first rotating line (hour hand)
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(-angle2, 0, 0, 1)  # Rotate the line by angle2
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(0, 0)  # Start point of the line
    glVertex2f(0, 80)  # End point of the line
    glEnd()  # End drawing the line
    glPopMatrix()  # Restore the previous transformation matrix

    # Draw the second rotating line (minute hand)
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(-angle1, 0, 0, 1)  # Rotate the line by angle1
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(0, 0)  # Start point of the line
    glVertex2f(50, 0)  # End point of the line
    glEnd()  # End drawing the line
    glPopMatrix()  # Restore the previous transformation matrix

    # Draw the third rotating line (second hand)
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(-angle3, 0, 0, 1)  # Rotate the line by angle3
    glBegin(GL_LINES)  # Start drawing a line
    glColor3f(1, 0, 0)  # Set the color to red
    glVertex2f(0, 0)  # Start point of the line
    glVertex2f(0, 70)  # End point of the line
    glEnd()  # End drawing the line
    glPopMatrix()  # Restore the previous transformation matrix

    glutSwapBuffers()  # Swap buffers for double buffering

# Timer function for animation
def timer(value):
    """Update the rotation angles for the lines."""
    global angle1, angle2, angle3  # Access global variables
    angle3 += 1  # Increment the angle for the third line
    if angle3 == 360:  # If the third line completes a full rotation
        angle2 += 1  # Increment the angle for the second line
        angle3 = 0  # Reset the angle for the third line
    if angle2 == 360:  # If the second line completes a full rotation
        angle1 += 1  # Increment the angle for the first line
        angle2 = 0  # Reset the angle for the second line
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(120, timer, 0)  # Call this function again after 120 milliseconds (~8 FPS)

# Initialize OpenGL and create the window
glutInit(sys.argv)  # Initialize GLUT
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
glutInitWindowPosition(500, 500)  # Set the window position
glutInitWindowSize(500, 500)  # Set the window size
glutCreateWindow("CLock")  # Create the window with a title
glClearColor(1, 1, 1, 1)  # Set the background color to white
gluOrtho2D(-250, 250, -250, 250)  # Set up a 2D orthographic projection
glutDisplayFunc(mainfn)  # Register the main rendering function
glutTimerFunc(0, timer, 0)  # Start the animation timer
glutMainLoop()  # Enter the GLUT event processing loop
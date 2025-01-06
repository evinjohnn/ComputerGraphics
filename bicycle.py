 # Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
import sys  # For command-line arguments
import math  # For trigonometric functions (e.g., cos, sin)

# Global variables
angle = 0  # Rotation angle of the wheels
motion = 0  # Horizontal position of the vehicle

# Main rendering function
def mainfn():
    """Render the scene."""
    global angle, motion  # Access global variables
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw the vehicle and wheels
    glPushMatrix()  # Save the current transformation matrix
    glTranslate(motion, 0, 0)  # Move the vehicle horizontally

    # Draw the first wheel (left wheel)
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(angle, 0, 0, 1)  # Rotate the wheel
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    theta = 0  # Initialize the angle for drawing the circle
    glColor3f(0, 0, 0)  # Set the color to black
    while theta <= 6.28:  # Loop through 360 degrees (in radians)
        x = 30 * math.cos(theta)  # Calculate x-coordinate of the circle's edge
        y = 30 * math.sin(theta)  # Calculate y-coordinate of the circle's edge
        glVertex2f(x, y)  # Draw a point on the circle's edge
        theta += 0.01  # Increment the angle
    glEnd()  # End drawing the circle

    # Draw a red dot on the wheel (to visualize rotation)
    glColor3f(1, 0, 0)  # Set the color to red
    glBegin(GL_POINTS)  # Start drawing points
    glVertex2f(10, 0)  # Draw a point at (10, 0)
    glEnd()  # End drawing points
    glPopMatrix()  # Restore the previous transformation matrix

    # Draw the second wheel (right wheel)
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(100, 0, 0)  # Move to the position of the second wheel
    glRotatef(angle, 0, 0, 1)  # Rotate the wheel
    glTranslatef(-100, 0, 0)  # Move back to the original position
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    theta1 = 0  # Initialize the angle for drawing the circle
    glColor3f(0, 0, 0)  # Set the color to black
    while theta1 <= 6.28:  # Loop through 360 degrees (in radians)
        x = 30 * math.cos(theta1)  # Calculate x-coordinate of the circle's edge
        y = 30 * math.sin(theta1)  # Calculate y-coordinate of the circle's edge
        glVertex2f(x + 100, y)  # Draw a point on the circle's edge
        theta1 += 0.01  # Increment the angle
    glEnd()  # End drawing the circle

    # Draw a red dot on the wheel (to visualize rotation)
    glColor3f(1, 0, 0)  # Set the color to red
    glBegin(GL_POINTS)  # Start drawing points
    glVertex2f(110, 0)  # Draw a point at (110, 0)
    glEnd()  # End drawing points
    glPopMatrix()  # Restore the previous transformation matrix

    # Draw the vehicle body (magenta rectangles)
    glColor3f(1, 0, 1)  # Set the color to magenta
    glPointSize(3)  # Set the point size

    # Draw the base of the vehicle
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled rectangle
    glVertex2f(-10, 60)  # Bottom-left corner
    glVertex2f(-10, 70)  # Top-left corner
    glVertex2f(100, 70)  # Top-right corner
    glVertex2f(100, 60)  # Bottom-right corner
    glEnd()  # End drawing the rectangle

    # Draw the left pillar of the vehicle
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled rectangle
    glVertex2f(0, 70)  # Top-left corner
    glVertex2f(10, 70)  # Top-right corner
    glVertex2f(10, 0)  # Bottom-right corner
    glVertex2f(0, 0)  # Bottom-left corner
    glEnd()  # End drawing the rectangle

    # Draw the right pillar of the vehicle
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled rectangle
    glVertex2f(110, 0)  # Bottom-left corner
    glVertex2f(100, 0)  # Bottom-right corner
    glVertex2f(100, 100)  # Top-right corner
    glVertex2f(110, 100)  # Top-left corner
    glEnd()  # End drawing the rectangle

    # Draw the top of the vehicle
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled rectangle
    glVertex2f(100, 100)  # Bottom-left corner
    glVertex2f(100, 90)  # Top-left corner
    glVertex2f(80, 90)  # Top-right corner
    glVertex2f(80, 100)  # Bottom-right corner
    glEnd()  # End drawing the rectangle

    glPopMatrix()  # Restore the previous transformation matrix
    glutSwapBuffers()  # Swap buffers to display the rendered frame

# Timer function for animation
def timer(value):
    """Update the rotation angle and horizontal position."""
    global angle, motion  # Access global variables
    angle += 30  # Increment the rotation angle
    motion += 1  # Move the vehicle horizontally
    if angle >= 360:  # Reset the angle after a full rotation
        angle = 0
    if motion >= 250:  # Reset the horizontal position after reaching the edge
        motion = -250
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(3, timer, 0)  # Call this function again after 3 milliseconds (~333 FPS)

# Initialize OpenGL and create the window
glutInit(sys.argv)  # Initialize GLUT
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)  # Set the display mode to RGB with double buffering
glutInitWindowPosition(500, 500)  # Set the window position
glutInitWindowSize(500, 500)  # Set the window size
glutCreateWindow("cycle")  # Create the window with a title
glClearColor(1, 1, 1, 1)  # Set the background color to white
gluOrtho2D(-250, 250, -250, 250)  # Set up a 2D orthographic projection
glutDisplayFunc(mainfn)  # Register the main rendering function
glutTimerFunc(0, timer, 0)  # Start the animation timer
glutMainLoop()  # Enter the GLUT event processing loop
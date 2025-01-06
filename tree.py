# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from sys import argv  # For command-line arguments
from math import sin, cos, radians  # For trigonometric functions
from time import sleep  # For adding delays
from random import random  # For random scaling of disks

# Global variable for tree size
SIZE = 1  # Initial size of the tree

# Function to update the tree size
def update():
    """Gradually increase the size of the tree."""
    global SIZE
    if SIZE < 9.6:  # Stop growing when SIZE reaches 9.6
        SIZE += 0.1  # Increment the size
    sleep(0.1)  # Add a small delay for smooth animation

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
    glTranslatef(0, -10, 0)  # Translate the scene downward
    glTranslatef(0, 10, 0)  # Translate the scene upward (net effect: no translation)
    drawTree()  # Draw the tree
    glutPostRedisplay()  # Request a redraw of the scene
    glutSwapBuffers()  # Swap buffers for double buffering
    update()  # Update the tree size

# Function to draw the tree
def drawTree():
    """Draw the tree with a stump and disks representing leaves."""
    global SIZE

    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(0, -200, 0)  # Move the tree downward

    # Draw the stump (green rectangle)
    glPushMatrix()
    glScalef(SIZE, 2 * SIZE, 1)  # Scale the stump
    glTranslatef(0, 10, 0)  # Move the stump upward
    glColor3f(0, 0.69, 0)  # Set the color to green
    drawStump()  # Draw the stump
    glPopMatrix()

    # Draw the disks (leaves)
    glPushMatrix()
    glTranslatef(0, 20 * SIZE, 0)  # Move the disks upward
    glScalef(10, 10, 1)  # Scale the disks
    for angle in range(180, -30, -30):  # Loop through angles for disk placement
        glPushMatrix()
        x = cos(radians(angle))  # Calculate x-coordinate
        y = sin(radians(angle))  # Calculate y-coordinate
        glColor3f(0, 0.96, 0)  # Set the color to bright green
        glScalef(SIZE * (1 + random() / 3), SIZE * (1 + random() / 5), 1)  # Randomly scale the disk
        glTranslatef(x, y, random())  # Position the disk
        drawDisk()  # Draw the disk
        glPopMatrix()
    glPopMatrix()

    glPopMatrix()  # Restore the previous transformation matrix

# Function to draw the stump (a rectangle)
def drawStump():
    """Draw the stump of the tree."""
    glBegin(GL_QUADS)  # Start drawing a rectangle
    glVertex2f(1, 10)  # Top-right corner
    glVertex2f(1, -10)  # Bottom-right corner
    glVertex2f(-1, -10)  # Bottom-left corner
    glVertex2f(-1, 10)  # Top-left corner
    glEnd()  # End drawing the rectangle

# Function to draw a disk (a circle)
def drawDisk():
    """Draw a disk (circle) representing a leaf."""
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    glVertex2f(0, 0)  # Center of the circle
    for theta in range(0, 361):  # Loop through 360 degrees
        x = cos(radians(theta))  # Calculate x-coordinate
        y = sin(radians(theta))  # Calculate y-coordinate
        glVertex2f(x, y)  # Add a point on the circle
    glEnd()  # End drawing the circle

# Initialize OpenGL and create the window
glutInit(argv)  # Initialize GLUT
glutInitDisplayMode(GLUT_RGB | GLUT_DEPTH | GLUT_DOUBLE)  # Set the display mode
glutInitWindowSize(500, 500)  # Set the window size
glutCreateWindow("Ball Rolling Downhill to a Rest")  # Create the window with a title
glutInitWindowPosition(500, 500)  # Set the window position
glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
glClearColor(0.5, 0.5, 0.5, 0)  # Set the background color to gray
glPointSize(2.4)  # Set the point size
glColor3f(1, 1, 1)  # Set the default color to white
glOrtho(-250, 250, -250, 250, -250, 250)  # Set up a 2D orthographic projection
glutDisplayFunc(display)  # Register the display function
glutMainLoop()  # Enter the GLUT main loop
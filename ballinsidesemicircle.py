# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLU import *  # OpenGL Utility Library
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from math import *  # For trigonometric functions (e.g., sin, cos)
from sys import *  # For command-line arguments

# Global variables
win = 500  # Window size (500x500 pixels)
r = 20  # Radius of the ball
t = 0  # Angle for the line inside the ball
c = 60  # Maximum angle for the ball's oscillation
f = 0  # Flag to control the direction of oscillation
angle = 0  # Current angle of the ball's position in the bowl

# Function to draw the ball
def ball(r):
    """Draw a ball with the given radius."""
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    for i in range(0, 360):  # Loop through 360 degrees
        xc = r * cos(pi * i / 180)  # Calculate x-coordinate
        yc = r * sin(pi * i / 180)  # Calculate y-coordinate
        glVertex2f(xc, yc)  # Add the point to the circle
    glEnd()  # End drawing the circle

# Function to draw the line inside the ball
def line(r):
    """Draw a line inside the ball."""
    glLineWidth(3)  # Set the line width
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(-r * cos(t), r * sin(t))  # Start point of the line
    glVertex2f(r * cos(t), -r * sin(t))  # End point of the line
    glEnd()  # End drawing the line

# Function to draw the bowl
def bowl(r):
    """Draw a bowl with the given radius."""
    glLineWidth(2)  # Set the line width
    glBegin(GL_LINE_STRIP)  # Start drawing a connected line strip
    theta = 0  # Initialize the angle
    for i in range(0, 180):  # Loop through 180 degrees
        glVertex2f(r * cos(pi * theta / 180), r * sin(pi * theta / 180))  # Add a point to the bowl
        theta -= 1  # Decrease the angle
    glEnd()  # End drawing the bowl

# Function to render the scene
def draw():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    glPushMatrix()  # Save the current transformation matrix
    glScalef(2, 2, 0)  # Scale the scene by 2x
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(angle, 0, 0, 1)  # Rotate the ball by the current angle
    glTranslatef(0, -100, 0)  # Move the ball to the bottom of the bowl
    glColor3f(1, 0, 0)  # Set the ball's color to red
    ball(r)  # Draw the ball
    glColor3f(0, 0, 0)  # Set the line's color to black
    line(r)  # Draw the line inside the ball
    glPopMatrix()  # Restore the previous transformation matrix
    glColor3f(0, 1, 0)  # Set the bowl's color to green
    bowl(r + 100)  # Draw the bowl
    glPopMatrix()  # Restore the previous transformation matrix
    glFlush()  # Flush the OpenGL pipeline

# Function to animate the ball
def animate(n):
    """Animate the ball's oscillation."""
    global t, c, angle, f  # Access global variables
    glutPostRedisplay()  # Request a redraw of the scene
    if c <= 5:  # If the maximum angle is too small
        c = 0  # Stop the animation
        return
    if angle >= c:  # If the ball reaches the maximum angle
        f = 1  # Reverse the direction
    if angle <= -c:  # If the ball reaches the minimum angle
        f = 0  # Reverse the direction
    if f == 0:  # If the ball is moving forward
        angle += n  # Increase the angle
        t += n - 0.8  # Update the line's angle
    if f == 1:  # If the ball is moving backward
        angle -= n  # Decrease the angle
        t -= n - 0.8  # Update the line's angle
    if angle == 0:  # If the ball returns to the center
        c -= 2  # Reduce the maximum angle (simulate damping)
    glutTimerFunc(16, animate, 1)  # Call this function again after 16 milliseconds (~60 FPS)

# Main function
def main():
    """Main function to initialize the OpenGL window and start the program."""
    glutInit(argv)  # Initialize GLUT
    glutInitWindowSize(win, win)  # Set the window size
    glutInitDisplayMode(GLUT_RGB)  # Set the display mode to RGB
    glutCreateWindow("Ball in Bowl")  # Create the window with a title
    glutDisplayFunc(draw)  # Register the draw function as the rendering callback
    glutTimerFunc(0, animate, 0)  # Start the animation timer
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-win, win, -win, win)  # Set up a 2D orthographic projection
    glutMainLoop()  # Enter the GLUT event processing loop

# Entry point of the program
main()
# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions (e.g., sin, cos)
import time  # For time-based animation

# Boat parameters
boat_x = 0.0  # Horizontal position of the boat
boat_y = -0.5  # Vertical position of the boat
oar_angle = 0.0  # Rotation angle of the oars
oar_speed = 2.0  # Speed of the oar rotation
water_level = -0.6  # Vertical position of the water surface
boat_speed = 0.005  # Speed of the boat movement

# Function to draw the boat
def draw_boat():
    """Draw the boat as a brown polygon."""
    glColor3f(0.5, 0.3, 0.1)  # Set the color to brown
    glBegin(GL_POLYGON)  # Start drawing a filled polygon
    glVertex2f(-0.3, 0.1)  # Top-left corner
    glVertex2f(0.3, 0.1)  # Top-right corner
    glVertex2f(0.2, -0.1)  # Bottom-right corner
    glVertex2f(-0.2, -0.1)  # Bottom-left corner
    glEnd()  # End drawing the polygon

# Function to draw the person rowing the boat
def draw_person():
    """Draw a person as a stick figure."""
    glColor3f(0.0, 0.0, 0.0)  # Set the color to black

    # Draw the head (a circle)
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    for i in range(0, 360, 10):  # Loop through 360 degrees in steps of 10
        glVertex2f(0.0 + 0.05 * math.cos(math.radians(i)), 0.2 + 0.05 * math.sin(math.radians(i)))  # Calculate points on the circle
    glEnd()  # End drawing the circle

    # Draw the body (a line)
    glBegin(GL_LINES)  # Start drawing lines
    glVertex2f(0.0, 0.2)  # Top of the body
    glVertex2f(0.0, 0.0)  # Bottom of the body
    glEnd()  # End drawing lines

    # Draw the arms (two lines)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.1)  # Shoulder
    glVertex2f(-0.1, 0.2)  # Left arm
    glVertex2f(0.0, 0.1)  # Shoulder
    glVertex2f(0.1, 0.2)  # Right arm
    glEnd()

    # Draw the legs (two lines)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)  # Hip
    glVertex2f(-0.1, -0.1)  # Left leg
    glVertex2f(0.0, 0.0)  # Hip
    glVertex2f(0.1, -0.1)  # Right leg
    glEnd()

# Function to draw an oar
def draw_oar(x, y, angle):
    """Draw an oar at position (x, y) with a given rotation angle."""
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(x, y, 0.0)  # Move to the oar's position
    glRotatef(angle, 0.0, 0.0, 1.0)  # Rotate the oar
    glColor3f(0.0, 0.0, 0.0)  # Set the color to black

    # Draw the oar handle (a line)
    glBegin(GL_LINES)
    glVertex2f(0.0, 0.0)  # Top of the handle
    glVertex2f(0.0, -0.3)  # Bottom of the handle
    glEnd()

    # Draw the oar blade (a rectangle)
    glBegin(GL_POLYGON)
    glVertex2f(-0.02, -0.3)  # Top-left corner
    glVertex2f(0.02, -0.3)  # Top-right corner
    glVertex2f(0.02, -0.5)  # Bottom-right corner
    glVertex2f(-0.02, -0.5)  # Bottom-left corner
    glEnd()

    glPopMatrix()  # Restore the previous transformation matrix

# Function to draw the water
def draw_water():
    """Draw the water as a blue rectangle."""
    glColor3f(0.0, 0.0, 1.0)  # Set the color to blue
    glBegin(GL_POLYGON)  # Start drawing a filled rectangle
    glVertex2f(-1.0, water_level)  # Top-left corner
    glVertex2f(1.0, water_level)  # Top-right corner
    glVertex2f(1.0, -1.0)  # Bottom-right corner
    glVertex2f(-1.0, -1.0)  # Bottom-left corner
    glEnd()  # End drawing the rectangle

# Function to update the animation
def update(value):
    """Update the oar angle and boat position."""
    global oar_angle, boat_x

    # Animate oars using a sine wave
    oar_angle = 30 * math.sin(math.radians(time.time() * oar_speed * 100))

    # Move the boat forward when the oars are pushing water
    if oar_angle > 0:  # Move boat when oars are in the correct position
        boat_x += boat_speed

    # Reset the boat position if it goes off-screen
    if boat_x > 1.0:
        boat_x = -1.0

    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    # Draw the water
    draw_water()

    # Draw the boat and person
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(boat_x, boat_y, 0.0)  # Move the boat to its current position
    draw_boat()  # Draw the boat
    draw_person()  # Draw the person

    # Draw the oars (only above water)
    if oar_angle > -15:  # Only draw oars when not submerged
        draw_oar(-0.2, 0.1, oar_angle)  # Left oar
        draw_oar(0.2, 0.1, -oar_angle)  # Right oar
    glPopMatrix()  # Restore the previous transformation matrix

    glutSwapBuffers()  # Swap buffers to display the rendered frame

# Function to handle window resizing
def reshape(width, height):
    """Handle window resizing."""
    glViewport(0, 0, width, height)  # Set the viewport to cover the new window size
    glMatrixMode(GL_PROJECTION)  # Switch to the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection

# Main function
def main():
    """Main function to initialize OpenGL and start the program."""
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow(b"Boat Rowing with Movement")  # Create the window with a title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glutDisplayFunc(display)  # Register the display function
    glutReshapeFunc(reshape)  # Register the reshape function
    glutTimerFunc(0, update, 0)  # Start the animation timer
    glutMainLoop()  # Enter the GLUT event processing loop

# Entry point of the program
if __name__ == "__main__":
    main()
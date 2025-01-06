# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions (e.g., sin, cos)
import time  # For time-based animation

# Stickman parameters
stickman_x = -0.8  # Initial horizontal position of the stickman
stickman_y = -0.5  # Initial vertical position of the stickman
leg_angle = 0.0  # Angle of the legs for running animation
arm_angle = 0.0  # Angle of the arms for running animation
knee_angle = 0.0  # Angle of the knees for running animation
slope_angle = 30  # Angle of the slope in degrees
running_speed = 200  # Speed of the running animation (higher value for smoother motion)

# Function to draw a filled circle
def draw_circle(x, y, radius, color):
    """Draw a filled circle at (x, y) with a given radius and color."""
    glColor3f(*color)  # Set the color
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    for angle in range(0, 360, 10):  # Loop through 360 degrees in steps of 10
        rad = math.radians(angle)  # Convert degrees to radians
        glVertex2f(x + radius * math.cos(rad), y + radius * math.sin(rad))  # Calculate points on the circle
    glEnd()  # End drawing the circle

# Function to draw a line
def draw_line(x1, y1, x2, y2, color):
    """Draw a line from (x1, y1) to (x2, y2) with a given color."""
    glColor3f(*color)  # Set the color
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(x1, y1)  # Start point of the line
    glVertex2f(x2, y2)  # End point of the line
    glEnd()  # End drawing the line

# Function to draw the stickman
def draw_stickman():
    """Draw the stickman with animated limbs."""
    global leg_angle, arm_angle, knee_angle  # Access global variables

    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(stickman_x, stickman_y, 0.0)  # Position the stickman

    # Draw the head (a yellow circle)
    draw_circle(0.0, 0.2, 0.05, (1.0, 1.0, 0.0))  # Yellow head

    # Draw the body (a blue line)
    draw_line(0.0, 0.2, 0.0, 0.0, (0.0, 0.0, 1.0))  # Blue body

    # Draw the arms (red lines)
    draw_arm(0.15, arm_angle, -1)  # Left arm
    draw_arm(0.15, -arm_angle, 1)  # Right arm

    # Draw the legs (green lines)
    draw_leg(leg_angle, knee_angle, -1)  # Left leg
    draw_leg(-leg_angle, -knee_angle, 1)  # Right leg

    glPopMatrix()  # Restore the previous transformation matrix

# Function to draw an arm
def draw_arm(shoulder_y, angle, direction):
    """Draw an arm with rotation."""
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(0.0, shoulder_y, 0.0)  # Move to the shoulder position
    glRotatef(direction * angle, 0.0, 0.0, 1.0)  # Rotate the arm
    draw_line(0.0, 0.0, direction * 0.1, -0.1, (1.0, 0.0, 0.0))  # Red arm
    glPopMatrix()  # Restore the previous transformation matrix

# Function to draw a leg
def draw_leg(angle, knee_angle, direction):
    """Draw a leg with bending knee."""
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(direction * angle, 0.0, 0.0, 1.0)  # Rotate the upper leg
    draw_line(0.0, 0.0, direction * 0.1, -0.2, (0.0, 1.0, 0.0))  # Green upper leg
    glTranslatef(direction * 0.1, -0.2, 0.0)  # Move to the knee position
    glRotatef(direction * knee_angle, 0.0, 0.0, 1.0)  # Rotate the lower leg
    draw_line(0.0, 0.0, direction * 0.1, -0.2, (0.0, 1.0, 0.0))  # Green lower leg
    glPopMatrix()  # Restore the previous transformation matrix

# Function to draw the slope
def draw_slope():
    """Draw the slope."""
    draw_line(-1.0, -0.5, 1.0, 0.5, (0.5, 0.5, 0.5))  # Gray slope

# Function to update the animation
def update(value):
    """Update animation parameters."""
    global leg_angle, arm_angle, knee_angle, stickman_x, stickman_y  # Access global variables

    # Animate limbs using sine and cosine functions
    t = time.time() * running_speed  # Time-based animation
    leg_angle = 30 * math.sin(math.radians(t))  # Animate legs
    arm_angle = 30 * math.cos(math.radians(t))  # Animate arms
    knee_angle = 20 * math.sin(math.radians(t * 2))  # Animate knees

    # Move stickman along the slope
    stickman_x += 0.01 * math.cos(math.radians(slope_angle))  # Update horizontal position
    stickman_y += 0.01 * math.sin(math.radians(slope_angle))  # Update vertical position

    # Reset position if stickman goes off-screen
    if stickman_x > 1.0:  # If stickman goes beyond the right edge
        stickman_x = -1.0  # Reset horizontal position
        stickman_y = -0.5  # Reset vertical position

    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_slope()  # Draw the slope
    draw_stickman()  # Draw the stickman
    glutSwapBuffers()  # Swap buffers for double buffering

# Function to handle window resizing
def reshape(width, height):
    """Adjust the viewport and projection."""
    glViewport(0, 0, width, height)  # Set the viewport to cover the new window size
    glMatrixMode(GL_PROJECTION)  # Switch to the projection matrix
    glLoadIdentity()  # Reset the projection matrix
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection

# Main function
def main():
    """Main function to set up the OpenGL environment."""
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow(b"Running Stickman on a Slope")  # Create the window with a title
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    glutDisplayFunc(display)  # Register the display function
    glutReshapeFunc(reshape)  # Register the reshape function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

# Entry point of the program
if __name__ == "__main__":
    main()
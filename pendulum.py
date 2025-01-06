# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions (e.g., sin, radians)
import sys  # For command-line arguments

# Initialize variables
angle = 30  # Initial angle of the swing (in degrees)
angle_velocity = 0  # Initial angular velocity
angle_acceleration = 0  # Initial angular acceleration
damping = 0.995  # Damping factor to reduce energy over time
gravity = 0.1  # Gravity effect (affects swing speed)
length = 0.5  # Length of the swing

# Function to draw the swing
def draw_swing():
    """Draw the swinging pendulum."""
    glPushMatrix()  # Save the current transformation matrix

    # Draw the swing rope (a line)
    glColor3f(0.8, 0.8, 0.8)  # Light gray color for the rope
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(0, 0)  # Top of the swing (pivot point)
    glVertex2f(length * math.sin(math.radians(angle)), -length * math.cos(math.radians(angle)))  # Bottom of the swing
    glEnd()  # End drawing the line

    # Draw the bob (the circular seat of the swing)
    glColor3f(0.9, 0.1, 0.1)  # Red color for the bob
    glPushMatrix()  # Save the current transformation matrix
    glTranslatef(length * math.sin(math.radians(angle)), -length * math.cos(math.radians(angle)), 0)  # Position the bob
    glutSolidSphere(0.05, 20, 20)  # Draw the bob (sphere)
    glPopMatrix()  # Restore the previous transformation matrix

    glPopMatrix()  # Restore the previous transformation matrix

# Function to update the pendulum's motion
def update(value):
    """Update the pendulum's angle and velocity."""
    global angle, angle_velocity, angle_acceleration, gravity, damping

    # Simple harmonic motion formula (Pendulum)
    angle_acceleration = -gravity * math.sin(math.radians(angle)) / length  # Calculate angular acceleration
    angle_velocity += angle_acceleration  # Update angular velocity
    angle_velocity *= damping  # Apply damping (friction)
    angle += angle_velocity  # Update the angle

    # Limit the angle to avoid it flipping
    if angle > 60:  # If the angle exceeds 60 degrees
        angle = 60  # Set the angle to 60 degrees
        angle_velocity *= -1  # Reverse the direction

    if angle < -60:  # If the angle goes below -60 degrees
        angle = -60  # Set the angle to -60 degrees
        angle_velocity *= -1  # Reverse the direction

    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_swing()  # Draw the swinging pendulum
    glutSwapBuffers()  # Swap buffers for double buffering

# Main function
def main():
    """Main function to initialize OpenGL and start the program."""
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow("Swinging Pendulum")  # Create the window with a title
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

# Entry point of the program
if __name__ == "__main__":
    main()
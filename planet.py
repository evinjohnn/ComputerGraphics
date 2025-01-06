# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions (e.g., cos, sin)

# Initialize variables
planet_angle = 0  # Angle of the planet's orbit
planet_distance = 0.7  # Distance from the sun
planet_speed = 1  # Speed of the planet's orbit

# Function to draw the sun
def draw_sun():
    """Draw the sun as a yellow circle."""
    glColor3f(1.0, 1.0, 0.0)  # Set the color to yellow
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    glVertex2f(0, 0)  # Center of the sun
    for i in range(0, 361, 10):  # Loop through 360 degrees in steps of 10
        glVertex2f(0.2 * math.cos(math.radians(i)), 0.2 * math.sin(math.radians(i)))  # Calculate points on the circle
    glEnd()  # End drawing the circle

# Function to draw the planet
def draw_planet():
    """Draw the planet as a blue circle orbiting the sun."""
    global planet_angle
    glPushMatrix()  # Save the current transformation matrix
    glRotatef(planet_angle, 0, 0, 1)  # Rotate the planet around the sun
    glTranslatef(planet_distance, 0, 0)  # Position the planet
    glColor3f(0.0, 0.0, 1.0)  # Set the color to blue
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    glVertex2f(0, 0)  # Center of the planet
    for i in range(0, 361, 10):  # Loop through 360 degrees in steps of 10
        glVertex2f(0.1 * math.cos(math.radians(i)), 0.1 * math.sin(math.radians(i)))  # Calculate points on the circle
    glEnd()  # End drawing the circle
    glPopMatrix()  # Restore the previous transformation matrix

# Function to update the planet's position
def update(value):
    """Update the planet's angle for orbital motion."""
    global planet_angle
    planet_angle += planet_speed  # Increment the planet's angle
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_sun()  # Draw the sun
    draw_planet()  # Draw the planet
    glutSwapBuffers()  # Swap buffers for double buffering

# Main function
def main():
    """Main function to initialize OpenGL and start the program."""
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow("Planet Rotating Around the Sun")  # Create the window with a title
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

# Entry point of the program
if __name__ == "__main__":
    main()
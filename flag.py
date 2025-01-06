# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions (e.g., sin)

# Initialize variables
flag_width = 0.5  # Width of the flag
flag_height = 0.3  # Height of the flag
wave_amplitude = 0.05  # Amplitude of the flag's wave
wave_frequency = 0.05  # Reduced frequency for slower fluttering
time = 0  # Time variable for animation

# Function to draw the flag pole
def draw_pole():
    """Draw the flag pole."""
    glColor3f(0.5, 0.5, 0.5)  # Gray color for the pole
    glLineWidth(5.0)  # Thicker line for the pole

    # Main pole (longer part below the flag)
    glBegin(GL_LINES)
    glVertex2f(0.0, -1.0)  # Bottom of the pole (centered)
    glVertex2f(0.0, 0.0)   # Top of the main pole (at the base of the flag)
    glEnd()

    # Smaller pole above the flag
    glBegin(GL_LINES)
    glVertex2f(0.0, flag_height)  # Top of the flag
    glVertex2f(0.0, flag_height + 0.2)  # Top of the smaller pole
    glEnd()

# Function to draw the flag
def draw_flag():
    """Draw the fluttering flag."""
    glBegin(GL_QUAD_STRIP)  # Start drawing a quad strip
    for x in range(0, 100):  # Loop to create the wave effect
        x_norm = x / 100.0  # Normalize x to [0, 1]
        y_wave = wave_amplitude * math.sin(2 * math.pi * (x_norm - time))  # Calculate wave offset
        glColor3f(1.0, 0.0, 0.0)  # Red color for the flag
        glVertex2f(x_norm * flag_width, y_wave)  # Bottom edge of the flag
        glVertex2f(x_norm * flag_width, y_wave + flag_height)  # Top edge of the flag
    glEnd()  # End drawing the quad strip

# Function to update the animation
def update(value):
    """Update the flag's fluttering animation."""
    global time
    time += wave_frequency  # Increment time for wave animation
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_pole()  # Draw the flag pole
    draw_flag()  # Draw the fluttering flag
    glutSwapBuffers()  # Swap buffers for double buffering

# Main function
def main():
    """Main function to initialize OpenGL and start the program."""
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow("Flag Fluttering on a Pole")  # Create the window with a title
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

# Entry point of the program
if __name__ == "__main__":
    main()
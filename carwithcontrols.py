# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import sys  # For command-line arguments
import math  # For trigonometric functions (e.g., cos, sin)

# Initialize variables
car_x = 0.0  # Horizontal position of the car
car_y = 0.0  # Vertical position of the car
car_speed = 0.1  # Speed of the car
car_direction = 1  # Direction of the car (1 for right, -1 for left)
horn_on = False  # Flag to toggle the horn

# Function to draw the car
def draw_car():
    """Draw the car as a red rectangle with black wheels and an optional horn."""
    glColor3f(1.0, 0.0, 0.0)  # Set the color to red
    glBegin(GL_QUADS)  # Start drawing a filled rectangle
    glVertex2f(car_x - 0.2, car_y - 0.1)  # Bottom-left corner
    glVertex2f(car_x + 0.2, car_y - 0.1)  # Bottom-right corner
    glVertex2f(car_x + 0.2, car_y + 0.1)  # Top-right corner
    glVertex2f(car_x - 0.2, car_y + 0.1)  # Top-left corner
    glEnd()  # End drawing the rectangle

    # Draw the wheels (black circles)
    glColor3f(0.0, 0.0, 0.0)  # Set the color to black
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    glVertex2f(car_x - 0.15, car_y - 0.15)  # Center of the left wheel
    for i in range(0, 361, 10):  # Loop through 360 degrees in steps of 10
        glVertex2f(car_x - 0.15 + 0.05 * math.cos(math.radians(i)), car_y - 0.15 + 0.05 * math.sin(math.radians(i)))  # Calculate points on the circle
    glEnd()  # End drawing the circle

    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle
    glVertex2f(car_x + 0.15, car_y - 0.15)  # Center of the right wheel
    for i in range(0, 361, 10):  # Loop through 360 degrees in steps of 10
        glVertex2f(car_x + 0.15 + 0.05 * math.cos(math.radians(i)), car_y - 0.15 + 0.05 * math.sin(math.radians(i)))  # Calculate points on the circle
    glEnd()  # End drawing the circle

    # Draw the horn if it is turned on
    if horn_on:
        glColor3f(1.0, 1.0, 0.0)  # Set the color to yellow
        glBegin(GL_TRIANGLES)  # Start drawing a filled triangle
        glVertex2f(car_x + 0.2, car_y + 0.1)  # Bottom-left corner of the horn
        glVertex2f(car_x + 0.3, car_y + 0.1)  # Bottom-right corner of the horn
        glVertex2f(car_x + 0.2, car_y + 0.2)  # Top corner of the horn
        glEnd()  # End drawing the triangle

# Function to handle keyboard input
def keyboard(key, x, y):
    """Handle keyboard input to control the car."""
    global car_direction, car_speed, horn_on  # Access global variables
    if key == b'a':  # Move left
        car_direction = -1
    elif key == b'd':  # Move right
        car_direction = 1
    elif key == b'w':  # Increase speed
        car_speed += 0.05
    elif key == b's':  # Decrease speed
        car_speed -= 0.05
    elif key == b'h':  # Toggle horn
        horn_on = not horn_on
    glutPostRedisplay()  # Request a redraw of the scene

# Function to update the car's position
def update(value):
    """Update the car's position based on its speed and direction."""
    global car_x  # Access global variables
    car_x += car_direction * car_speed * 0.01  # Move the car
    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_car()  # Draw the car
    glutSwapBuffers()  # Swap buffers for double buffering

# Main function
def main():
    """Main function to initialize OpenGL and start the program."""
    glutInit(sys.argv)  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set the display mode to RGB with double buffering
    glutInitWindowSize(500, 500)  # Set the window size to 500x500 pixels
    glutCreateWindow("Car Motion with Controls")  # Create the window with a title
    glClearColor(1, 1, 1, 1)  # Set the background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set up a 2D orthographic projection
    glutDisplayFunc(display)  # Register the display function
    glutKeyboardFunc(keyboard)  # Register the keyboard function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

# Entry point of the program
if __name__ == "__main__":
    main()
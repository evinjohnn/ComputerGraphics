# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric calculations (e.g., drawing circles)

# Global variables for ball positions and velocities
red_x = -0.8  # Red ball starts at x = -0.8 (left side)
yellow_x = 0.0  # Yellow ball starts at x = 0.0 (middle)
purple_x = 0.8  # Purple ball starts at x = 0.8 (right side)
red_v = 0.01  # Red ball's initial velocity (moving right)
yellow_v = 0.0  # Yellow ball's initial velocity (stationary)
purple_v = 0.0  # Purple ball's initial velocity (stationary)

# State flags to control ball movement and collisions
red_moving = True  # Red ball is initially moving
yellow_moving = False  # Yellow ball is initially stationary
purple_moving = False  # Purple ball is initially stationary
collision_occurred = False  # Flag to track if the first collision has happened
second_collision = False  # Flag to track if the second collision has happened

# Animation parameters
slowdown_factor = 0.995  # Friction factor to gradually slow down the purple ball

# Function to draw a ball at a given position with a specified color
def draw_ball(x, y, radius, r, g, b):
    """Draw a ball at position (x, y) with given color and radius."""
    glColor3f(r, g, b)  # Set the color of the ball
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a filled circle using a triangle fan
    glVertex2f(x, y)  # Center of the circle
    for i in range(0, 361, 10):  # Loop through 360 degrees in steps of 10
        angle = math.radians(i)  # Convert degrees to radians
        glVertex2f(x + radius * math.cos(angle), y + radius * math.sin(angle))  # Calculate points on the circumference
    glEnd()  # End drawing the circle

# Function to draw the collision path line
def draw_path():
    """Draw a horizontal line representing the path of the balls."""
    glColor3f(0.8, 0.8, 0.8)  # Set the color of the line (light gray)
    glBegin(GL_LINES)  # Start drawing a line
    glVertex2f(-1.0, 0.0)  # Left endpoint of the line
    glVertex2f(1.0, 0.0)  # Right endpoint of the line
    glEnd()  # End drawing the line

# Function to update ball positions and handle collisions
def update(value):
    """Update ball positions and handle collisions."""
    global red_x, yellow_x, purple_x, red_v, yellow_v, purple_v  # Access global variables
    global red_moving, yellow_moving, purple_moving  # Access global state flags
    global collision_occurred, second_collision  # Access global collision flags

    # Update positions based on velocities
    if red_moving:  # If the red ball is moving
        red_x += red_v  # Move the red ball by its velocity

    if yellow_moving:  # If the yellow ball is moving
        yellow_x += yellow_v  # Move the yellow ball by its velocity

    if purple_moving:  # If the purple ball is moving
        purple_x += purple_v  # Move the purple ball by its velocity
        if abs(purple_v) > 0.0001:  # If the purple ball is moving significantly
            purple_v *= slowdown_factor  # Apply friction to slow it down

    # First collision: Red ball hits Yellow ball
    if red_moving and not collision_occurred and abs(red_x - yellow_x) < 0.2:  # Check if red is close to yellow
        red_moving = False  # Stop the red ball
        yellow_moving = True  # Start the yellow ball
        yellow_v = red_v  # Transfer red's velocity to yellow
        purple_moving = True  # Start the purple ball
        purple_v = -0.01  # Set purple's velocity to move left
        collision_occurred = True  # Mark the first collision as occurred

    # Second collision: Yellow ball hits Purple ball
    if collision_occurred and not second_collision and abs(yellow_x - purple_x) < 0.2:  # Check if yellow is close to purple
        yellow_moving = False  # Stop the yellow ball
        yellow_v = 0  # Set yellow's velocity to zero
        purple_v = 0.01  # Reverse purple's direction to move right
        second_collision = True  # Mark the second collision as occurred

    # Stop the purple ball when it's moving very slowly
    if second_collision and abs(purple_v) < 0.0001:  # Check if purple's velocity is negligible
        purple_moving = False  # Stop the purple ball
        purple_v = 0  # Set purple's velocity to zero

    glutPostRedisplay()  # Request a redraw of the scene
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (~60 FPS)

# Function to render the scene
def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen

    draw_path()  # Draw the collision path line

    # Draw the three balls at their current positions
    draw_ball(red_x, 0.0, 0.1, 1.0, 0.0, 0.0)  # Red ball
    draw_ball(yellow_x, 0.0, 0.1, 1.0, 1.0, 0.0)  # Yellow ball
    draw_ball(purple_x, 0.0, 0.1, 0.5, 0.0, 0.5)  # Purple ball

    glutSwapBuffers()  # Swap buffers to display the rendered frame

# Main function to initialize the OpenGL window and start the program
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set up double buffering and RGB color mode
    glutInitWindowSize(800, 400)  # Set the window size to 800x400 pixels
    glutCreateWindow(b"Three Ball Collision Sequence")  # Create the window with a title

    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set the background color to white
    gluOrtho2D(-1.2, 1.2, -0.6, 0.6)  # Set up a 2D orthographic projection

    glutDisplayFunc(display)  # Register the display function as the rendering callback
    glutTimerFunc(0, update, 0)  # Start the animation timer
    glutMainLoop()  # Enter the GLUT event processing loop

# Entry point of the program
if __name__ == "__main__":
    main()  # Run the main function
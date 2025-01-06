# Import necessary libraries
from OpenGL.GL import *  # Core OpenGL functions for rendering
from OpenGL.GLUT import *  # OpenGL Utility Toolkit for window management and input
from OpenGL.GLU import *  # OpenGL Utility Library for additional functionality
import math  # For trigonometric functions like sine and cosine
import time  # For tracking time and calculating delta time

# Define the YoYo class
class YoYo:
    def __init__(self):
        self.y = 0.25  # Initial vertical position of the yoyo (centered at the top)
        self.velocity = 0.0  # Initial velocity (starts at rest)
        self.gravity = 0.0006  # Gravity force pulling the yoyo down (reduced for slower fall)
        self.string_length = 0.4  # Length of the yoyo string
        self.state = "FALLING"  # Current state of the yoyo: "FALLING" or "RISING"
        self.spin_angle = 0.0  # Current rotation angle of the yoyo (in radians)
        self.spin_velocity = 10.0  # Speed at which the yoyo spins
        self.string_wound = 0.0  # Amount of string wound around the yoyo
        self.last_update = time.time()  # Time of the last update (used for delta time)
        self.sleep_time = 0.0  # Not used in this code
        self.bounce_factor = -0.8  # Energy retention after bouncing (80% of velocity retained)

    def update(self):
        current_time = time.time()  # Get the current time
        delta_time = (current_time - self.last_update) * 60  # Calculate delta time (scaled for smooth animation)
        self.last_update = current_time  # Update the last update time

        if self.state == "FALLING":  # If the yoyo is falling
            self.velocity -= self.gravity * delta_time  # Apply gravity to increase downward velocity
            new_y = self.y + self.velocity * delta_time  # Calculate new y position

            # Bottom boundary (bounce)
            if new_y <= -0.25:  # If the yoyo hits the bottom boundary
                self.y = -0.25  # Set y to the bottom boundary
                self.velocity *= self.bounce_factor  # Reverse velocity with bounce factor
                self.spin_velocity = 15.0  # Increase spin speed after bouncing
            else:
                self.y = new_y  # Update y position

            self.spin_angle += self.spin_velocity * delta_time  # Update spin angle
            self.string_wound += abs(self.velocity) * 0.1  # Wind the string around the yoyo

        elif self.state == "RISING":  # If the yoyo is rising
            self.velocity -= self.gravity * 0.5 * delta_time  # Apply reduced gravity to slow down the rise
            new_y = self.y + self.velocity * delta_time  # Calculate new y position

            # Top boundary (bounce)
            if new_y >= 0.25:  # If the yoyo hits the top boundary
                self.y = 0.25  # Set y to the top boundary
                self.velocity *= self.bounce_factor  # Reverse velocity with bounce factor
            else:
                self.y = new_y  # Update y position

            self.spin_angle += self.spin_velocity * delta_time  # Update spin angle
            self.string_wound = max(0, self.string_wound - abs(self.velocity) * 0.1)  # Unwind the string

# Function to draw the yoyo and its string
def draw_yoyo(yoyo):
    x = 0  # X-coordinate of the yoyo (centered horizontally)

    # Draw string
    glColor3f(0.9, 0.9, 0.9)  # Set string color to light gray
    glLineWidth(2.0)  # Set line thickness

    # Adjusted control points for tighter curve
    if yoyo.state == "FALLING":
        ctrl1_x = -0.1 * (0.25 - yoyo.y) / yoyo.string_length  # Control point 1 for falling state
        ctrl2_x = 0.05 * (0.25 - yoyo.y) / yoyo.string_length  # Control point 2 for falling state
    else:
        ctrl1_x = -0.05 * (0.25 - yoyo.y) / yoyo.string_length  # Control point 1 for rising state
        ctrl2_x = 0.025 * (0.25 - yoyo.y) / yoyo.string_length  # Control point 2 for rising state

    # Draw main string using a Bezier curve
    glBegin(GL_LINE_STRIP)  # Start drawing a line strip
    steps = 30  # Number of steps for the curve
    for i in range(steps + 1):  # Loop through each step
        t = i / float(steps)  # Calculate interpolation factor (0 to 1)
        # Calculate x and y coordinates using Bezier formula
        px = x + (1 - t) ** 3 * 0 + 3 * t * (1 - t) ** 2 * ctrl1_x + 3 * t ** 2 * (1 - t) * ctrl2_x + t ** 3 * 0
        py = 0.25 * (1 - t) + yoyo.y * t  # Interpolate y-coordinate
        glVertex2f(px, py)  # Add vertex to the line strip
    glEnd()  # End drawing the line strip

    # Draw wound string (if any)
    if yoyo.string_wound > 0:
        glBegin(GL_LINE_STRIP)  # Start drawing a line strip
        for i in range(15):  # Loop to draw the wound string
            angle = yoyo.spin_angle + i * math.pi / 7  # Calculate angle for each point
            r = 0.03 + (yoyo.string_wound * 0.01) * (i / 15.0)  # Calculate radius for spiral effect
            glVertex2f(x + r * math.cos(angle), yoyo.y + r * math.sin(angle))  # Add vertex
        glEnd()  # End drawing the line strip

    # Draw yoyo body (smaller radius)
    radius = 0.05  # Radius of the yoyo
    glColor3f(0.8, 0.2, 0.2)  # Set yoyo color to red

    # Main disc
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a triangle fan
    glVertex2f(x, yoyo.y)  # Center of the yoyo
    for i in range(0, 361, 10):  # Loop to draw the disc
        angle = math.radians(i) + yoyo.spin_angle  # Calculate angle for each vertex
        glVertex2f(x + radius * math.cos(angle), yoyo.y + radius * math.sin(angle))  # Add vertex
    glEnd()  # End drawing the triangle fan

    # Decorative pattern (spokes)
    glColor3f(1.0, 1.0, 1.0)  # Set spoke color to white
    glBegin(GL_LINES)  # Start drawing lines
    for i in range(0, 360, 45):  # Loop to draw spokes
        angle = math.radians(i) + yoyo.spin_angle  # Calculate angle for each spoke
        glVertex2f(x, yoyo.y)  # Center of the yoyo
        glVertex2f(x + radius * math.cos(angle), yoyo.y + radius * math.sin(angle))  # End of spoke
    glEnd()  # End drawing lines

    # Center hub
    glColor3f(0.9, 0.9, 0.9)  # Set hub color to light gray
    glBegin(GL_TRIANGLE_FAN)  # Start drawing a triangle fan
    glVertex2f(x, yoyo.y)  # Center of the yoyo
    for i in range(0, 361, 10):  # Loop to draw the hub
        angle = math.radians(i) + yoyo.spin_angle  # Calculate angle for each vertex
        glVertex2f(x + (radius * 0.2) * math.cos(angle), yoyo.y + (radius * 0.2) * math.sin(angle))  # Add vertex
    glEnd()  # End drawing the triangle fan

# Create a global yoyo object
yoyo = YoYo()

# Function to update the yoyo's state
def update(value):
    yoyo.update()  # Update yoyo's position and state
    glutPostRedisplay()  # Request a redraw
    glutTimerFunc(16, update, 0)  # Call this function again after 16 milliseconds (60 FPS)

# Function to display the scene
def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Clear the screen
    draw_yoyo(yoyo)  # Draw the yoyo
    glutSwapBuffers()  # Swap buffers for smooth rendering

# Function to handle window resizing
def reshape(width, height):
    size = min(width, height)  # Ensure square viewport
    glViewport((width - size) // 2, (height - size) // 2, size, size)  # Set viewport to maintain aspect ratio

# Main function
def main():
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Set display mode (double buffering and RGB)
    glutInitWindowSize(500, 500)  # Set window size
    glutCreateWindow(b"Yoyo Animation with Bouncing")  # Create window with title

    glClearColor(0.2, 0.2, 0.2, 1.0)  # Set background color to dark gray
    gluOrtho2D(-0.3, 0.3, -0.3, 0.3)  # Set up 2D orthographic projection

    glutDisplayFunc(display)  # Register display callback
    glutReshapeFunc(reshape)  # Register reshape callback
    glutTimerFunc(0, update, 0)  # Start the animation timer
    glutMainLoop()  # Enter the main event loop

# Entry point
if __name__ == "__main__":
    main()
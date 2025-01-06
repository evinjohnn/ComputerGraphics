from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import sys

# Initialize variables
angle = 30  # Initial angle of the swing (in degrees)
angle_velocity = 0  # Initial angular velocity
angle_acceleration = 0  # Initial angular acceleration
damping = 0.995  # Damping factor to reduce energy over time
gravity = 0.1  # Gravity effect (affects swing speed)
length = 0.5  # Length of the swing

def draw_swing():
    glPushMatrix()  # Save the current matrix

    # Draw the swing rope (a line)
    glColor3f(0.8, 0.8, 0.8)  # Light gray color for the rope
    glBegin(GL_LINES)
    glVertex2f(0, 0)  # Top of the swing (pivot point)
    glVertex2f(length * math.sin(math.radians(angle)), -length * math.cos(math.radians(angle)))  # Bottom of the swing
    glEnd()

    # Draw the bob (the circular seat of the swing)
    glColor3f(0.9, 0.1, 0.1)  # Red color for the bob
    glPushMatrix()
    glTranslatef(length * math.sin(math.radians(angle)), -length * math.cos(math.radians(angle)), 0)  # Position the bob
    glutSolidSphere(0.05, 20, 20)  # Draw the bob (sphere)
    glPopMatrix()

    glPopMatrix()  # Restore the matrix

def update(value):
    global angle, angle_velocity, angle_acceleration, gravity, damping

    # Simple harmonic motion formula (Pendulum)
    angle_acceleration = -gravity * math.sin(math.radians(angle)) / length
    angle_velocity += angle_acceleration  # Update angular velocity
    angle_velocity *= damping  # Apply damping (friction)
    angle += angle_velocity  # Update the angle

    # Limit the angle to avoid it flipping
    if angle > 60:
        angle = 60
        angle_velocity *= -1  # Reverse direction when it reaches max angle

    if angle < -60:
        angle = -60
        angle_velocity *= -1  # Reverse direction when it reaches min angle

    glutPostRedisplay()  # Request a redraw
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_swing()  # Draw the swing
    glutSwapBuffers()  # Swap buffers for double buffering

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering
    glutInitWindowSize(500, 500)
    glutCreateWindow("Swinging Pendulum")
    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set orthogonal projection
    glutDisplayFunc(display)  # Register the display function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
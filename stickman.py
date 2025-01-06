from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

# Stickman parameters
stickman_x = -0.8  # Initial position
stickman_y = -0.5
leg_angle = 0.0
arm_angle = 0.0
knee_angle = 0.0
slope_angle = 30  # Slope angle in degrees
running_speed = 200  # Higher value for smoother motion

def draw_circle(x, y, radius, color):
    """Draw a filled circle at (x, y) with a given radius and color."""
    glColor3f(*color)
    glBegin(GL_TRIANGLE_FAN)
    for angle in range(0, 360, 10):
        rad = math.radians(angle)
        glVertex2f(x + radius * math.cos(rad), y + radius * math.sin(rad))
    glEnd()

def draw_line(x1, y1, x2, y2, color):
    """Draw a line from (x1, y1) to (x2, y2) with a given color."""
    glColor3f(*color)
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw_stickman():
    """Draw the stickman with animated limbs."""
    global leg_angle, arm_angle, knee_angle

    glPushMatrix()
    glTranslatef(stickman_x, stickman_y, 0.0)  # Position the stickman

    # Head
    draw_circle(0.0, 0.2, 0.05, (1.0, 1.0, 0.0))  # Yellow head

    # Body
    draw_line(0.0, 0.2, 0.0, 0.0, (0.0, 0.0, 1.0))  # Blue body

    # Arms
    draw_arm(0.15, arm_angle, -1)
    draw_arm(0.15, -arm_angle, 1)

    # Legs
    draw_leg(leg_angle, knee_angle, -1)
    draw_leg(-leg_angle, -knee_angle, 1)

    glPopMatrix()

def draw_arm(shoulder_y, angle, direction):
    """Draw an arm with rotation."""
    glPushMatrix()
    glTranslatef(0.0, shoulder_y, 0.0)
    glRotatef(direction * angle, 0.0, 0.0, 1.0)
    draw_line(0.0, 0.0, direction * 0.1, -0.1, (1.0, 0.0, 0.0))  # Red arms
    glPopMatrix()

def draw_leg(angle, knee_angle, direction):
    """Draw a leg with bending knee."""
    glPushMatrix()
    glRotatef(direction * angle, 0.0, 0.0, 1.0)
    draw_line(0.0, 0.0, direction * 0.1, -0.2, (0.0, 1.0, 0.0))  # Green upper leg
    glTranslatef(direction * 0.1, -0.2, 0.0)
    glRotatef(direction * knee_angle, 0.0, 0.0, 1.0)
    draw_line(0.0, 0.0, direction * 0.1, -0.2, (0.0, 1.0, 0.0))  # Green lower leg
    glPopMatrix()

def draw_slope():
    """Draw the slope."""
    draw_line(-1.0, -0.5, 1.0, 0.5, (0.5, 0.5, 0.5))  # Gray slope

def update(value):
    """Update animation parameters."""
    global leg_angle, arm_angle, knee_angle, stickman_x, stickman_y

    # Animate limbs
    t = time.time() * running_speed
    leg_angle = 30 * math.sin(math.radians(t))
    arm_angle = 30 * math.cos(math.radians(t))
    knee_angle = 20 * math.sin(math.radians(t * 2))

    # Move stickman along the slope
    stickman_x += 0.01 * math.cos(math.radians(slope_angle))
    stickman_y += 0.01 * math.sin(math.radians(slope_angle))

    # Reset position if stickman goes off-screen
    if stickman_x > 1.0:
        stickman_x = -1.0
        stickman_y = -0.5

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    """Render the scene."""
    glClear(GL_COLOR_BUFFER_BIT)
    draw_slope()
    draw_stickman()
    glutSwapBuffers()

def reshape(width, height):
    """Adjust the viewport and projection."""
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)

def main():
    """Main function to set up the OpenGL environment."""
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Running Stickman on a Slope")
    glClearColor(1.0, 1.0, 1.0, 1.0)  # White background
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()

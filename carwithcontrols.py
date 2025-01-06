from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import math  # Import the math module

# Initialize variables
car_x = 0.0
car_y = 0.0
car_speed = 0.1
car_direction = 1  # 1 for right, -1 for left
horn_on = False

def draw_car():
    glColor3f(1.0, 0.0, 0.0)  # Red color for the car
    glBegin(GL_QUADS)
    glVertex2f(car_x - 0.2, car_y - 0.1)
    glVertex2f(car_x + 0.2, car_y - 0.1)
    glVertex2f(car_x + 0.2, car_y + 0.1)
    glVertex2f(car_x - 0.2, car_y + 0.1)
    glEnd()

    # Draw wheels
    glColor3f(0.0, 0.0, 0.0)  # Black color for wheels
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(car_x - 0.15, car_y - 0.15)
    for i in range(0, 361, 10):
        glVertex2f(car_x - 0.15 + 0.05 * math.cos(math.radians(i)), car_y - 0.15 + 0.05 * math.sin(math.radians(i)))
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(car_x + 0.15, car_y - 0.15)
    for i in range(0, 361, 10):
        glVertex2f(car_x + 0.15 + 0.05 * math.cos(math.radians(i)), car_y - 0.15 + 0.05 * math.sin(math.radians(i)))
    glEnd()

    # Draw horn if on
    if horn_on:
        glColor3f(1.0, 1.0, 0.0)  # Yellow color for horn
        glBegin(GL_TRIANGLES)
        glVertex2f(car_x + 0.2, car_y + 0.1)
        glVertex2f(car_x + 0.3, car_y + 0.1)
        glVertex2f(car_x + 0.2, car_y + 0.2)
        glEnd()

def keyboard(key, x, y):
    global car_direction, car_speed, horn_on
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
    glutPostRedisplay()

def update(value):
    global car_x
    car_x += car_direction * car_speed * 0.01
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # Timer for next frame (60 FPS)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_car()  # Draw the car
    glutSwapBuffers()  # Swap buffers for double buffering

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)  # Use double buffering
    glutInitWindowSize(500, 500)
    glutCreateWindow("Car Motion with Controls")
    glClearColor(1, 1, 1, 1)  # Set background color to white
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)  # Set orthogonal projection
    glutDisplayFunc(display)  # Register the display function
    glutKeyboardFunc(keyboard)  # Register the keyboard function
    glutTimerFunc(0, update, 0)  # Start the update function
    glutMainLoop()  # Enter the GLUT main loop

if __name__ == "__main__":
    main()
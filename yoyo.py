from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import time

class YoYo:
    def __init__(self):
        self.y = 0.25                # Initial position
        self.velocity = 0.0          # Initial velocity
        self.gravity = 0.0006        # Reduced gravity
        self.string_length = 0.4     # Reduced string length
        self.state = "FALLING"
        self.spin_angle = 0.0
        self.spin_velocity = 10.0
        self.string_wound = 0.0
        self.last_update = time.time()
        self.sleep_time = 0.0
        self.bounce_factor = -0.8    # Bounce energy retention (80%)

    def update(self):
        current_time = time.time()
        delta_time = (current_time - self.last_update) * 60
        self.last_update = current_time

        if self.state == "FALLING":
            self.velocity -= self.gravity * delta_time
            new_y = self.y + self.velocity * delta_time

            # Bottom boundary (bounce)
            if new_y <= -0.25:
                self.y = -0.25
                self.velocity *= self.bounce_factor  # Reverse velocity with bounce factor
                self.spin_velocity = 15.0
            else:
                self.y = new_y

            self.spin_angle += self.spin_velocity * delta_time
            self.string_wound += abs(self.velocity) * 0.1

        elif self.state == "RISING":
            self.velocity -= self.gravity * 0.5 * delta_time
            new_y = self.y + self.velocity * delta_time

            # Top boundary (bounce)
            if new_y >= 0.25:
                self.y = 0.25
                self.velocity *= self.bounce_factor  # Reverse velocity with bounce factor
            else:
                self.y = new_y

            self.spin_angle += self.spin_velocity * delta_time
            self.string_wound = max(0, self.string_wound - abs(self.velocity) * 0.1)

def draw_yoyo(yoyo):
    x = 0

    # Draw string
    glColor3f(0.9, 0.9, 0.9)
    glLineWidth(2.0)

    # Adjusted control points for tighter curve
    if yoyo.state == "FALLING":
        ctrl1_x = -0.1 * (0.25 - yoyo.y) / yoyo.string_length
        ctrl2_x = 0.05 * (0.25 - yoyo.y) / yoyo.string_length
    else:
        ctrl1_x = -0.05 * (0.25 - yoyo.y) / yoyo.string_length
        ctrl2_x = 0.025 * (0.25 - yoyo.y) / yoyo.string_length

    # Draw main string
    glBegin(GL_LINE_STRIP)
    steps = 30
    for i in range(steps + 1):
        t = i / float(steps)
        px = x + (1-t)**3 * 0 + 3*t*(1-t)**2 * ctrl1_x + 3*t**2*(1-t) * ctrl2_x + t**3 * 0
        py = 0.25 * (1-t) + yoyo.y * t
        glVertex2f(px, py)
    glEnd()

    # Draw wound string
    if yoyo.string_wound > 0:
        glBegin(GL_LINE_STRIP)
        for i in range(15):
            angle = yoyo.spin_angle + i * math.pi / 7
            r = 0.03 + (yoyo.string_wound * 0.01) * (i / 15.0)
            glVertex2f(x + r * math.cos(angle),
                      yoyo.y + r * math.sin(angle))
        glEnd()

    # Draw yoyo body (smaller radius)
    radius = 0.05
    glColor3f(0.8, 0.2, 0.2)

    # Main disc
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, yoyo.y)
    for i in range(0, 361, 10):
        angle = math.radians(i) + yoyo.spin_angle
        glVertex2f(x + radius * math.cos(angle),
                  yoyo.y + radius * math.sin(angle))
    glEnd()

    # Decorative pattern
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for i in range(0, 360, 45):
        angle = math.radians(i) + yoyo.spin_angle
        glVertex2f(x, yoyo.y)
        glVertex2f(x + radius * math.cos(angle),
                  yoyo.y + radius * math.sin(angle))
    glEnd()

    # Center hub
    glColor3f(0.9, 0.9, 0.9)
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(x, yoyo.y)
    for i in range(0, 361, 10):
        angle = math.radians(i) + yoyo.spin_angle
        glVertex2f(x + (radius * 0.2) * math.cos(angle),
                  yoyo.y + (radius * 0.2) * math.sin(angle))
    glEnd()

yoyo = YoYo()

def update(value):
    yoyo.update()
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_yoyo(yoyo)
    glutSwapBuffers()

def reshape(width, height):
    # Ensure square viewport
    size = min(width, height)
    glViewport((width - size) // 2, (height - size) // 2, size, size)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"Yoyo Animation with Bouncing")

    glClearColor(0.2, 0.2, 0.2, 1.0)
    gluOrtho2D(-0.3, 0.3, -0.3, 0.3)  # Tighter coordinate system

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
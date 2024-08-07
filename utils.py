from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

import reimplementation
import time

def drawRectangle(length: float, width: float, height: float, color=(1, 1, 1), cube_size=0.1):
    """
    Draws a rectangle using smaller cubes.

    Args:
        length: Length of the rectangle.
        width: Width of the rectangle.
        height: Height of the rectangle.
        color: Optional color tuple (red, green, blue) of the rectangle. Defaults to white.
        cube_size: Size of each individual cube.
    """

    # Calcula o número de cubos necessários em cada dimensão
    num_cubes_x = int(length / cube_size)
    num_cubes_y = int(width / cube_size)

    for i in range(num_cubes_x):
        for j in range(num_cubes_y):
            # Calcula a posição do cubo
            x = -length/2 + i * cube_size + cube_size/2
            y = -width/2 + j * cube_size + cube_size/2
            z = height/2

            # Desenha o cubo
            glPushMatrix()
            reimplementation.glTranslatef(x, y, z)
            glColor3f(*color)
            glutSolidCube(cube_size)
            glPopMatrix()

def drawRectanglePoints(
        length: float, 
        width: float, 
        height: float, 
        color=(1, 1, 1), 
        point_size=5.0, 
        point_spacing=0.05
        ):
    """
    Draws a rectangle using points.

    Args:
        length: Length of the rectangle.
        width: Width of the rectangle.
        height: Height of the rectangle.
        color: Optional color tuple (red, green, blue) of the rectangle. Defaults to white.
        point_size: Size of each individual point.
        point_spacing: Spacing between points.
    """

    # Calcula o número de pontos necessários em cada dimensão
    num_points_x = int(length / point_spacing)
    num_points_y = int(width / point_spacing)

    # Configura o tamanho do ponto
    glPointSize(point_size)

    # Define a cor do material dos pontos
    glMaterialfv(GL_FRONT, GL_AMBIENT, [c * 0.1 for c in color] + [1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, list(color) + [1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [c * 0.5 for c in color] + [1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [30.0])

    # Inicia a renderização de pontos
    glBegin(GL_POINTS)

    for i in range(num_points_x):
        for j in range(num_points_y):
            # Calcula a posição do ponto
            x = -length/2 + i * point_spacing + point_spacing/2
            y = -width/2 + j * point_spacing + point_spacing/2
            z = height/2

            glColor3f(*color)

            # Desenha o ponto
            glVertex3f(x, y, z)

    glEnd()


def drawOctagon(radius: float, height: float, color=(1, 1, 1)):
    """
    Draws an octagon using rectangles.

    Args:
    radius: Radius of the circumscribed circle of the octagon.
    height: Height of the octagon.
    color: Optional color tuple (red, green, blue) of the octagon. Defaults to white.
    """

    half_side_length = radius / math.sqrt(5.8)
    # Draw eight rectangles to form the octagon
    for i in range(8):
        # Calculate rotation angle for each rectangle
        angle = i * math.pi / 4

        x_center = 0
        y_center = 0

        # Draw the rectangle
        glPushMatrix()
        reimplementation.glTranslatef(x_center, y_center, height / 2)
        reimplementation.glRotatef(angle * 180 / math.pi, 0, 0, 1)  # Rotate the rectangle
        for i in range(3):
            reimplementation.glTranslatef(0, 0, 0.1)
            drawRectangle(radius, half_side_length, height, color)  # Adjusted value
        glPopMatrix()


step =0.1
eye = [.0, .0, 1.0]
center = [.0, .0, .0]
up = [1.0, 40.0, .0]

def keyboard(key, x, y):
    global eye, center, up, step
    if key == b'p':
        print(f"eye: {eye}, center: {center}, up: {up}")
    elif key == b'+':
        step += 0.1
        print(step)
    elif key == b'-':
        step -= 0.1
        print(step)
    elif key == b'x':
        eye[0] += step
    elif key == b'X':
        eye[0] -= step
    elif key == b'y':
        eye[1] += step
    elif key == b'Y':
        eye[1] -= step
    elif key == b'z':
        eye[2] += step
    elif key == b'Z':
        eye[2] -= step
    elif key == b'c':
        center[0] += step
    elif key == b'C':
        center[0] -= step
    elif key == b'v':
        center[1] += step
    elif key == b'V':
        center[1] -= step
    elif key == b'b':
        center[2] += step
    elif key == b'B':
        center[2] -= step
    elif key == b'u':
        up[0] += step
    elif key == b'U':
        up[0] -= step
    elif key == b'i':
        up[1] += step
    elif key == b'I':
        up[1] -= step
    elif key == b'o':
        up[2] += step
    elif key == b'O':
        up[2] -= step
    elif key == b'g':
        for i in range(45):
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            gluLookAt(*eye, *center, *up)
            drawRectanglePoints(1, 1, 1)
            drawOctagon(0.5, 1)
            glutSwapBuffers()
            time.sleep(0.01)
            eye[0] = math.cos(math.radians(i))
            eye[1] = math.sin(math.radians(i))
            center[0] = 0
            center[1] = 0
            center[2] = 0
            up[0] = 1.0
            up[1] = 40.0
            up[2] = 0.0
            glutPostRedisplay()

    glutPostRedisplay()
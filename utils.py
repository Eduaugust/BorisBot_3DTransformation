from OpenGL.GL import *
from OpenGL.GLUT import *
import math

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
            glTranslatef(x, y, z)
            glColor3f(*color)
            glutSolidCube(cube_size)
            glPopMatrix()

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
        glTranslatef(x_center, y_center, height / 2)
        glRotatef(angle * 180 / math.pi, 0, 0, 1)  # Rotate the rectangle
        drawRectangle(radius, half_side_length, height, color)  # Adjusted value
        glPopMatrix()


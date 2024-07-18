from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

def draw_base():
    num_sides = 8
    radius = 1.5
    height = 0.5

    def draw_face(z):
        glBegin(GL_POLYGON)
        for i in range(num_sides):
            angle = 2 * math.pi * i / num_sides
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex3f(x, y, z)
        glEnd()

    def draw_sides():
        glBegin(GL_QUAD_STRIP)
        for i in range(num_sides + 1):
            angle = 2 * math.pi * i / num_sides
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            glVertex3f(x, y, height)
            glVertex3f(x, y, -height)
        glEnd()

    glPushMatrix()
    glTranslatef(0, -2, -5)
    glScalef(3, 1, 3)
    
    # Desenhar a face superior
    draw_face(height)

    # Desenhar a face inferior
    draw_face(-height)

    # Desenhar as laterais
    draw_sides()
    
    glPopMatrix()

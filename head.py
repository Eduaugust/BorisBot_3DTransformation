from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import reimplementation
from utils import calculate_normal


def draw_head():
    # Carregar os dados do arquivo TXT
    vertices = np.loadtxt('output.txt')
    color = (0.5, 0.5, 0.5)

    glMaterialfv(GL_FRONT, GL_AMBIENT, [c * 0.1 for c in color] + [1.0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, list(color) + [1.0])
    glMaterialfv(GL_FRONT, GL_SPECULAR, [c * 0.5 for c in color] + [1.0])
    glMaterialfv(GL_FRONT, GL_SHININESS, [30.0])

    # Desenhar os vértices
    glPushMatrix()
    reimplementation.glTranslatef(0, 0, -5) 
    scale = 0.2
    reimplementation.glScalef(scale, scale, scale)
    glBegin(GL_TRIANGLES)
    for index, vertex in enumerate(vertices):
        if index % 2 == 0:
            continue
        glVertex3f(vertex[0], vertex[1], vertex[2])
    glEnd()
    glPopMatrix()


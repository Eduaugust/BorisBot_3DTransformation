from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_arm():
    glPushMatrix()
    glTranslatef(-1.5, 1, -5)
    glScalef(0.5, 2, 0.5)
    glutSolidCube(1)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(1.5, 1, -5)
    glScalef(0.5, 2, 0.5)
    glutSolidCube(1)
    glPopMatrix()

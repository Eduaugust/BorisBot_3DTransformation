from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_body():
    glPushMatrix()
    glTranslatef(0, 0, -5)
    glScalef(2, 3, 1)
    glutSolidCube(1)
    glPopMatrix()
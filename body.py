from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import reimplementation

def draw_body():
    glPushMatrix()
    #reimplementation.glTranslatef(0, 0, -5)
    reimplementation.glScalef(1, 2, 1)
    glutSolidCube(1)
    glPopMatrix()

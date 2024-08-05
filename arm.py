from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import utils

def draw_arm():

    # DRAW ARM STRUCTURE

    # ARM BASE
    glPushMatrix()
    glTranslatef(0.5, 0, -5)
    glScalef(0.1, 0.01, -5)
    glutSolidCube(1)
    glPopMatrix()

    # ARM BASE JOINT
    glPushMatrix()
    glTranslatef(0.8, 0.55, -5.2)
    glRotatef(90, 1, 0, 0)
    utils.drawOctagon(0.5, 0.5, color=(0, 1, 0))
    glPopMatrix()

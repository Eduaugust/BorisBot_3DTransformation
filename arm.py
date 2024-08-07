from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import reimplementation
import utils

def draw_arm():

    # DRAW ARM STRUCTURE

    # ARM BASE
    glPushMatrix()
    reimplementation.glTranslatef(0.5, 0, -5)
    reimplementation.glScalef(0.1, 0.01, -5)
    glutSolidCube(1)
    glPopMatrix()

    # ARM BASE JOINT
    glPushMatrix()
    reimplementation.glTranslatef(0.8, 0.55, -5.2)
    reimplementation.glRotatef(90, 1, 0, 0)
    utils.drawOctagon(0.5, 0.5, color=(0, 1, 0))
    glPopMatrix()

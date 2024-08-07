from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import reimplementation
import utils

def draw_base():
    # DRAW WHEEL 1
    
    glPushMatrix()
    reimplementation.glTranslatef(0, -1.5, -6)
    reimplementation.glScalef(0.2, 0.2, 0.2)
    glutSolidTorus(0.5, 1, 30, 30)
    glPopMatrix()

    # DRAW WHEEL 2
    glPushMatrix()
    reimplementation.glTranslatef(0, -1.5, -4)
    reimplementation.glScalef(0.2, 0.2, -0.2)
    glutSolidTorus(0.5, 1, 30, 30)
    glPopMatrix()

    # BASE
    glPushMatrix()
    reimplementation.glTranslatef(0, 0, -5)  # Move the octagon 0.5 units back in the z-axis
    reimplementation.glRotatef(90, 1, 0, 0)
    utils.drawOctagon(2, 1, color=(0, 1, 2))
    glPopMatrix()
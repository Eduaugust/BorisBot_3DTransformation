from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import reimplementation
import utils

def draw_base():
    # DRAW WHEEL 1
    
    glPushMatrix()
    reimplementation.glTranslatef(0, -1.5, -1)
    reimplementation.glScalef(0.2, 0.2, 0.2)
    material_diffuse = [1, 0.1, 0.0, 1.0]  # Cor difusa do material (laranja)
    material_specular = [.0, .5, .5, 1.0]  # Cor especular do material
    material_shininess = [10.0]  # Coeficiente de brilho especular
    
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)
    glutSolidTorus(0.5, 1, 30, 30)
    glPopMatrix()

    # DRAW WHEEL 2
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)
    glPushMatrix()
    reimplementation.glTranslatef(0, -1.5, 1)
    reimplementation.glScalef(0.2, 0.2, -0.2)
    glutSolidTorus(0.5, 1, 30, 30)
    glPopMatrix()

    # BASE
    glPushMatrix()
    reimplementation.glTranslatef(0, 0, 0)  # Move the octagon 0.5 units back in the z-axis
    reimplementation.glRotatef(90, 1, 0, 0)
    utils.drawOctagon(2, 1, color=(0, 0, 1))
    glPopMatrix()
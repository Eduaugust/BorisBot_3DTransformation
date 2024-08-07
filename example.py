from OpenGL.GL import * # type: ignore
from OpenGL.GLUT import * # type: ignore
from OpenGL.GLU import *

import reimplementation # type: ignore

def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    
    glEnable(GL_LIGHTING)  # Habilita a iluminação
    glEnable(GL_LIGHT0)    # Habilita a luz 0
    
    light_position = [0, 1, 1, 0]  # Define a posição da luz
    light_ambient = [0.2, 0.2, 0.2, 1.0]  # Cor ambiente da luz
    light_diffuse = [1.0, 1.0, 1.0, 1.0]  # Cor difusa da luz (branco)
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Cor especular da luz (branco)
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    
    # Define as propriedades do material
    material_ambient = [0.7, 0.7, 0.7, 1.0]  # Cor ambiente do material
    material_diffuse = [0.8, 0.8, 0.8, 1.0]  # Cor difusa do material
    material_specular = [1.0, 1.0, 1.0, 1.0]  # Cor especular do material
    material_shininess = [50.0]  # Coeficiente de brilho especular
    
    glMaterialfv(GL_FRONT, GL_AMBIENT, material_ambient)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material_diffuse)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material_specular)
    glMaterialfv(GL_FRONT, GL_SHININESS, material_shininess)
    
    glColor3f(0, 0, 0)
    glLoadIdentity()
    glPushMatrix()
    reimplementation.glTranslatef(0, 0, -3)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    reimplementation.glTranslatef(2, 0, -3)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    reimplementation.glTranslatef(-2, 0, -3)
    glutWireCube(1)
    glPopMatrix()
    glPushMatrix()
    reimplementation.glTranslatef(0, 0, -6)
    glNormal3f(0, 0, 1)
    glutWireSphere(1, 1000, 1000)
    glPopMatrix()
    glFlush()


def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # reimplementation.glFrustum( -1.0, 1.0, -1.0, 1.0, 1.5, 20.0 )
    reimplementation.glOrtho(-3, 3, -3, 3, 1.5, 20)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE or GLUT_RGB)
    glutInitWindowSize(400, 400)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"3D Cube")
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == '__main__':
    main()
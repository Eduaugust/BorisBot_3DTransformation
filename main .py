from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Importar as partes do robô
from base import draw_base
from body import draw_body
from arm import draw_arm
import reimplementation
import utils

def display():
    glClearColor(1, 1, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    
    glEnable(GL_LIGHTING)  # Habilita a iluminação
    glEnable(GL_LIGHT0)    # Habilita a luz 0
    
    light_position = [0, 0, -1, 0]  # Define a posição da luz na direção do observador
    light_ambient = [0.2, 0.2, 0.2, 1.0]  # Cor ambiente da luz
    light_diffuse = [1.0, 1.0, 1.0, 1.0]  # Cor difusa da luz (branco)
    light_specular = [1.0, 1.0, 1.0, 1.0]  # Cor especular da luz (branco)
    
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    glLoadIdentity()
    gluLookAt(*utils.eye, *utils.center, *utils.up)
    
    glPushMatrix()
    reimplementation.glRotatef(utils.get_rotation(), 0, 1, 0)
    draw_base()
    draw_body()
    draw_arm()  
    glPopMatrix()

    glutPostRedisplay()
    glutSwapBuffers()

def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    reimplementation.glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 50.0)
    # reimplementation.glOrtho(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glEnable(GL_DEPTH_TEST)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Robo 3D")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(utils.keyboard)

    glutMainLoop()

if __name__ == '__main__':
    main()

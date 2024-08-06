from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Importar as partes do robô
from base import draw_base
from body import draw_body
from arm import draw_arm
import utils

# Variáveis globais para a posição e orientação da câmera
camera_pos = [0.0, 0.0, 5.0]  # Posição inicial da câmera
camera_front = [0.0, 0.0, -1.0]  # Direção na qual a câmera está olhando
camera_up = [0.0, 1.0, 0.0]  # Vetor "up" da câmera

# Velocidade de movimento e sensibilidade do mouse
camera_speed = 0.1
mouse_sensitivity = 0.1

# Ângulos de rotação da câmera
yaw = -90.0  # Inicialmente voltado para -z
pitch = 0.0

# Variáveis para armazenar a posição anterior do mouse
last_x, last_y = 350, 350  # Centro da janela

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

    # Definir a câmera usando gluLookAt
    glLoadIdentity()
    target = [camera_pos[0] + camera_front[0], camera_pos[1] + camera_front[1], camera_pos[2] + camera_front[2]]
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], target[0], target[1], target[2], camera_up[0], camera_up[1], camera_up[2])

    # Desenhar as partes do robô
    draw_base()
    draw_body()
    draw_arm()
    
    glFlush()

def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glFrustum(-1.0, 1.0, -1.0, 1.0, 1.5, 20.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global camera_pos, camera_front, camera_up, camera_speed
    
    if key == b'w':  # Move para frente
        camera_pos[0] += camera_front[0] * camera_speed
        camera_pos[1] += camera_front[1] * camera_speed
        camera_pos[2] += camera_front[2] * camera_speed
    elif key == b's':  # Move para trás
        camera_pos[0] -= camera_front[0] * camera_speed
        camera_pos[1] -= camera_front[1] * camera_speed
        camera_pos[2] -= camera_front[2] * camera_speed
    elif key == b'a':  # Move para a esquerda
        right = [camera_front[2], 0, -camera_front[0]]
        camera_pos[0] += right[0] * camera_speed
        camera_pos[2] += right[2] * camera_speed
    elif key == b'd':  # Move para a direita
        right = [camera_front[2], 0, -camera_front[0]]
        camera_pos[0] -= right[0] * camera_speed
        camera_pos[2] -= right[2] * camera_speed
    glutPostRedisplay()

def mouse_motion(x, y):
    global last_x, last_y, yaw, pitch, camera_front, mouse_sensitivity

    # Calcula a diferença de movimento do mouse
    x_offset = x - last_x
    y_offset = last_y - y  # Invertido porque as coordenadas Y aumentam de cima para baixo

    # Atualiza a última posição do mouse
    last_x = x
    last_y = y

    # Aplica a sensibilidade do mouse
    x_offset *= mouse_sensitivity
    y_offset *= mouse_sensitivity

    # Atualiza os ângulos de rotação
    yaw += x_offset
    pitch += y_offset

    # Limita o ângulo de pitch para evitar inversão
    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    # Calcula a nova direção da câmera
    front = [
        math.cos(math.radians(yaw)) * math.cos(math.radians(pitch)),
        math.sin(math.radians(pitch)),
        math.sin(math.radians(yaw)) * math.cos(math.radians(pitch))
    ]
    camera_front = [front[0], front[1], front[2]]
    camera_front = [x / math.sqrt(sum(i**2 for i in camera_front)) for x in camera_front]  # Normaliza o vetor

    glutPostRedisplay()

def main():
    if not hasattr(glutInit, '__call__'):
        raise RuntimeError('glutInit not available. Ensure that freeglut is properly installed.')

    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(10, 10)
    glutCreateWindow(b"Robo 3D")
    glEnable(GL_DEPTH_TEST)
    
    # Registrar as funções de callback
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)  # Usado para rastrear o movimento do mouse
    glutMainLoop()

if __name__ == '__main__':
    main()

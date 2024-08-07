from OpenGL.GL import glMultMatrixf, glGetFloatv, glLoadMatrixf, GL_MODELVIEW_MATRIX
import numpy as np

def glTranslatef(x, y, z):
    # Criar a matriz de translação
    translation_matrix = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [x,   y,   z,   1.0]
    ], dtype=np.float32)
    
    glMultMatrixf(translation_matrix)

def glScalef(sx, sy, sz):
    # Criar a matriz de escala
    scale_matrix = np.array([
        [sx,  0.0, 0.0, 0.0],
        [0.0, sy,  0.0, 0.0],
        [0.0, 0.0, sz,  0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.float32).T
    
    # Multiplicar a matriz de modelagem atual pela matriz de escala
    glMultMatrixf(scale_matrix)

def glRotatef(angle, x, y, z):
    # Converter o ângulo de graus para radianos
    radians = np.radians(angle)
    
    # Normalizar o vetor (x, y, z)
    norm = np.sqrt(x**2 + y**2 + z**2)
    if norm == 0:
        return
    x /= norm
    y /= norm
    z /= norm
    
    # Calcular os componentes da matriz de rotação
    c = np.cos(radians)
    s = np.sin(radians)
    t = 1 - c
    
    rotation_matrix = np.array([
        [t*x*x + c,   t*x*y - s*z, t*x*z + s*y, 0.0],
        [t*x*y + s*z, t*y*y + c,   t*y*z - s*x, 0.0],
        [t*x*z - s*y, t*y*z + s*x, t*z*z + c,   0.0],
        [0.0,         0.0,         0.0,         1.0]
    ], dtype=np.float32).T
    
    # Multiplicar a matriz de modelagem atual pela matriz de rotação
    glMultMatrixf(rotation_matrix)
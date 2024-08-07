from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def bresenham_line(x0, y0, x1, y1):
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    
    while True:
        points.append((x0, y0))
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    
    return points

def draw_bresenham_line(x0, y0, x1, y1):
    points = bresenham_line(x0, y0, x1, y1)
    glBegin(GL_POINTS)
    glColor3f(1, 0, 0)  # Red color for Bresenham
    for point in points:
        glVertex2i(point[0], point[1])
    glEnd()

def dda_line(x0, y0, x1, y1):
    points = []
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    x_increment = dx / float(steps)
    y_increment = dy / float(steps)
    x = x0
    y = y0
    for _ in range(int(steps) + 1):
        points.append((round(x), round(y)))
        x += x_increment
        y += y_increment
    return points

def draw_dda_line(x0, y0, x1, y1):
    points = dda_line(x0, y0, x1, y1)
    glBegin(GL_POINTS)
    glColor3f(0, 0, 1)  # Blue color for DDA
    for point in points:
        glVertex2i(point[0], point[1])
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    
    # Draw Bresenham Lines
    draw_bresenham_line(-50, -50, 50, 50) 
    draw_bresenham_line(-50, 50, 50, 0)  

    # Draw DDA Lines
    draw_dda_line(-50, 50, 50, -50)       
    draw_dda_line(-50, 50, 50, 0)        
    
    glFlush()

def reshape(w: int, h: int):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-100, 100, -100, 100)  # Define the orthographic projection
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit()
    glEnable(GL_POINT_SMOOTH)  # Smooth points
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Line Algorithms Comparison")
    
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)

    glutMainLoop()

if __name__ == '__main__':
    main()

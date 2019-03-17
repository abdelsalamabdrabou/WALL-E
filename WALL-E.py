from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import numpy as np

scale = 14.5

def drawShape(r,g,b,alistX,alistY,shape):
    glColor3f(r,g,b)
    glBegin(shape)
    n = len(alistX)

    for index in range(0,n,1):
        glVertex(alistX[index]/scale,alistY[index]/scale)

    glEnd()

def drawCircle(r,g,b,rad=0, xc=0, yc=0):
    glBegin(GL_POLYGON)
    rad = rad / scale
    xc = xc / scale
    yc = yc / scale

    for theta in np.arange(0, 2 * pi, .001):
        x = (xc + rad * sin(theta))
        y = (yc + rad * cos(theta))
        glColor3f(r,g,b)
        glVertex(x, y)

    glEnd()

def robot():

    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)

    # Axis
    #x = [-scale,scale,0,0]
    #y = [0,0,scale,-scale]
    #drawShape(0,0,1,x,y,GL_LINES)
#################################################
    # Right Leg
    # Main
    x = [1.7, 3.3, 3.3, 3, 3, 2.2, 1.7]
    y = [-1.9, -1.9, -4.5, -4.5, -4.7, -4.7, -4.3]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [3.3, 3.1, 3.1, 3.3]
    y = [-3.5, -3.7, -3.9, -3.9]
    drawShape(0.953, 0.933, 0.906, x, y, GL_POLYGON)

    x = [3.3, 1.9, 1.9, 3, 3.3]
    y = [-2.1, -2.1, -3.6, -3.6, -3.3]
    drawShape(0.678, 0.737, 0.753, x, y, GL_POLYGON)

    x = [3, 1.9, 1.9, 2.3, 3]
    y = [-3.8, -3.8, -4.2, -4.6, -4.6]
    drawShape(0.678, 0.737, 0.753, x, y, GL_POLYGON)

    # small circle
    drawCircle(0.15, 0.27, 0.45, 0.1, 2.2, -4.2)

    # legs
    x = [5.7, 3.3, 3.3, 5.7]
    y = [-1.3, -1.3, -5.4, -5.4]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [5.5, 3.5, 3.5, 5.5]
    y = [-1.5, -1.5, -5.2, -5.2]
    drawShape(0.498, 0.506, 0.517, x, y, GL_POLYGON)

    x = [5.5, 3.5]
    y = [-1.8, -1.8]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-2.33, -2.33]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-2.86, -2.86]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-3.39, -3.39]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-3.92, -3.92]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-4.48, -4.48]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-4.984, -4.984]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [5.5, 3.5]
    y = [-5, -5]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [3.3, 3.1, 3.1, 3.3]
    y = [-4.1, -4.1, -4.3, -4.3]
    drawShape(0.502, 0.756, 0.557, x, y, GL_POLYGON)

    # Left Leg
    # Main
    x = [-3.3,-1.7, -1.7, -2.2, -3, -3,-3.3]
    y = [-1.9,-1.9, -4.3, -4.7, -4.7, -4.5,-4.5]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-3.3, -3.1, -3.1, -3.3]
    y = [-3.5, -3.7,-3.9, -3.9]
    drawShape(0.953, 0.933, 0.906, x, y, GL_POLYGON)

    x = [-3.3, -1.9, -1.9, -3, -3.3]
    y = [-2.1, -2.1, -3.6, -3.6, -3.3]
    drawShape(0.678, 0.737, 0.753, x, y, GL_POLYGON)

    x = [-3, -1.9, -1.9, -2.3, -3]
    y = [-3.8, -3.8, -4.2, -4.6, -4.6]
    drawShape(0.678, 0.737, 0.753, x, y, GL_POLYGON)

    #small circle
    drawCircle(0.15,0.27,0.45,0.1,-2.2,-4.2)

    #legs
    x = [-5.7, -3.3, -3.3, -5.7]
    y = [-1.3, -1.3, -5.4, -5.4]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-5.5, -3.5, -3.5, -5.5]
    y = [-1.5, -1.5, -5.2, -5.2]
    drawShape(0.498, 0.506, 0.517, x, y, GL_POLYGON)

    x = [-5.5, -3.5]
    y = [-1.8, -1.8]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-2.33, -2.33]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-2.86, -2.86]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-3.39, -3.39]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-3.92, -3.92]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-4.48, -4.48]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-4.984, -4.984]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-5.5, -3.5]
    y = [-5, -5]
    drawShape(0.15, 0.27, 0.45, x, y, GL_LINES)

    x = [-3.3, -3.1, -3.1, -3.3]
    y = [-4.1, -4.1, -4.3, -4.3]
    drawShape(0.502, 0.756, 0.557, x, y, GL_POLYGON)




    #################################################
    # Main Box
    x = [-3.2, 3.2, 3.2, -3.2]
    y = [2.2, 2.2, -3.3, -3.3]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    # Arm
    x = [3.2, 3.7, 3.7, 3]
    y = [2.2, 1.7, 0, 0]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-3.2, -3.7, -3.7, -3]
    y = [2.2, 1.7, 0, 0]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)
#################################################\
    # Inside yellow Squares #
    x = [-3, -1.7, -1.7, -3]
    y = [2, 2, 1.7, 1.7]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    x = [3, 1.7, 1.7, 3]
    y = [2, 2, 1.7, 1.7]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    # down
    x = [-3, -1.7, -1.7, -3]
    y = [1.5, 1.5, 0.6, 0.6]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    x = [3, 1.7, 1.7, 3]
    y = [1.5, 1.5, 0.6, 0.6]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    # left and right
    x = [3.2, 3.6, 3.6, 3.2]
    y = [1.8, 1.6, 0, 0]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    x = [-3.2, -3.6, -3.6, -3.2]
    y = [1.8, 1.6, 0, 0]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)
#################################################
    # center head box
    x = [-1.5, 1.5, 1.5, -1.5]
    y = [2, 2, 0.5, 0.5]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    # half box
    x = [-3, 3, 3, -3]
    y = [0.4, 0.4, -3.1, -3.1]
    drawShape(1, 0.8, 0.3, x, y, GL_POLYGON)

    x = [-2.5, -0.05, -0.05, -2.5]
    y = [0.4, 0.4, -2.2, -2.2]
    drawShape(1, 0.9, 0.556, x, y, GL_POLYGON)

    # Blue squares
    x = [-1.15, 0.1, 0.1, -1.15]
    y = [1.72, 1.72, 1, 1]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-1, -0.1, -0.1, -1]
    y = [1.6, 1.6, 1.1, 1.1]
    drawShape(0.55, 0.82, 0.87, x, y, GL_POLYGON)

    # Circles
    drawCircle(0.15, 0.27, 0.45, 0.3, 0.8, 1.35)
    drawCircle(1,0.42,0.29,0.1,0.8,1.35)
#################################################
    # Nick
    x = [-0.9, 0.9, 0.9, -0.9]
    y = [3.6, 3.6, 2.2, 2.2]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-0.7, 0.7, 0.7, -0.7]
    y = [2.5, 2.5, 2.2, 2.2]
    drawShape(0.96, 0.84, 0.48, x, y, GL_POLYGON)

    x = [-0.7, 0.7, 0.7, -0.7]
    y = [3.1, 3.1, 2.6, 2.6]
    drawShape(0.96, 0.84, 0.48, x, y, GL_POLYGON)

    x = [-0.7, 0.7, 0.7, -0.7]
    y = [3.4, 3.4, 3.2, 3.2]
    drawShape(0.96, 0.84, 0.48, x, y, GL_POLYGON)

    # Second
    x = [-0.6, 0.6, 0.6, -0.6]
    y = [4.5, 4.5, 3.6, 3.6]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [-0.4, 0.4, 0.4, -0.4]
    y = [4.3, 4.3, 3.6, 3.6]
    drawShape(0.96, 0.84, 0.48, x, y, GL_POLYGON)

    drawCircle(0.15, 0.27, 0.45, 0.35, 0.9, 4.5)
    drawCircle(0.957, 0.961, 0.980, 0.2, 0.87, 4.5)

    drawCircle(0.15, 0.27, 0.45, 0.35, -0.9, 4.5)
    drawCircle(0.957, 0.961, 0.980, 0.2, -0.87, 4.5)

    # Main Nick
    x = [-2.4, 2.4, 0.6, -0.6]
    y = [6.4, 6.4, 4.5, 4.5]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    # center
    x = [-1, 1, 0.5, -0.5]
    y = [5.1, 5.1, 4.5, 4.5]
    drawShape(0.749,0.655,0.376, x, y, GL_POLYGON)

    # circle in middle nick
    drawCircle(0.15,0.27,0.45,0.65,0,5.4)

    x = [-0.4, 0.4, 0.5, -0.5]
    y = [5.6, 5.6, 5.3, 5.3]
    drawShape(0.749, 0.655, 0.376, x, y, GL_POLYGON)

    x = [-0.2, 0.2, 0.4, -0.4]
    y = [6.2, 6.2, 5.7, 5.7]
    drawShape(0.749, 0.655, 0.376, x, y, GL_POLYGON)

    # Main blue circles
    drawCircle(0.15,0.27,0.45,1.35,2,5.2)
    drawCircle(0.831, 0.917, 0.945, 1.1, 2, 5.2)

    drawCircle(0.15, 0.27, 0.45, 1.35, -2, 5.2)
    drawCircle(0.831, 0.917, 0.945, 1.1, -2, 5.2)

    # blue2 circles
    #right
    drawCircle(0.15,0.27,0.45,1,1.5,5.6)
    drawCircle(0.254, 0.364, 0.505, 0.8, 1.5, 5.6)
    drawCircle(0.192, 0.306, 0.471, 0.5, 1.5, 5.6)
    drawCircle(0.243, 0.357, 0.502, 0.25, 1.5, 5.6)
    drawCircle(0.757, 0.788, 0.839, 0.125, 1.3, 5.5)
    drawCircle(0.757, 0.788, 0.839, 0.25, 1.75, 5.9)
    #left
    drawCircle(0.15, 0.27, 0.45, 1, -1.5, 5.6)
    drawCircle(0.254, 0.364, 0.505, 0.8, -1.5, 5.6)
    drawCircle(0.192, 0.306, 0.471, 0.5, -1.5, 5.6)
    drawCircle(0.243, 0.357, 0.502, 0.25, -1.5, 5.6)
    drawCircle(0.757, 0.788, 0.839, 0.125, -1.3, 5.5)
    drawCircle(0.757, 0.788, 0.839, 0.25, -1.75, 5.9)


    #################################################

    # Main Arms

    x = [-4,-3.7,-2.2,-1.3,-1.3,-1.6,-1.6,-1.3,-1.3,-2.2,-3.7,-4]
    y = [0.6,1,1,0.8,0.2,0.2,-0.2,-0.2,-0.8,-1,-1,-0.6]
    drawShape(0.15,0.27,0.45,x,y,GL_POLYGON)

    x = [4, 3.7, 2.2, 1.3, 1.3, 1.6, 1.6, 1.3, 1.3, 2.2, 3.7, 4]
    y = [0.6, 1, 1, 0.8, 0.2, 0.2, -0.2, -0.2, -0.8, -1, -1, -0.6]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    # 4 inside arms

    x = [-2.5, -2.1, -1.5, -1.5,-2.5]
    y = [0.9,0.9,0.7,0.3,0.3]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [-3.6, -2.7, -2.7, -3.7, -3.7]
    y = [0.9, 0.9, 0.3, 0.3, 0.7]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [-2.5, -2.1, -1.5, -1.5, -2.5]
    y = [-0.9, -0.9, -0.7, -0.3, -0.3]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [-3.6, -2.7, -2.7, -3.7, -3.7]
    y = [-0.9, -0.9, -0.3, -0.3, -0.7]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [-3.3, -1.8, -1.8, -3.3]
    y = [0.1, 0.1, -0.1, -0.1]
    drawShape(0.541, 0.627, 0.647, x, y, GL_POLYGON)

    x = [-4, -3.3, -3.3, -4]
    y = [0.6, 0.6, -0.6, -0.6]
    drawShape(0.15,0.27,0.45, x, y, GL_POLYGON)

    x = [-3.8, -3.4, -3.4, -3.8]
    y = [0.5, 0.5, -0.5, -0.5]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    # 4 inside arms right

    x = [2.5, 2.1, 1.5, 1.5, 2.5]
    y = [0.9, 0.9, 0.7, 0.3, 0.3]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [3.6, 2.7, 2.7, 3.7, 3.7]
    y = [0.9, 0.9, 0.3, 0.3, 0.7]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [2.5, 2.1, 1.5, 1.5, 2.5]
    y = [-0.9, -0.9, -0.7, -0.3, -0.3]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [3.6, 2.7, 2.7, 3.7, 3.7]
    y = [-0.9, -0.9, -0.3, -0.3, -0.7]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    x = [3.3, 1.8, 1.8, 3.3]
    y = [0.1, 0.1, -0.1, -0.1]
    drawShape(0.541, 0.627, 0.647, x, y, GL_POLYGON)

    x = [4, 3.3, 3.3, 4]
    y = [0.6, 0.6, -0.6, -0.6]
    drawShape(0.15, 0.27, 0.45, x, y, GL_POLYGON)

    x = [3.8, 3.4, 3.4, 3.8]
    y = [0.5, 0.5, -0.5, -0.5]
    drawShape(0.776, 0.898, 0.925, x, y, GL_POLYGON)

    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(800, 600)
glutCreateWindow(b"WALL-E")
glutDisplayFunc(robot)
glutMainLoop()
import pygame
from pygame.locals import *


matrix = [
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
    [ 0, 0, 0, 0],
]

pygame.init()
def load_image(filename, transparent=False):
    try: image = pygame.image.load(filename)
    except:
        raise SystemExit('No se pudo cargar la imagen')
    #image = image.convert()
    if transparent:
        color = image.get_at((0,0)) 
        image.set_colorkey(color, RLEACCEL) 
    return image


def check_matrix(row, column):
    return matrix[row][column] == 0
    
def matrix_fill_space(row, column):
    if check_matrix(row, column):
        matrix[row][column] = 1
    

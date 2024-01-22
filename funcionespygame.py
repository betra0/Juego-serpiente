import pygame
from clases import cuerpo
from variables import(allobjetos, moradito, tamañocola, segmentos)



def colordinamico(color, ared, ablue):
        rojo = color[0]
        azul = color[2]
        verde = color[1]
        if not ared:
            rojo -= 2
        if ared:
            rojo += 2
        if not ablue:
            azul += 2
        if ablue:
            azul -= 2

        if rojo <50:
            rojo = 50
            ared = True 
        if rojo >220:
            rojo = 220
            ared = False
        if azul <50:
            azul = 50
            ablue = False
        if azul >220:
            azul = 220
            ablue = True
        color = (rojo, verde, azul)
        return color, ared, ablue

def calculardistancia(x, y, x1, y1):

        distanciacuadrado = (x - x1)**2+(y - y1)**2
        distancia = distanciacuadrado**0.5
        
        return distancia

def distancia():

        pass

def debug(texto):
     
     print("\n Debug", texto)



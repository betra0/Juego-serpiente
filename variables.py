import pygame


# Dimensiones de la pantalla
#ancho
width = 600
#alto
height = 600
# Velocidad de fotogramas por segundo
velocidad = 25
aumentovelocidad = 0.2
verderamdom = 3
# Tamaño de la cabeza de la serpiente
tamañocabeza = 20
divisioncabeza = 2
tamañocola =3
# Colores
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
moradito = (130, 0, 130)


score = 0
copyscore = 0

# Bucle principal del juego
running = True
exit = False
#se utiliza para medir el tiempo de los ciclos del bucle
inicio = False
posiciones = []
manzanaverdecontador = 0 

segmentos = pygame.sprite.Group()
allobjetos = pygame.sprite.Group()


import pygame
import random
import funcionespygame as py
from variables import (width, height, velocidad, aumentovelocidad, verderamdom, 
    tamañocabeza, divisioncabeza, tamañocola, black, white, blue, red, moradito, score,
    copyscore, running, exit, inicio, posiciones, manzanaverdecontador, segmentos,)
from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT,
        K_w,
        K_s,
        K_d,
        K_a,
)

class Cabeza(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("cara.png")
            self.image = pygame.transform.scale(self.image, (tamañocabeza, tamañocabeza))
            
            self.rect = self.image.get_rect()
            self.rect.center = ((width // 2), (height // 2))
            self.speed = tamañocabeza/divisioncabeza
            self.last_direction = "stop"  # Inicializar detenido
            self.running = True

        def update(self, posiciones, sinparedes):
            keys = pygame.key.get_pressed()
           
            if keys[K_UP]:
                if not self.last_direction == "down":
                    self.last_direction = "up"
            elif keys[K_DOWN]:
                if not self.last_direction == "up":
                    self.last_direction = "down"
            elif keys[K_LEFT]:
                if not self.last_direction == "right":
                    self.last_direction = "left"
            elif keys[K_RIGHT]:
                if not self.last_direction == "left":
                    self.last_direction = "right"

            elif keys[K_w]:
                if not self.last_direction == "down":
                    self.last_direction = "up"
            elif keys[K_s]:
                if not self.last_direction == "up":
                    self.last_direction = "down"
            elif keys[K_a]:
                if not self.last_direction == "right":
                    self.last_direction = "left"
            elif keys[K_d]:
                if not self.last_direction == "left":
                    self.last_direction = "right"

            # Obtener la última dirección en la que se movió
            direction = self.last_direction

            # Actualizar la posición en función de la dirección
            if direction == "up":
                self.rect.y -= self.speed
            elif direction == "down":
                self.rect.y += self.speed
            elif direction == "left":
                self.rect.x -= self.speed
            elif direction == "right":
                self.rect.x += self.speed
            
            if sinparedes:
                if self.rect.x >= width and direction =="right":
                    self.rect.x = 0 - tamañocabeza
                if self.rect.x <= 0 - tamañocabeza and direction =="left":
                    self.rect.x = width
                if self.rect.y <= 0 - tamañocabeza and direction =="up":
                    self.rect.y = height
                if self.rect.y >= height  and direction =="down":
                    self.rect.y = 0 - tamañocabeza
                    pass
            # Agregar las coordenadas de la cabeza a la lista de posiciones
            posiciones.insert(0, (self.rect.x, self.rect.y))

            # Mantener el tamaño de la lista igual a la longitud total de la serpiente
            if len(posiciones) > len(segmentos) + 1:
                posiciones.pop()


        def colisionpared(self, running):
            # colision con pared
            if self.rect.left < -5:
                running = False
                print("debug colisiond1")
            if self.rect.right > width+5:
                running = False
                print("debug colisiond1")
            if self.rect.top <= -5:
                running = False
                print("debug colisiond1")
            if self.rect.bottom >= height+5:
                running = False
                print("debug colisiond1")
            return running
        
class comida(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamañocabeza +10
            self.image = pygame.image.load("apple.png")
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño))
            
            self.rect = self.image.get_rect()
            y = (( height //2 ) -tamañocabeza*3)
            x = (width//2)
            self.rect.center = (x, y)

        def aleatoria(self):
            self.rect.y = random.randint(self.tamaño, height-self.tamaño)
            self.rect.x = random.randint(self.tamaño, width-self.tamaño)

class cuerpo(pygame.sprite.Sprite):
        def __init__(self, color):
            super().__init__()
            self.color = color
            self.tamaño = tamañocabeza 
            self.image = pygame.Surface((self.tamaño, self.tamaño))
            self.image.fill(color)
            self.rect = self.image.get_rect()
            self.rect.center = (-tamañocabeza, -tamañocabeza)
            self.ared = False
            self.ablue = False

        def moversegmento(self, xs, ys):

            self.rect.center = (xs, ys)
           

        def update(self,):

            self.color, self.ared, self.ablue = py.colordinamico(self.color, self.ared, self.ablue)

            self.image.fill(self.color)

class comidapodrida(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.tamaño = tamañocabeza +5
            self.image = pygame.image.load("manzanaverde.png")
            self.image = pygame.transform.scale(self.image, (self.tamaño, self.tamaño))

            self.rect = self.image.get_rect()

            self.rect.center = (-tamañocabeza, -tamañocabeza)
        
        def aleatoria(self, cabeza_jugador):
            while True:

                self.rect.y = random.randint(self.tamaño, height-self.tamaño)
                self.rect.x = random.randint(self.tamaño, width-self.tamaño)
                xcabesa, ycabesa = cabeza_jugador.rect.center
                distancia = py.calculardistancia(xcabesa, ycabesa, self.rect.x, self.rect.y)
                
                if distancia <= 50  :
                    pass
                else:
                    texto = "distancia manzana/Cabeza", distancia
                    py.debug(texto)
                    break

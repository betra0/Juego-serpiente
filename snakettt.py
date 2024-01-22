
import pygame
import random
import time
import os
import funcionespygame as py
from clases import (Cabeza, comida, cuerpo, comidapodrida)
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
from variables import*

def gameon(mananas_verdes=True, highscore=0, sinparedes=False):

    # Inicialización de pygame
    pygame.init()

 
    from variables import (width, height, velocidad, aumentovelocidad, verderamdom, 
    tamañocabeza, divisioncabeza, tamañocola, black, white, blue, red, moradito, score,
    copyscore, running, exit, inicio, posiciones, manzanaverdecontador, segmentos, )
    


    font = pygame.font.Font(None, 36)
    overfont = pygame.font.Font(None, 80)
 
   
    #funciones

    def agregarsegmento():
        for i in range(0, tamañocola):
            segmento = cuerpo(moradito)
            segmentos.add(segmento)
            allobjetos.add(segmento)

    def segircabeza():

        segmento1 = segmentos.sprites()[0]

        xcabeza, ycabeza = cabeza_jugador.rect.center
        segmento1.moversegmento(xcabeza, ycabeza)

    def segirsegmento():
        totalSeg = len(segmentos)
        for index in range(totalSeg -1, 0, -1):
             segmento = segmentos.sprites()[index - 1]
             x, y = segmento.rect.center
             segmento2 = segmentos.sprites()[index]
             segmento2.moversegmento(x, y)

    def spawnmanzanaverde(contador, verderamdom):
        if mananas_verdes == True:
            contador += 1
            if contador >= verderamdom:
                for manzanaverde in manzanasverdes:
                    manzanaverde.aleatoria(cabeza_jugador)
                contador = 0
                verderamdom =  random.randint(2,9)
        return contador, verderamdom

    def newmanzanaverde():
        if mananas_verdes == True:

            manzanaverde = comidapodrida()
            manzanaverde.aleatoria(cabeza_jugador)
            allobjetos.add(manzanaverde)
            manzanasverdes.add(manzanaverde)
            print("Debug: se a agregado un nuevo sprite verde")
            print("Debug: Cantidad de manzanas verdes: ", len(manzanasverdes))
    
    def todaslascolisiones(running):

        # colicion con Pared
        if sinparedes == False:
            running = cabeza_jugador.colisionpared(running)
        # COLISION SEGMENTOS 1
        if (cabeza_jugador.rect.x, cabeza_jugador.rect.y) in posiciones[1:]:
            running = False
            py.debug("debug colisionf1")
        # COLISION SEGMENTOS 2
        if any(pygame.sprite.collide_rect(cabeza_jugador, segmento) for segmento in segmentos.sprites()[5:]):
            running = False
            py.debug("debug colisionf2")

        # las manzanas verdes son un asco
        if pygame.sprite.spritecollideany(cabeza_jugador, manzanasverdes):
            running = False
            py.debug("debug colisionf3")

        return running
    
    # Configuración de la pantalla
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snake Game")

    # Cargar imagen de fondo
    ruta_imagen = os.path.abspath("fondo.gif")
    background = pygame.image.load(ruta_imagen)

    # Reloj para controlar la velocidad de fotogramas
    clock = pygame.time.Clock()

    # Crear la cabeza de la serpiente como un pygame.Rect
    # Crear grupo de sprites para el jugador
    allobjetos = pygame.sprite.Group()
    
    cabesasprite = pygame.sprite.Group()
    manzanasverdes = pygame.sprite.Group()
    comidarica = pygame.sprite.Group()
    segmentos = pygame.sprite.Group()
    cabeza_jugador = Cabeza()
    manzana = comida()
    manzanaverde = comidapodrida()
    allobjetos.add(cabeza_jugador)
    cabesasprite.add(cabeza_jugador)

    allobjetos.add(manzana)
    comidarica.add(manzana)
    allobjetos.add(manzanaverde)
    manzanasverdes.add(manzanaverde)


    
    gameovertxt = overfont.render("Game Over", True, red)


    posiciones = []

    #=== comiensa el bucle ===#
    print("")
    while running:
        
        #revisa las colisiones
        running = todaslascolisiones(running)

        if pygame.sprite.spritecollideany(manzana, manzanasverdes):
            py.debug("choque de manzanas1")
            for manzanaverde in manzanasverdes:
                manzanaverde.aleatoria(cabeza_jugador) 

        # calcular eventos 
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                exit = True
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    exit = True
        # Renderizar texto de score y highscore
        score_text = font.render("Score: {}".format(score), True, white)
        highscore_text = font.render("Highscore: {}".format(highscore), True, white)
        

        #mover cola 
        if len(segmentos) >0:
            segircabeza()

            if len(segmentos) >1:
                segirsegmento()


         # Actualizar sprites
        
        cabesasprite.update(posiciones, sinparedes)
        segmentos.update()

        # Dibujar el fondo
        screen.blit(background, (0, 0))

         # Dibujar sprites
        allobjetos.draw(screen)
        cabesasprite.draw(screen)
        comidarica.draw(screen)
        manzanasverdes.draw(screen)
        # dibuja el marcador
        screen.blit(score_text, (width//2-width//4, 10))
        screen.blit(highscore_text, (width//2, 10))

        # Comer manzanas es bueno xd
        if pygame.sprite.spritecollideany(cabeza_jugador, comidarica):
 
            manzana.aleatoria()
            if copyscore >= 190:
                newmanzanaverde()
                copyscore = 0
            manzanaverdecontador, verderamdom = spawnmanzanaverde(manzanaverdecontador, verderamdom)

            #llamar funcion agregar segmentos 
            agregarsegmento()
            score += 10
            copyscore += 10
            if retardo > 0.027:

                velocidad += aumentovelocidad
            else:
                velocidad += aumentovelocidad/2
            if score > highscore:
                highscore = score


        corx, cory = cabeza_jugador.rect.center
        #print(f"\rCordenadas: {corx}, {cory}", end="")

        # Actualizar la pantalla
        pygame.display.flip()
        
        if inicio:
            try:
                
                fin = time.time()
                retardo = fin - inicio  
                fps = 1 / retardo
                velocidad2 = (fps * (tamañocabeza / divisioncabeza))
                print(f"\rRetardo: {retardo:.3f} segundos, FPS: {fps:.0f}, velocidad: {velocidad2:.0f}, Cordenadas: {corx}, {cory}", end="")
            except ZeroDivisionError:
                pass
        inicio = time.time() 
        # Controlar la velocidad de fotogramas
        clock.tick(velocidad)
        #time.sleep(0.5)

    # Salir del juego
    if not exit:
        screen.blit(gameovertxt, (width // 2 -140, height // 2 -70))
        pygame.display.flip()
        print ("\n tu score fue: ", score)
        time.sleep(1)
    pygame.quit()
    return exit, score



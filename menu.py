import tkinter as tk
from rich import print
from scores import*
from snakettt import *





v1boton = None
nuevo_boton_opcion2 = None
atrasboton = None

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")

def normalgame():
    #ocultar ventana menu
    ventana.withdraw() 
    print("     <<<<<< [bold green] Snake Game [/bold green] >>>>>> ")
    print("   <<<<<< [bold blue] Iniciando Snake [/bold blue] >>>>>> ")
    #ejucutar pygame
    while True:
        nada, high_score = obtenerscore()
        run, score = gameon(highscore=high_score) 
        nada, high_score = obtenerscore()
        if score > high_score:
            high_score = score
            print("\nsu nuevo puntaje es:", high_score)
            guardar2scores(score, high_score)
        else:
            print("\nsu puntaje fue:", score)
        if run:
            break
    #volver a mostrar menu   
    ventana.deiconify()

def experimentalgame():
    #ocultar ventana menu
    ventana.withdraw() 
    print("     <<<<<< [bold green] Snake Game [/bold green] >>>>>> ")
    print("   <<<<<< [bold blue] Iniciando Snake [/bold blue] >>>>>> ")
    #ejucutar pygame
    while True:
        nada, high_score = xobtenerscore()
        run, score = gameon(highscore=high_score, sinparedes=True) 
        nada, high_score = xobtenerscore()
        if score > high_score:
            high_score = score
            print("\nsu nuevo puntaje es:", high_score)
            xguardar2scores(score, high_score)
        else:
            print("\nsu puntaje fue:", score)
        if run:
            break
    #volver a mostrar menu
    ventana.deiconify()
def eleccionjuego():

    global v1boton, nuevo_boton_opcion2, atrasboton
    # Ocultar botones
    botoniniciar.pack_forget()
    botonsalir.pack_forget()

    v1boton = tk.Button(ventana, text="Normal", command=normalgame, font=("consolas", 13), background="RoyalBlue4", bd=6)
    v1boton.pack(pady=80)

    nuevo_boton_opcion2 = tk.Button(ventana, text="experimental", font=("consolas", 13), background="RoyalBlue4", bd=6, command=experimentalgame)
    nuevo_boton_opcion2.pack(pady=5)

    atrasboton = tk.Button(ventana, text="Volver", command=volveratras, font=("consolas", 10), background="RoyalBlue4", bd=6)
    atrasboton.pack(pady=(150, 0))

def volveratras():
    global v1boton, nuevo_boton_opcion2, atrasboton
    # Ocultar los nuevos elementos
    v1boton.pack_forget()
    nuevo_boton_opcion2.pack_forget()
    atrasboton.pack_forget()
    
    # Mostrar los elementos originales nuevamente
    botoniniciar.pack(pady=(70,0))
    botonsalir.pack(pady=100)


def salir():
    cerrarventana()
    pass
def cerrarventana():
    ventana.quit()

#establecer ventana
ventana = tk.Tk()
ventana.title("Snake Game")
width = 600
height = 600

center_window(ventana, width, height)


#establece la imagen de fondo
imagenfondo = tk.PhotoImage(file="imagen.png")
fondolabel = tk.Label(ventana, image=imagenfondo)
fondolabel.place(x=0, y=0, relwidth=1, relheight=1)

#establece titulo label
titulolabel = tk.Label(ventana, text="Snake game", font=("consolas", 24, "bold"), background="RoyalBlue4", relief = tk.GROOVE, bd=10
)
titulolabel.pack(pady=(50,0))

botoniniciar = tk.Button(ventana, text="Jugar", command=eleccionjuego, font=("consolas", 15), background="RoyalBlue4", bd=6)
botoniniciar.pack(pady=(70,0))

botonsalir = tk.Button(ventana, text="Salir", command=salir, font=("consolas", 15), background="RoyalBlue4", bd=4)
botonsalir.pack(pady=100)

ventana.protocol("WM_DELETE_WINDOW", cerrarventana)



ventana.mainloop()
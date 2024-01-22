

def obtenerscore():
    with open("score.txt", "r") as archivo:
        contenido = archivo.readlines()
        try:
            score = int(contenido[0])
        except IndexError:
            score = 0
        try:
            high_score = int(contenido[1])
        except IndexError:
            high_score = 0
            
        return score, high_score

def guardar2scores(score, high_score):
    with open("score.txt", "w") as archivo:
        lineas = []
        lineas.append(str(score)  + "\n")
        lineas.append(str(high_score) + "\n")
        archivo.writelines(lineas)


def xobtenerscore():
    with open("scorex.txt", "r") as archivo:
        contenido = archivo.readlines()
        try:
            score = int(contenido[0])
        except IndexError:
            score = 0
        try:
            high_score = int(contenido[1])
        except IndexError:
            high_score = 0
            
        return score, high_score

def xguardar2scores(score, high_score):
    with open("scorex.txt", "w") as archivo:
        lineas = []
        lineas.append(str(score)  + "\n")
        lineas.append(str(high_score) + "\n")
        archivo.writelines(lineas)





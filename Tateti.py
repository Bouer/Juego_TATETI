
import random
import os




def Bienvenida (tablero): 
    print("")
    print("----------------------------------------------------------------")
    print("#","              BIENVENIDO AL JUEGO DEL TATETI                ","#",)
    print("#","                By Matias Cabrera - Ouer3D                  ","#")
    print("#","Contacto:                                                   ","#")
    print("#","      Github:   https://github.com/Bouer/Juego_TATETI       ","#")
    print("#","      Linkedin: https://www.linkedin.com/in/matiasouer3d/   ","#")
    print("----------------------------------------------------------------")
    print("")
    print("----------------------------------------------------------------")
    print("#","              QUE EL LIMITE SEA TU IMAGINACION!!            ","#")
    print("----------------------------------------------------------------")
    input("¡¡Presiona un 'Enter' para leer reglas del juego!!")
    borrarPantalla() #Limpia la pantalla
    print("REGLAS DEL JUEGO: ")
    print ("#"," El primer movimiento es de la maquina - siempre coloca una 'X' en el centro")
    print("#"," La maquina elegirá un cuadro de manera aleatoria")
    print("#"," El usuario ingresa su movimiento introduciendo el número de cuadro elegido")
    print("#"," Si el cuadro elegido ya fue jugado o el numero no es entre 1 y el 9, pedira otro numero")
    print("#"," El juego termina en empate, tu ganas, o la maquina gana")
    print("")
    imprimirTablero (tablero)
    input("¡¡Presiona un 'Enter' para arrancar el juego!!")
    borrarPantalla() #Limpia la pantalla

def borrarPantalla(): #Definimos la función estableciendo el nombre que queramos
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def imprimirTablero (tablero):  #Funcion que imprime el tablero!!
    
    for i in range(0,3):
        print ("+","+","+","+", sep="-------")
        print("|","|","|","|", sep="       ")
        for j in range(0,3):
            print("|  ",tablero[i][j],"  ", end="")
        print("|")
        print("|","|","|","|", sep="       ")
    print ("+","+","+","+", sep="-------")  
def jugadaMaquina (tablero):
    numAleatorio = random.randint(1, 9)
    print("")
    print("")
    print("Turno de la maquina:")
    
    while True:
        for i in range(len(tablero)):
            for j in range(len(tablero[i])):
                if tablero[i][j] == numAleatorio:
                    #print("El numero esta")
                    tablero[i][j] = 'X'
                    return True
        #Generamos otro numero porque el anterior ya esta ocupado!!        
        #print("Generando 2do numaleatorio")
        numAleatorio = random.randint(1, 9)
def jugadaUsuario(tablero):
    print("***")
    print("Es tu TURNO: ")
    print("***")
    jugada = int(input("Ingrese un numero del 1 al 9:")) #Pide que ingrese un numero!
    
    while True:
        if jugada < 10 and jugada > 0: #Valua si el numero esta dentro del rango permitido
            for i in range(3):
                for j in range(3): #Recorremos la matriz para verificar si el numero esta
                    if jugada == tablero[i][j] :
                        tablero[i][j] = 'O'
                        #print ("Esta")
                        return tablero
            else:
                print("***")
                print("Elija otra, la casilla ya esta ocupada")
                print("***")
                jugada = int(input("Ingrese un numero del 1 al 9:"))        
        else:
            print("***")
            print("Elija otra, el valor es incorrecto debe ser un numero el 1 al 9")
            print("***")
            jugada = int(input("Ingrese un numero del 1 al 9:"))
def verificacion(tablero):
    #Verificamos si alguno de los jugadores logro completar una linea, columna o diagonal
    # Verificar filas
    if tablero[0][0] == tablero[0][1] == tablero[0][2]:
        return tablero[0][0]
    elif tablero[1][0] == tablero[1][1] == tablero[1][2]:
        return tablero[1][0]
    elif tablero[2][0] == tablero[2][1] == tablero[2][2]:
        return tablero[2][0]

    # Verificar columnas
    elif tablero[0][0] == tablero[1][0] == tablero[2][0]:
        return tablero[0][0]
    elif tablero[0][1] == tablero[1][1] == tablero[2][1]:
        return tablero[0][1]
    elif tablero[0][2] == tablero[1][2] == tablero[2][2]:
        return tablero[0][2]

    # Verificar diagonales
    elif tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return tablero[0][0]
    elif tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[0][2]

    # Si nadie gano
    else:
        return False
def verificarGanador (tablero):
    
    global cantidadJugadas
    ganador = verificacion(tablero)
    

    if ganador is not False and cantidadJugadas < 9:
        if ganador == 'O':
            print("***")
            print("USTED HA GANADO!!!!!!!")
            print("FELICITACIONES!!! ... ")
            print("***")
            return True
        else:
            print("***")
            print("LA MAQUINA GANO!!")
            print("MEJOR SUERTE LA PROXIMA VEZ...!")
            print("***")
            return True
    elif cantidadJugadas >= 8:
        print("***")
        print("El juego termino en EMPATE!!")
        print("MEJOR SUERTE LA PROXIMA VEZ...!")
        print("***")
        return True
    else:
        print("***")
        print("No hay ganador todavía.. continuemos!!!")
        print("***")
        cantidadJugadas += 1
        #print(cantidadJugadas)
        return False
def juego (tablero):
    #Primer jugada de la maquina, colocando una X en el centro
    print("")
    print("Turno de la maquina:")
    tablero[1][1] = 'X'
    imprimirTablero(tablero)
    ganador = verificarGanador(tablero) #Verificamos si hay un ganador
    while True:
        if ganador == False:
            jugadaUsuario(tablero)
            imprimirTablero(tablero)
            ganador = verificarGanador(tablero)
        else:
            break
        if ganador == False:
            jugadaMaquina(tablero)
            imprimirTablero(tablero)
            ganador = verificarGanador(tablero)
        else:
            break    


#Comienzo del programa
cantidadJugadas = 0  # Variable global para el número de movimientos realizados
tab=[[1,2,3], #Creamos la matriz
     [4,5,6],
     [7,8,9]]

Bienvenida(tab) #Llamamos a la funcion bienvenida para que presente el juego
juego(tab) #Comienza el juego!
import socket

DIRECCION = socket.gethostbyname(socket.gethostname())
PUERTO_JUGADOR = 5050
FORMATO = "utf-8"
INFO_SOCKET_JUGADOR = (DIRECCION, PUERTO_JUGADOR)

socket_jugador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket_jugador.connect(INFO_SOCKET_JUGADOR)
except:
    exit("Error al conectar el cliente al servidor intermedio, revise que el servidor intermedio este conectado.\n")

"""
Nombre: Tablero.
Parametros: Lista de listas de enteros, representa los valores del tablero.
Funcionamiento: Printea el tablero de gato
Retorno: String vacio, para evitar errores.
"""
def tablero(board):
    print(" 0  | 1 | 2 ")
    print("0 "+board[0][0]+" | "+board[0][1]+" | "+board[0][2])
    print(" ---+---+---")
    print("1 "+board[1][0]+" | "+board[1][1]+" | "+board[1][2])
    print(" ---+---+---")
    print("2 "+board[2][0]+" | "+board[2][1]+" | "+board[2][2])
    return " "

# Variables a usar para el tablero y empate.
board = [[" " for col in range(3)] for row in range(3)]
count = 0

print("-------- Bienvenido al Juego --------\n-Seleccione una opcion\n1-Jugar\n2-Salir")
mensajeSaliente = input('\t')

while True:
    socket_jugador.send(mensajeSaliente.encode(FORMATO))
    respuesta = socket_jugador.recv(1024).decode()
    respuesta=respuesta.split("|")

    #No se juega
    if mensajeSaliente == "2":  
        exit("OK")
    #El servidor gato no disponible, no se juega.
    if respuesta[0] =="NO":    
        exit("Servidor gato no disponible, intente nuevamente.\n")

    #Se puede jugar.
    elif respuesta[0] == "OK": 
        print("respuesta de disponibilidad: OK")
        print("-------- Comienza el Juego --------")

        #Primer Turno.

        print(tablero(board))
        print("Ingrese su jugada (x,y):")
        mensajeSaliente = input("\t")
        a = mensajeSaliente.split(",")
        b,c = int(a[0]), int(a[1])
        if board[b][c] == " ":
            board[b][c] = "X"
            count += 1
        
        else:
            print("Jugada Inválida, intente en otra casilla. No te equivoques de nuevo porfavor, primer strike.")
            mensajeSaliente = input("\t")
            a = mensajeSaliente.split(",")
            b,c = int(a[0]), int(a[1])
            board[b][c] = "X"
            count += 1
    
    #Caso si gana Cliente
    elif respuesta[0] == "Client":
        print("------- Termino el Juego -------")
        tablero(board)
        exit("\n\n\t\t ..:: Ganador Client ::.. \n")
    
    #Caso si gana BOT
    elif respuesta[0] == "BOT":
        print("------- Termino el Juego -------")
        a = (respuesta[1]).split(",")
        b,c = int(a[0]), int(a[1])
        board[b][c] = "O"
        tablero(board)
        exit("\n\n\t\t ..:: Ganador BOT ::.. \n")
    
    #Caso si hay EMPATE
    elif respuesta[0] == "Empate":
        print("------- Termino el Juego -------")
        tablero(board)
        exit("\n\n\t\t ..:: Empate ::.. \n")

    else:   
        #Turno BOT
        print("Jugada Bot", respuesta[1], "\n")
        a = (respuesta[1]).split(",")
        b,c = int(a[0]), int(a[1])
        board[b][c] = "O"
        count += 1

        #Turno Cliente    
        print(tablero(board))
        print("Ingrese su jugada (x,y):")
        mensajeSaliente = input("\t")
        a = mensajeSaliente.split(",")
        b,c = int(a[0]),int(a[1])
        if board[b][c] == " ":
            board[b][c] = "X"
            count += 1
        else:
            #Si el cliente se equivoca, otra oportunidad.
            print("Jugada Inválida, Intente en otra casilla. No te equivoques de nuevo.")
            mensajeSaliente = input("\t")
            a = mensajeSaliente.split(",")
            b,c = int(a[0]), int(a[1])
            if board[b][c] == " ":
                board[b][c] = "X"
                count += 1
            else:
                #Se equivoco dos veces, se termina el juego.
                mensajeSaliente = "RIP"
                socket_jugador.send(mensajeSaliente.encode(FORMATO))
                exit("Jugada invalida, 2do y ultimo strike.")
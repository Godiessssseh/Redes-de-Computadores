import socket

#Informacion para los sockets.
FORMATO = "utf-8"
PUERTO_JUGADOR = 5050
PUERTO_GATO= 8002 #!DEJAR UNO ENTRE 8000 Y 65535
DIRECCION = socket.gethostbyname(socket.gethostname())
socket_servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_gato = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

INFO_SOCKET_JUGADOR = (DIRECCION, PUERTO_JUGADOR)
INFO_SOCKET_GATO = (DIRECCION, PUERTO_GATO)

#Revisar errores
try:
    socket_servidor.bind(INFO_SOCKET_JUGADOR)
except socket.error as mensaje_error:
    exit("Fallo en la union del puerto del jugador con la IP del servidor intermedio, intente nuevamente en unos segundos.")

"""
Nombre: Win
Parametros: Lista, representa el tablero; Entero, representa la cantidad de movimientos hasta el momento.
Funcionamiento: Revisa quien es el ganador.
Retorno: String, representa una respuesta a si es que hay algun ganador
"""
def Win(board, count):
    for i in range(3):
        #Gana X Horizontal
        if board[i][0] == "X" and board[i][1] == "X" and board[i][2] == "X":
            return "Client"

        #Vertical
        elif board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            return "Client"

        #Gana O
        elif board[i][0] == "O" and board[i][1] == "O" and board[i][2] == "O":
            return "BOT"
        
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            return "BOT"

    #Revision de diagonales
    #Gana X
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return "Client"

    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return "Client"

    #Gana O
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return "BOT"

    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return "BOT"

    #Si no ocurre ninguna de las anteriores, significa que nadie gano-> empate.
    elif count == 9:
        return "Empate"

    else:
        return "No hay ganador"


"""
Nombre: revisar
Parametros: String, representa resultado entregado por la funcion Win()
Funcionamiento: Recibe el resultado de la funcion win y retorna un resultado final, revisando si existe ganador, o empate.
Retorno: Sting, representa el ganador en caso de que haya, sino retorna un espacio. 
"""

def revisar(ganador):
    if ganador == "Client":
        return "Client"
             
    elif ganador == "BOT":
        return "BOT"

    elif ganador == "Empate":
        return "Empate"
    else:
        return " "

#Inicializar la matriz vacía y los turnos igual a 0.
board = [[" " for col in range(3)] for row in range(3)]
count = 0


# ----- Empieza todo. -----
print("Encendiendo servidor")
socket_servidor.listen(1)
print(f"El servidor ya esta esperando conexiones del jugador en la direccion {DIRECCION}, en el puerto {PUERTO_JUGADOR}")


while True:
    socket_jugador, direccionJugador = socket_servidor.accept()
    print(f"El servidor acepto la conexion, {direccionJugador} se conecto")

    while True:
        
        mensaje = socket_jugador.recv(1024).decode(FORMATO)  
        print(f"{direccionJugador} envia el mensaje: {mensaje}")

        socket_gato.sendto(mensaje.encode(), INFO_SOCKET_GATO)
        print("Esperando respuesta de disponibilidad del servidor gato")
        mensajeServerGato, direccionServerGato = socket_gato.recvfrom(1024)
        mensajeServerGato=(mensajeServerGato.decode()).split("|")

        #Servidor gato disponible.
        if (mensajeServerGato[0])== "OK": #? Aca revisamos si es que el servidor gato esta disponible
            print("Llego el ok del gato")
            mensajeConfirmacion="OK| "
            socket_jugador.send(mensajeConfirmacion.encode())
            continue

        #Servidor gato NO esta disponible    
        elif (mensajeServerGato[0]) == "NO":
            mensajeErrorConexionGato="NO| "
            socket_jugador.send(mensajeErrorConexionGato.encode())
            break
        
        #Servidor Gato desconectado.
        elif (mensajeServerGato[0]) == "END":
            socket_gato.close()
            socket_jugador.close()
            socket_servidor.close()
            print("Servidor intermedio cerrado")
            break

        #Caso borde donde el Cliente tuvo la ultima jugada.
        elif (mensajeServerGato[0]) == "CHECK":
            count+=1
            #Caso borde donde el jugador puede ganar con la ultima jugada.
            for i in range(0,3):
                for j in range(0,3):
                    print("Tablero posicion",board[i][j],"posicion",i,",",j)
                    if board[i][j] == " ":
                        board[i][j] = "X"
            
            print("Revisando caso de empate o victoria de client, cantidad de turnos=", count)
            rev = revisar(Win(board,count))
            print("Revision:", rev)
            mensaje = rev
            socket_gato.sendto(mensaje.encode(), INFO_SOCKET_GATO)
            socket_gato.close()
            socket_jugador.send(mensaje.encode())
            socket_jugador.close()
            socket_servidor.close()
            break
        
        #Caso borde cuando el usuario ingresa dos movimientos invalidos de manera consecutiva.
        elif mensaje=="RIP":
            PUERTO_GATO=int(mensajeServerGato[1]) #Actualiazmos el puerto anterior, al nuevo puerto de conexion con el server gato
            INFO_SOCKET_GATO=(DIRECCION, PUERTO_GATO)
            socket_gato.sendto(mensaje.encode(), INFO_SOCKET_GATO)
            socket_gato.close()
            socket_jugador.close()
            socket_servidor.close()
            break
        else:  
            #Juega Jugador 1
            a = mensaje.split(",")
            b, c = int(a[0]), int(a[1])
            if board[b][c] == " ":
                board[b][c] = "X"
                count += 1

            #Se revisa si gano el Client
            rev = revisar(Win(board,count))
                
            if rev != " ":
                print(rev)
                mensaje2 = rev
                socket_gato.sendto(mensaje2.encode(), INFO_SOCKET_GATO)
                socket_gato.close()
                mensaje2 = mensaje2+"|"+mensaje
                socket_jugador.send(mensaje2.encode())
                socket_jugador.close()
                socket_servidor.close()
                break

            #Sino gano o empate, le toca al BOT
            mensajeserver2 = mensajeServerGato[0]
            a = mensajeserver2.split(",")
            b,c = int(a[0]),int(a[1])
            if board[b][c] == " ":
                board[b][c] = "O"
                count += 1

            #Revisar si el bot Gana

            rev = revisar(Win(board,count))
            if rev != " ":
                print(rev)
                mensaje2 = rev
                socket_gato.sendto(mensaje2.encode(), INFO_SOCKET_GATO)
                socket_gato.close()
                mensaje2 = mensaje2+"|"+mensajeServerGato[0]
                socket_jugador.send(mensaje2.encode())
                socket_jugador.close()
                socket_servidor.close()
                break

            mensajeServerGato = " |"+mensajeServerGato[0]
            socket_jugador.send(mensajeServerGato.encode())
    break

print("\n\n \t\t..:: Juego terminado ::..\n\n")
socket_gato.close()
socket_jugador.close()
socket_servidor.close()
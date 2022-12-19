package main

import (
	"fmt"
	"math/rand"
	"net"
	"strconv"
	"time"
)

/*
* Nombre: remove
* Parametros: Una lista de strings y un string.
* Funcion: Busca el string entregado, dentro de la lista entregada; lo elimina y devuelve la lista nueva sin ese valor.
* Retorno: Lista, con el string en cuestion ya eliminado.
 */
func remove(s []string, r string) []string {
	for i, v := range s {
		if v == r {
			return append(s[:i], s[i+1:]...)
		}
	}
	return s
}

func main() {
	PORT := ":8002"
	BUFFER := 1024
	s, err := net.ResolveUDPAddr("udp4", PORT) //Se especifica tipo y puerto de conexion

	if err != nil { //Error handling
		fmt.Println(err)
		return
	}

	connection, err := net.ListenUDP("udp4", s) //Deja "escuchando" a la conexion en la direccion entregada
	if err != nil {                             //Error handling
		fmt.Println(err)
		return
	}

	defer connection.Close()
	buffer := make([]byte, BUFFER)
	//Lista de los posibles valores del bot.
	p := []string{"0,0", "0,1", "0,2", "1,0", "1,1", "1,2", "2,0", "2,1", "2,2"}
	//Inicializa un generador de valores al azar
	rand.Seed(time.Now().Unix())

	for true {
		fmt.Println("Esperando mensaje del servidor intermedio")
		n, addr, _ := connection.ReadFromUDP(buffer)
		msg := string(buffer[:n])
		fmt.Println("Direccion Cliente:", addr)
		fmt.Println("mensaje del servidor intermedio:", msg)
		//?Manejar probabilidades. 80% de que funcione y un 20% de que falle.
		if msg == "1" {
			prob := rand.Intn(10) //? Genera un numero random entre 0 y 9
			//?80% de probabilidad
			if prob <= 7 {

				newport := rand.Intn(57565) + 8000 //Generamos un nuevo puerto al azar
				npstr := strconv.Itoa(newport)     //Casteamos el entero que representa el puerto a un string

				responde := []byte("OK|" + npstr)            //OK|PUERTO
				_, _ = connection.WriteToUDP(responde, addr) //Escribimos el mensaje con el puerto nuevo, hacia el puerto dado.
				RANDOM_PORT := ":" + npstr                   //: + VALOR ENTRE 8000 Y 57565

				//Se necesita un nuevo BUFFER.

				s2, err2 := net.ResolveUDPAddr("udp4", RANDOM_PORT) //Se especifica tipo y nuevo puerto random de conexion
				if err2 != nil {                                    //Error handlind
					fmt.Println(err2)
					return
				}
				fmt.Println("Ejecutando servidor gato en el puerto :", RANDOM_PORT) // Indicamos en que puerto aleatorio se ejecutara

				connection, err2 := net.ListenUDP("udp4", s2) //Deja "escuchando" a la nueva conexion en la direccion entregada
				_ = connection
				if err2 != nil { //Error handlind
					fmt.Println(err2)
					return
				}

				//? 20% de probabilidad de que no funcione

			} else {
				fmt.Println("---Servidor gato, no disponible---")
				response := []byte("NO")
				_, _ = connection.WriteToUDP(response, addr)
				fmt.Println("cerrando bot")
				break
			}
			//No quiere jugar.

		} else if msg == "2" {
			fmt.Println("cerrando bot")
			response := []byte("END")
			_, _ = connection.WriteToUDP(response, addr)
			break

			//Si sale RIP, es porque el Cliente eligió dos movimientos inválidos consecutivos.

		} else if msg == "RIP" {
			fmt.Println("cerrando bot")
			response := []byte("RIP GATO")
			_, _ = connection.WriteToUDP(response, addr)
			break

			//Caso si gana Cliente
		} else if msg == "Client" {
			fmt.Println("Ganador Client")
			break

			//Caso si gana BOT
		} else if msg == "BOT" {
			fmt.Println("Ganador BOT")
			break

			//Caso si gana Empate
		} else if msg == "Empate" {
			fmt.Println("No hay ganador")
			break

			//Jugada BOT
		} else {

			fmt.Println(msg)

			p = remove(p, msg) // se remueve el valor al azar de la list
			//Si la lista se acaba, se revisa si hay empate o si el cliente gana.

			if len(p) == 0 {
				response := []byte("CHECK")
				_, _ = connection.WriteToUDP(response, addr)
				fmt.Println("Revisar Empate o Victoria del Usuario.")
			} else {
				number := rand.Intn(len(p))
				fmt.Println("Jugada Bot ", p[number])

				//? De aqui comienza la creacion del nuevo puerto random
				newport := rand.Intn(57565) + 8000
				npstr := strconv.Itoa(newport)
				RANDOM_PORT := ":" + npstr //: + VALOR ENTRE 8000 Y 57565
				//Se necesita un nuevo BUFFER.

				s2, err2 := net.ResolveUDPAddr("udp4", RANDOM_PORT)
				if err2 != nil {
					fmt.Println(err2)
					return
				}
				fmt.Println("Ejecutando servidor gato en el puerto :", RANDOM_PORT) // Indicamos en que puerto aleatorio se ejecutara
				connection, err2 := net.ListenUDP("udp4", s2)
				if err2 != nil {
					fmt.Println(err2)
					return
				}
				//? Hasta aqui llega la creacion del nuevo puerto random

				response := []byte(p[number] + "|" + npstr)
				p = remove(p, p[number])

				_, _ = connection.WriteToUDP(response, addr)
				fmt.Println("Se mando la respuesta.")
			}

		}
	}
}

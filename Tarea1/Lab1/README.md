☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･

# ( ͡° ͜ʖ ͡°)ﾉ README Laboratorio 1 Redes De Computadores (◕ᴥ◕ʋ)

>Fecha entrega: Lunes 11 de Abril del 2022  
>**Integrante 1**: Diego Rosales Leon, *201810531-7*, paralelo 201  
>**Integrante 2**: Alan Zapata Silva, *201956567-2*, paralelo 201  

##### Consideraciones a tomar en cuenta:
- El cliente siempre tiene el primer turno y el último turno.
- Correr siempre el Servidor Intermedio. Si este no se corre, el *ServidorCliente.py* devolverá un error de conexión, mientras que el *ServidorGato.go* esperará la conexión.

###### Servidor Gato: 
- La probabilidad de que el servidor este activo es de un 80%

##### Archivos:
- *ServidorCliente.py*: Funcionamiento del cliente, conecta con el servidor intermedio.  
- *ServidorIntermedio.py*: Funcionamiento del Servidor Intermedio, conecta al **Cliente** mediante **_TCP_** y al **Gato** mediante **_UDP_**.  
- *ServidorGato.py*: Funcionamiento del Gato, conecta con el servidor intermedio.  

##### Detalles para una correcta ejecución:
- Los archivos *ServidorCliente.py*, *ServidorGato.go* y *ServidorIntermedio.py* deben estar en el mismo directorio.  

##### Instrucciones ejecución:
- Se debe correr primero el *ServidorIntermedio.py* a través de consola usando `python3 ServidorIntermedio.py`.  
- Luego se puede correr cualquiera de los otros dos archivos, `go run ServidorGato.go` y `python3 ServidorCliente.py`.  

*Programado en VSCode, testeado en Ubuntu 20.04, Python (3.10.4 y 3.9.0) y Go 1.18*  
☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ.☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. * ･ ｡ﾟ☆ﾟ. 
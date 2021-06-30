mensaje='Hola mundo!'

#ljust -> justifica a la izquierda
#rjust -> justifica a la derecha
#center -> centrar

mensaje=mensaje.ljust(20) #anade 20 espacios a la derecha del string
mensaje=mensaje.center(20) #anade 10 espacios a la izquierda y 10 a la derecha
print(mensaje)

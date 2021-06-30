uno, dos, tres, cuatro = 1, 2, 3, 4
print(uno)
print(dos)
print(tres)
print(cuatro)


# descomprimir valores de una tupla
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # tambien sirve con listas []
# *resto_valores a partir del cuarto valor, los valroes restantes se asignan a una lista
# en lugar de *resto_valores --> *_ se omiten los siguientes valores
#  si despues de *_ seguimos escribiendo variables se obtienen los ultimos valores
#   _ Omite este valor nadamas         *_ omite los siguientes valores
uno_t, _, tres_t, cuatro_t, *resto_valores, nueve_t, diez_t = numeros
print(uno_t)
print(tres_t)
print(cuatro_t)
print(nueve_t)
print(diez_t)
print(resto_valores)

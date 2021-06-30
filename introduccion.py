# Saber el tipo de variable
valor = 'Hola'
numero = 234
print(type(valor), type(numero))

'''
Este es un comentario 
el cual contiene 
varios saltos de linea
'''


# Ingresar valores de entrada
nombre_completo = input('Ingresa tu nombre completo: ')
print('Hola ', nombre_completo)
edad = input('Ingresa tu edad: ')
edad = int(edad)  # convertir str a int
print(edad, type(edad))
# Ingresa tu altura
altura = input('Ingresa altura: ')
altura = float(altura)
print(altura, type(altura))


# Crear multiples variables
nombre, apellido, titulo = 'Luis', 'Perez', 'Ing. '
print(nombre)
print(apellido)
print(titulo)

# iguales a las lista, pero las tuplas no pueden modificar el valor de sus elementos ni la longitud de esta
# las tuplas solo son para lectura
# almacena cualquier tipo de variables

#           0    1    2    3        4          5
tupla = ('Hola', 3, 13.2, True, [1, 2, 3], (4, 5, 6))
print(tupla)
# tupla[0] = 0 marca error por que no se puede modificar un elemento de una tupla
cursos = ('Python', 'Flask', 'Django', 'Rails', 'MongoDB')
print(cursos[0])
print(cursos[-1])
subtupla = cursos[1:4]
print(subtupla)
print(cursos[:2])

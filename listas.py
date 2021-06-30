lista = ['Hola', 10, 4.3, True]  # o tambien se puede usar --> list()
print(lista)

#                  0         1         2        3      4       5      6
#                 -7        -6        -5       -4     -3      -2     -1
lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'CSS', 'HTML']
print(lista_cursos[0])
print(lista_cursos[-3])

lista_cursos[1] = 'Javascript'  # reemplazando un elemento
print(lista_cursos)


# sublistas
# [start:end] --> Sublista con inicio y fin
# [start:] -->Obtenemos los ultimos elementos de la lista
# [:end] --> Obtenemos los primeros elementos de la lista
# [start:end;skip] --> sublista inicio fin con saltos
print(lista_cursos[0:3])
print(lista_cursos[1:])
print(lista_cursos[:4])
print(lista_cursos[1:6:2])

# append(elemento) --> anade elemento al final de la lista
# insert(n,elemento) --> anade elemento en el indice n
# lista1.extend(lista2) --> anade los elementos de la lista 2 al final de la lista 1
# lista1.remove(elemento) --> elimina varaible elemento de lista1f
# del lista1[n] elimina --> variable del indice n de la lista 1
# lista1.clear() --> elimina todos los elementos de la lista
lista_cursos.append('MongoDB')
lista_cursos.append('C#')
print(lista_cursos)
print(len(lista_cursos))
lista_cursos.insert(1, 'Rails')
print(lista_cursos)

lista_cursos2 = ['C', 'C++', 'Docker']
lista_cursos.extend(lista_cursos2)
print(lista_cursos)
print(lista_cursos2)
lista_cursos.remove('MongoDB')
del lista_cursos[0]
print(lista_cursos)
lista_cursos.clear()
print(len(lista_cursos))

# metodos de listas
# lista.sort() --> ordena la lista ascendentemente
# lista.sort(reverse=True)
# min(lista) o max(lista) -->min y max permite conocer el mayor y menor elemento de una lista
# 10 in lista --> busca 10 en la lista, devuelve T or F
# 11 not in lista --> devuelve true si 11 no esta en lista
# lista.index(n) --> Devuelve el indice en donde esta n (Devuelve el primer indice encontrado)

lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)
print(min(lista), max(lista))
print(10 in lista)
print(600 in lista)
print(11 not in lista)
print(lista.index(600))


# matrices
columna_a = [10, 20, 30, 40]
columna_b = [50, 60, 70, 80]

matriz = [columna_a, columna_b]  # matriz de 2x4
print(matriz)
print(matriz[0][0], matriz[1][0], matriz[0][1], matriz[1][1])

diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

#formas para borrar elementos del diccionario
del diccionario['a'] #1
valor=diccionario.pop('b') #2
diccionario.clear() #3 elimina todos los elementos del diccionario

print(valor)
print(diccionario)
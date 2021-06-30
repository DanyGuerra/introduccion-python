diccionario={'a':1,'b':2,'c':3,'d':4}


print('a' in diccionario) # para saber si una llave existe en el diccionario

valor=diccionario['b']
print(valor)


#get obtner --> el valor de una llave de forma segura devuelve none (ausencia de valor) si no existe
#setdefault('e',5) --> si la llave no existe le asigan el segundo argumento
valor=diccionario.get('z', 'La llave no existe en el diccionario') #si la llave no existe retorna el valor del segundo argumento
valor=diccionario.setdefault('e',5)
print(diccionario)

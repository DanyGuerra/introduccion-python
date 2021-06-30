titulo_curso='Curso profesional de Python, donde se ve Python'

contador=titulo_curso.count('Python') #devuelve las veces que esta el string en otro string
print(contador)


#lower y upper convierte el String a miniscula y mayusculas para estandarizar
print('python' in titulo_curso.lower()) #devuelve valor booleano para ver si existe el string en

print(titulo_curso.startswith('Curso')) #devuelve true si esta la palabra al inicio del string
print(titulo_curso.endswith('Curso'))
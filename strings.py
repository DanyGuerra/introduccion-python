# split
lenguajes = 'Pyrhon//Ruby//Java//Rust//C++//C'
# metodo split genera un listado por default separa donde hay espacio, pero se puede usar cualquier caracter
# el segundo argumento es el numero que divide y los demas los agrupa en una sola variable
listado_lenguajes = lenguajes.split('//', 3)
listado_lenguajes2 = lenguajes.split('//')
print(listado_lenguajes)
print(listado_lenguajes2)

# join une los elementos del listado en una variable (Inverso de split)
lenguajes = ['Python', 'Ruby', 'Java', 'Rust']
string_lenguajes = '/'.join(lenguajes)
print(string_lenguajes)


# concatenar
nombre = 'Luis Daniel'
apellido = 'Guerra'
nombre_completo = 'Ing.' + nombre + ' ' + apellido + '.'
print(nombre_completo)

nombre_completo2 = 'Mr. %s %s %s.' % (nombre, apellido, 'Perez')
print(nombre_completo2)

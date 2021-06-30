lista = [1, 2, 3, 4, 5]
tupla = (10, 20, 30, 40, 50)
lista_2 = [100, 200, 300, 400, 500]
tupla_2 = (1000, 2000, 3000, 4000, 5000)

# --> zip comprime elementos se puede comprimir solo listas o solo tuplas o combinadas
# si se tienen de diferentes tamanos se omiten los elementos que estan de mas
resultado = zip(lista, tupla, lista_2, tupla_2)
resultado = tuple(resultado)  # convierte a tupla o se puede usar list

print(resultado)

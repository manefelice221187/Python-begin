#valor_uno = 10
#valor_dos = 20
#valor_tres = 10 * 20


#valor_uno == valor_dos
#diferente = valor_uno != valor_dos
#resultado = True or False and diferente
#resultado2 = not False

#print(resultado)
#print(resultado2)
#print(valor_uno)
#print(valor_dos)
#print(valor_tres)

"""
este es un comentario 
para ingresar
"""

nombre = input("Cual es tu nombre?: ")
Edad = int(input("Cual es tu Edad? \n"))

print("Cual es tu Peso?")
Peso = float(input())

print("Estas autorizado (Si/NO)")
Autorizado = input() == "Si"

print("Hola", nombre)
print("Tenes", Edad)
print("Pesas", Peso)
print("Estas Autorizado", Autorizado)


"""
listas
"""
#[0,1,2,3] posiciones. Permite [-1] toma la ultima posicion de la lista
lista = [1,23, 15, 19,50,70]

elemento = lista[1]
print(elemento)

sub = lista[0:2]
sub1 = lista[0:7:2]#salto de dos en dos

#inverso de la lista
sub2 = lista[::-1]

"""
Estas son las formas en las cuales podemos crear una nueva lista (sublistas) a partir de otra.

[:] Todos los elementos.
[start:] Todos los elementos desde el índice establecido(start).
[:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
[start:end] Todos los elementos de un rango de índices.
[start:end:step] Todos los elementos de un rango de índices con saltos.
"""
lista2 = [1,80, 155, 19,50,70]
lista2.sort() #ordena la lista de manera ascendente
menor[0]
print(menor) # o menor = min(lista2)


lista2.sort(reverse=True) #ordena la lista de manera descendente
mayor[0] # mayor = max(lista2)
print(mayor)#imprime el mayor

longitud = len(lista2)
print(longitud)

#in
result = 8 in lista2
print(result)

#indice
indice = index(lista2)

#contador del numero q se pone
contador = lista2.count(80)

#matrices
fila_uno = [10,20]
fila_dos = [30,40]

matriz = [fila_uno, fila_dos]
primer_element = matriz[0][0]
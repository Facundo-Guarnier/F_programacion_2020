print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Realizar un programa que ingrese una cadena de caracteres por teclado y
    devuelva una lista con cada palabra que contiene la frase y su frecuencia de aparición.
    Aclaración: debe resolver con diccionarios.
    Ejemplo:
        Frase:'Como quieres que te quiera si el que quiero que me quiera no me quiere como
        quiero que me quiera'
        Salida: {'Como': 1, 'quieres': 1, 'que': 4, 'te': 1, 'quiera': 3, 'si': 1, 'el': 1, 'quiero': 2, 'me': 3,
        'no': 1, 'quiere': 1, 'como': 1}
"""

cadena = input("Ingrese una cadena de caracteres: ")
cantidad = []
diccionario = {}

l_palabras = cadena.split()

for i in l_palabras:
    cantidad.append(l_palabras.count(i))

for i in range(len(l_palabras)):
    diccionario[l_palabras[i]] = cantidad[i]

print(diccionario)

#Facundo Guarnier

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
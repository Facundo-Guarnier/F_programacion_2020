print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Diseña un programa que lea una cadena y un número entero c y nos diga cuántas
    palabras tiene una longitud de c caracteres. 
"""

frase = str(input("Ingrese una frase: "))
c = int(input("Ingrese una longitud: "))

contador = 0
indice = 0
cantidad = 0
while indice < len (frase):
    elemento = frase [indice]
    if (elemento != " "):
        contador += 1
    elif (elemento == " "):
        if contador == c:
            cantidad += 1
        contador = 0
    indice += 1
if contador == c:
    cantidad += 1

print("Las parabras de longitud '" + str(c) + "' son: ", cantidad)

print("\n++++++++++++++++++++++++++++++++++++++ Fin +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
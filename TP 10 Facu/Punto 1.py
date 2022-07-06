print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
    muestre por pantalla el número de veces que aparece la letra en la frase.

"""

frase = str(input("Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))
contador = 0

for i in frase:
    if (i == letra):
        contador += 1

print("La letra '" + letra + "' se repite", contador, "veces.")

print("\n++++++++++++++++++++++++++++++++++++++ Fin +++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que mediante una función contar_vocales() reciba una palabra y
    cuente cuantas letras “a” tiene, cuantas letras “e” tiene y así hasta completar todas las vocales. 
"""

def contar_vocales(vocal):
    cantidad = 0
    for j in palabra:
        if (vocal == j):
            cantidad += 1
    print("La vocal '" + vocal + "' está", cantidad)

palabra = input("Ingrese una palabra: ").lower()
print(palabra)
vocales = ["a", "e", "i", "o", "u"]

for i in vocales:
    contar_vocales(i)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
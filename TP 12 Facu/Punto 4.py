print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
Escriba un programa que permita crear una lista de palabras y que, a continuación,
cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, sino
de crear una lista distinta).
"""

mi_lista1 = []
mi_lista2 = []
longitud = int(input("Ingrese la cantidad de palabras que desea: "))

for i in range(longitud):
    mi_lista1.append(input("Ingrese una palabra: "))

for i in reversed(mi_lista1):
    mi_lista2.append(i)

print("Lista original: ", mi_lista1)
print("Nueva lista invertida de la original: ", mi_lista2)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que permita crear una lista de palabras y que, a continuación,
    elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
"""

mi_lista = []
longitud = int(input("Ingrese la cantidad de palabras que desea: "))

for i in range(longitud):
    mi_lista.append(input("Ingrese una palabra: "))
    if mi_lista.count(mi_lista[len(mi_lista) - 1]) == 2:
        mi_lista.pop()

print(mi_lista)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
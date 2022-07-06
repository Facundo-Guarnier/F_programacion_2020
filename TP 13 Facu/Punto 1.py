print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que permita crear una tupla con 15 números e indique cual es
    el elemento mayor y cual el menor. Imprima la tupla, el elemento mayor y el elemento menor. 
"""

mi_lista = []
for i in range(5):
    mi_lista.append(int(input("Ingrese un numero: ")))

mi_tupla = tuple(mi_lista)


print("----------- Opción 1 -----------")

mi_lista.sort()
mayor = mi_lista[-1]
menor = mi_lista[0]
print("Tupla: ", mi_tupla, "\nEl mayor numero es:", mayor, "\nEl menor numero es: ", menor)


print("----------- Opción 2 -----------")

print("Tupla: ", mi_tupla, "\nEl mayor numero es:", max(mi_tupla), "\nEl menor numero es: ", min(mi_tupla))

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
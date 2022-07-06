print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que permita al usuario ingresar 10 valores a una lista, calcular el
    promedio, su mínimo y máximo valor. Imprimir todos los resultados y la lista.
"""

mi_lista = []

for i in range(10):
    mi_lista.append(int(input("Ingrese un elemento: ")))

print(mi_lista)

print("El promedio es:", sum(mi_lista) / len(mi_lista))
print("Mayor valor", max(mi_lista))
print("Menor valor", min(mi_lista))


print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
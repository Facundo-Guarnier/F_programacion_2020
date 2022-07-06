print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que permita crear una lista de palabras y que, a continuación,
    pida dos palabras y sustituya la primera por la segunda en la lista.
"""

mi_lista = ["Palabra1", "Palabra2", "Palabra3", "Palabra4"]
ingresada1 = input("Ingrese la primera palabra: ")
ingresada2 = input("Ingrese la primera segunda: ")
mi_lista[1] = ingresada1
mi_lista[0] = ingresada2
print(mi_lista)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
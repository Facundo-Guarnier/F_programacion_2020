print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribe un programa para construir el siguiente patrón, usando dos bucles 'for' anidados.
        *
        * *
        * * *
        * * * *
        * * * * *
        * * * *
        * * *
        * *
        *
    Tip: Investigar el uso del parámetro 'end' de la función 'print()'.
"""

símbolo = "* "
for i in range(1, 5):
    print(símbolo * i)

for i in range(5, 1, -1):
    print(símbolo * i)
print(símbolo)

print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")
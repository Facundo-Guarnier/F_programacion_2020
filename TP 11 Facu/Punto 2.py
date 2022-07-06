print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que mediante una función pida una cadena e indique si es palíndromo o no. 

    Por ejemplo: "Dábale arroz a la zorra el abad"
"""

def palindromo(cadena):
    if cadena == cadena[ : :-1]:
        print("Si es palíndromo")
    else:
        print("No es palíndromo")

frase = input("Ingrese una frase: ")
frase = frase.lower().replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u").replace(" ", "")
palindromo(frase)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
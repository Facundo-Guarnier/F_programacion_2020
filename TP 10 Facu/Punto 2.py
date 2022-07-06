print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Realizar un programa que se ingrese una palabra por teclado y de como resultado la
    misma, escrita de atrás hacia adelante. Por ejemplo: FRUTILLA de como resultado ALLITURF.
"""

palabra = str(input("Ingrese una palabra: "))
indice = len (palabra)
letra = ""
while indice > 0:
    indice -= 1
    letra = letra + palabra [indice]
print(letra)
    
print("\n++++++++++++++++++++++++++++++++++++++ Fin +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
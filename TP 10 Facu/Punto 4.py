print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Diseñar un programa que lea un carácter cualquiera desde el teclado, y muestre el
    mensaje “Es una MAYÚSCULA” cuando el carácter sea una letra mayúscula y el mensaje “Es
    una MINÚSCULA” cuando sea una minúscula. En cualquier otro caso, mostrar el mensaje “No es
    una letra”. 
    Pista: aunque parezca una obviedad, recuerda que una letra es minúscula si esta
    entre la ’a’ y la ’z’, y mayúscula si está entre la ’A’ y la ’Z’
"""

caracter = str(input("Ingrese un caracter: "))

if ((len(caracter)) == 1):
    if (caracter != caracter.upper()) and (caracter == caracter.lower()):
        print("El caracter esta en minúscula")
    elif (caracter != caracter.lower()) and (caracter == caracter.upper()):
        print("El caracter esta en mayúscula")
    else :
        print("El caracter es no es una letra")
else:
    print("Se han ingresado múltiples caracteres.")

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n++++++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que permita ingresar el nombre completo de una persona, y
    devuelva la cantidad de letras, sin contar los espacios en blanco, que suma en total el
    nombre de la persona.

    Se debe repetir el ingreso para 5 personas.
    Ejemplo:
        Ingresar nombre: Rodrigo Rodríguez Del Campo
        Devuelve:
        El nombre ingresado contiene 24 letras.

    Nota: Recordar que una cadena de texto constituye una secuencia de caracteres que se puede
    recorrer mediante un bucle for.
"""

for cantidad_nombre in range(1, 6):
    cantidad = 0
    nombre = str(input("Ingrese un nombre: "))
    for letras in nombre:
        if (letras == " "):
            continue
        cantidad += 1
    print("EL nombre N°", cantidad_nombre, "es de", cantidad)

print("\n++++++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++\n")
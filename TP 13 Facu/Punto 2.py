print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que permita crear un diccionario donde la clave sea el nombre
    del usuario y el valor sea el teléfono. Tendrás que ir pidiendo contactos hasta el usuario diga que
    no quiere insertar mas. No se podrán introducir nombres repetidos.
"""

contactos = {}

while True:
    nombre = input("\nIngrese el nombre del contacto, si desea termina escriba 'listo': " )
    if nombre == "Listo" or nombre == "listo":
        break
    elif ((nombre in contactos) == True):
        print("\nYa hay un contacto con ese nombre, pruebe con un apodo")
        continue
    telefono = input("\nIngrese el numero de telefono: ")
    contactos[nombre] = telefono

print(contacto)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n++++++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Usando una estructura while, escribir un programa que cuente la cantidad de dígitos ingresados.
    Debe pedir al usuario ingresar una clave de 6 dígitos por teclado.

    Como resultado, avisar si la clave ingresada es válida, es decir que se ingresaron exactamente 6
    dígitos, o si fue inválida. También debe mostrar por pantalla la cantidad de dígitos ingresados.
    Ejemplo:
        Ingresar clave: 1234567
        Devuelve:
        “La clave es inválida”
        “Ingresó una clave de 7 dígitos“
        Ingresar clave: 223344
        Devuelve:
        “La clave es válida”
        “Ingresó una clave de 6 dígitos“

    Ayuda: utilizar en forma iterativa la operación aritmética de división entera “// 10”, de modo de ir
    reduciendo de a una unidad y poder contar los dígitos.
"""

cantidad = 0
clave = str(int(input("Ingrese una clave: ")))
while True:
    cantidad = len(clave)
    if (cantidad == 6):
        print("La clave es válida \nIngresó una clave de 6 dígitos")
        break
    else:
        print("La clave no es válida \nNo ingresó una clave de 6 dígitos")
    clave = str(int(input("Ingrese una clave: ")))

print("\n++++++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++\n")
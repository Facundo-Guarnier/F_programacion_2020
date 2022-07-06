print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir una función llamada recortar(numero, minimo, maximo) que reciba
    tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el
    tercero el límite superior. La función tendrá que cumplir lo siguiente:
        * Devolver el límite inferior si el número es menor que éste
        * Devolver el límite superior si el número es mayor que éste.
        * Devolver el número sin cambios si no se supera ningún límite.
"""

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

digito = input("Ingrese un numero a recortar: ")
a = input("ingrese un minimo: ")
b = input("Ingrese un maximo: ")

print("Su numero es: ", recortar(digito, a, b))

#Facundo Guarnier

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
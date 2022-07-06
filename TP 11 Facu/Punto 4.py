print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que simule una calculadora simple mediante cuatro funciones:
        1. función suma()
        2. función resta()
        3. función multiplicación()
        4. función división()
    El programa debe tener un menú que permita al usuario elegir la operación a calcular, dicho
    calculo se puede repetir las veces que el usuario desee.
"""

def función_suma(a, b):
    print("El resultado es: ", a + b)

def funciona_resta(a, b):
    print("El resultado es: ", a - b)

def funciono_multiplicación(a, b):
    print("El resultado es: ", a * b)

def función_division(a, b):
    if b == 0:
        print("No se puede dividir por cero")
    else:
        print("El resultado es: ", a / b)

while True:
    numero1 = float(input("Ingrese el primer numero: "))
    numero2 = float(input("Ingrese el segundo numero: "))
    calculo = int(input("¿Que operación decea hacer? \n1 : Suma \n2 : Resta \n3 : Multiplicación \n4 : Division \n5 : Salir \nIngrese el dígito correspondiente: "))

    r = False
    while r == False:
        if (calculo == 1 or calculo == 2 or calculo == 3 or calculo == 4 or calculo == 5):
            r = True
        else:
            print("\nIngrese un dígito valido")
            calculo = int(input("1 : Suma \n2 : Resta \n3 : Multiplicación \n4 : Division \nIngrese el dígito correspondiente: "))

    if (calculo == 1):
        función_suma(numero1, numero2)
    elif (calculo == 2):
        funciona_resta(numero1, numero2)
    elif (calculo == 3):
        funciono_multiplicación(numero1, numero2)
    elif (calculo == 4):
        función_division(numero1, numero2)
    elif (calculo == 5):
        print("Finalizando app...")
        break

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
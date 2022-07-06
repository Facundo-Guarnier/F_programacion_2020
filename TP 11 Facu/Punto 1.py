print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa, mediante una función factorial(), calcule el factorial de un
    número. El programa solicitará un número y calculará el factorial de ese número. El factorial de un
    número, se calcula multiplicando este número por todos los números anteriores a él hasta el 1.
    Esto es:
    6! = 6 * 5 * 4 * 3 * 2 * 1, lo que nos da como resultado 720.
"""

def factorial(a):
    print("!" + str(a), end=": ")
    fac = a
    for i in range(a-1):
        a -= 1
        fac *= a
        print(a, end=" ")
    print(" =", fac)

numero = int(input("Ingrese un numero para calcular su factorial: "))
factorial(numero)


print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")
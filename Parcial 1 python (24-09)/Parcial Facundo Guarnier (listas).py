print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que acepte como entrada desde teclado un número entero mayor
    que cero y dé como salida el resultado de sumar dos a dos los dígitos que aparecen en
    posiciones simétricas respecto al dígito central dentro del número dado como entrada.
    Por ejemplo:
        - Para el número: 2354869
        La salida es: 2 + 9 = 11, 3 + 6= 9, 5 + 8 = 13, 4  (11, 9, 13, 4)
        - Para el número: 6582
        La salida es: 6 + 2 = 8, 5 + 8 = 13

"""

numero = str(input("Ingrese un numero entero mayor a 0 (cero): "))   
correcto = 0

while correcto == 0:
    if (".") in numero:
        numero = str(input("1111111Ingrese un numero entero mayor a 0 (cero): "))
    elif ("-") in numero:
        numero = str(input("2222222Ingrese un numero entero mayor a 0 (cero): "))
    elif (numero == "0"):
        numero = str(input("3333333Ingrese un numero entero mayor a 0 (cero): "))
    else:
        correcto = 1
        

j = (len(str(numero)) - 1)
i = 0
mitad = 0
lista = []

while i < len(str(numero)) / 2:          
    comienzo = int(numero [i])
    i += 1
    final = int(numero [j])
    j -= 1
    lista.append(comienzo + final)

if (len(numero) % 2) != 0: 
    lista[len(lista)-1] = round(((comienzo + final) / 2))

print(lista)

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
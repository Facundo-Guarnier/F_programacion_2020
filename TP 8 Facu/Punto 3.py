print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Calcular el valor total que una persona debe pagar por la compra de llantas en un supermercado que tiene la 
    siguiente promoción: Si la cantidad de llantas compradas es mayor o igual a 4, el precio unitario tiene un descuento 
    del 10%, si las llantas compradas son menores a 4 pero mayores o igual a 2, el precio unitario tiene un descuento 
    del 5%. El programa debe pedir que se ingrese la cantidad de llantas y el precio unitario, luego muestra los resultados. 

"""

llantas = int(input("\nIngrese la cantidad de llantas que comprará: "))
precio = float(input("\nIngrese el valor unitario de la llanta (sin descuentos): "))

if (llantas >= 4):
    total = precio * llantas - precio * llantas * 0.1
    print("El total con descuento incluido es: " + str(total))
elif (llantas >= 2):
    total = precio * llantas - precio * llantas * 0.05
    print("El total con descuento incluido es: " + str(total))
else:
    total = precio * llantas
    print("El total con descuento incluido es: " + str(total))

print("\n+++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++\n")
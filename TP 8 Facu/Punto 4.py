print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o regular, y en función de su 
    respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente 
    además de la mozzarella y el tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la 
    pizza elegida es vegetariana o regular, todos los ingredientes que lleva y el valor final a abonar según los 
    siguientes valores: 

        Vegetariana = 270 (lleva más queso que la regular) 
            Pimiento = 30 
            Tofu = 45 

        Regular = 240
            Pepperoni = 32 jamón = 76 
            Salmón = 85 

"""

tipo = int(input("Seleccione un tipo de pizza: \nVegetariana ($270): 1 \nRegular ($240): 2\nIngrese el valor correspondiente: "))

while not(tipo == 1 or tipo == 2):
    tipo = int(input("El valor ingresado no es valido, intente nuevamente: "))

if (tipo == 1):
    ingrediente = int(input("\nSeleccione un ingrediente para agregar a la pizza: \nPimiento ($30): 1 \nTofu ($45): 2 \nIngrese el valor correspondiente: "))
    while not(ingrediente == 1 or ingrediente == 2):
         ingrediente = int(input("El valor ingresado no es valido, intente nuevamente: "))
    if (ingrediente == 1):
        print("1 Pizza vegetariana con Pimiento: $300")
    else:
        print("1 Pizza vegetariana con Tofu: $315")

else:
    ingrediente = int(input("\nSeleccione un ingrediente para agregar a la pizza: \nPepperoni ($32): 1 \nJamón ($76): 2 \nSalmón ($85): 3 \nIngrese el valor correspondiente: "))
    while not(ingrediente == 1 or ingrediente == 2 or ingrediente == 3):
         ingrediente = int(input("El valor ingresado no es valido, intente nuevamente: "))
    
    if (ingrediente == 1):
        print("1 Pizza Regular con Pepperoni: $272")
    elif (ingrediente == 2):
         print("1 Pizza Regular con Jamón: $316")
    else:
        print("1 Pizza Regular con Salmón: $325")

print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")
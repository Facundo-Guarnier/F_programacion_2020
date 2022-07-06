print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escribe un programa que imprima todos los números del 0 al 6 excepto el 3 y el 6.
    Nota: use la declaración 'continue'.

"""
for numero in range (0, 7):
    if (numero == 3 or numero == 6):
        continue 
    print(numero)
    
print("\n+++++++++++++++++++++++++++++++++++++++ FIN ++++++++++++++++++++++++++++++++++++++++++++++++++\n")
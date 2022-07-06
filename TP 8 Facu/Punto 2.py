print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Lea un valor de temperatura T y un código P que puede ser 1 o 2. Si el código es 1 convierta la temperatura T de 
    grados a Celsius, (C = 5/9 (T-32)). Si el código es 2 convierta la temperatura T de Celsius a Fahrenheit (F = 32 + 9 * T/5). 

"""

t = float(input("Ingrese la temperatura: "))
p = int(input("\nA que tipo de grados decea pasar la temperatura: \nCelsius : 1 \nFahrenheit : 2 \n\nIngrese el numero correspondiente: "))

while not(p == 1 or p == 2):
    p = int(input("Numero no valido intente nuevamente: "))

if (p == 1):
    grados = (5 / 9 * (t -32))
    print("\nGrados Celsius: ", round(grados, 3))
else:
    grados = 32 + (9 * t / 5) 
    print("\nGrados Fahrenheit: ", round(grados, 3))
    
print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
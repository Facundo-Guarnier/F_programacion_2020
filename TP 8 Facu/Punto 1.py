print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en 
    la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden 
    conseguir los empleados pueden ser 0.0, 0.4. o 0.6, pero no valores intermedios entre las cifras mencionadas. 

    A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación:

       Nivel       	Puntuación 
    Inaceptable     	0.0 
     Aceptable        	0.4 
     Meritorio       	0.6 

    La cantidad de dinero conseguida en cada nivel es de $ 2.400 multiplicada por la puntuación del nivel si corresponde 
    a horas normales y de $ 3.000 multiplicada por la puntuación del nivel si corresponde a horas extras. El monto obtenido 
    como premio, debe sumarse al salario básico de $10.000. 

    Escribir un programa que lea la puntuación del empleado, y pida ingresar si trabajó horas normales u horas extras, 
    luego indique por pantalla su nivel de rendimiento, así como la cantidad de dinero total que recibirá. 

"""


print("\nLas posibles puntuaciones pueden ser: \n0.0 : Inaceptable \n0.4 : Aceptable \n0.6 : Meritorio")

nivel = float(input("\nIngrese la puntuación del empleado: "))
while not (nivel == 0.0 or nivel == 0.4 or nivel == 0.6):
    print("\nIngresó un numero no valido, intente nuevamente")
    nivel = float(input("Ingrese la puntuación del empleado (utilice punto en vez de coma): ")) 

print("\nLos posibles tipos de horas son: ")
print("Horas Normales : 1 \nHoras Extras : 2 \n")
hora = int(input("Ingrese el número correspondiente: "))

while not (hora == 1 or hora == 2):
    print("\nNumero no valido, intente nuevamente")
    hora = int(input("Ingrese el número correspondiente: "))

if (hora == 1):
    saldo = 10000 + (2400 * nivel)
else: 
    saldo = 10000 + (3000 * nivel)
if (nivel == 0.0):
    t_nivel = ("Inaceptable")
elif (nivel == 0.4):
    t_nivel = ("Aceptable")
else:
    t_nivel = ("Meritorio")

print("\nEl sueldo total es: $" + str(saldo) + "\nEl nivel de rendimiento es: " + str(t_nivel))

print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
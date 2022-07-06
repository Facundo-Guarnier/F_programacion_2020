print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Escriba un programa que permita crear una tupla con los meses del año, pedirle un
    número al usuario, si el numero esta entre 1 y la longitud máxima de la tupla, mostrar el contenido
    de esa posición sino mostrar un mensaje de error. El programa termina cuando el usuario
    introduce un cero.
"""

t_meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while True:
    mes = int(input("Ingrese un numero de mes: "))
    if mes == 0:
        print("Saliendo del programa...")
        break
    elif mes-1 > len(t_meses):
        print("Error, no se ha encontrado.")
        continue
    print(t_meses[mes-1])


print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
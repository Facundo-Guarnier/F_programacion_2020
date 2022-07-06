print("\n+++++++++++++++++++++++++++++++++++++ INICIO +++++++++++++++++++++++++++++++++++++++++++++++++\n")

"""
    Codifica un programa en python que nos permita guardar los nombres de los alumnos
    de una clase y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas.
    Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los
    valores serán listas con las notas de cada alumno.

    El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo
    sus notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista
    de alumnos y la nota promedio obtenida por cada uno de ellos. Nota: si se introduce el nombre de
    un alumno que ya existe el programa nos dará un error

"""

cantidad = int(input("¿Cuantos alumnos se ingresaran sus notas? "))
l_alumnos = []
l_notas = []
d_alumno_nota = {}
d_alumno_promedio = {}

while len(l_alumnos) < cantidad:
    alumno = str(input("Ingrese el nombre del alumno: "))
    while (alumno in l_alumnos):
        print("NO se puede repetir los nombres")
        alumno = input("Ingrese el nombre del alumno: ")
    l_alumnos.append(alumno)
    while True:
        nota = int(input("Ingrese las notas, con un numero negativo termina: "))
        if nota > 0:
            l_notas.append(nota)
        elif (nota < 0):
            break
    d_alumno_nota[alumno] = l_notas
    d_alumno_promedio[alumno] = (sum(l_notas) / len(l_notas))
    l_notas = []

print("La lista con los alumnos y sus notas es: \n", d_alumno_nota)
print("La lista con los promedios es: \n", d_alumno_promedio)



print("\n++++++++++++++++++++++++++++++++++++++ FIN +++++++++++++++++++++++++++++++++++++++++++++++++++\n")
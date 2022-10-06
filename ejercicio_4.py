"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista,
pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

def nota_asignatura(asignatura, notas):
    asignatura = ["Lengua", "Historia", "Matematicas", "Fisica", "Quimica"]
    notas = []
    for asig in asignatura:
        nota = input("¿Qué nota tienes en " + asig + "?")
        notas.append(nota)
    for i in range(len(asignatura)):
        print("En" + asignatura[i]+ "has sacado "+ notas[i])


asignatura = ["Lengua", "Historia", "Matematicas", "Fisica", "Quimica"]
notas = []
for asig in asignatura:
    nota = input("¿Qué nota tienes en " + asig + "?")
    notas.append(nota)
for i in range(len(asignatura)):
    print("En" + asignatura[i]+ "has sacado "+ notas[i])    
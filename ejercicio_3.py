"""
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
Aclaración: El programa debe imprimir por la consola el mismo texto que el usuario introduce hasta que éste escriba la palabra "salir".
"""
def programa(texto):
    while True:
        texto = input("Ingrese su texto: ")
        if texto == "salir":
            break
        print(texto)

while True:
        texto = input("Ingrese su texto: ")
        if texto == "salir":
            break
        print(texto)

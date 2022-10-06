"""
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre por pantalla el número de teléfono
sin el prefijo y la extensión.
"""
def numero_de_telefono(telefono):
    telefono = input("Ingrese su numero de telefono con el formato +xx-xxxxxxxxx-xx: ")
    print("Su numero de telefnono es: ", telefono[4:-3])
    
telefono = input("Ingrese su numero de telefono con el formato +xx-xxxxxxxxx-xx: ")
print("Su numero de telefnono es: ", telefono[4:-3])

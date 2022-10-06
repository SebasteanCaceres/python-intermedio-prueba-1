"""
Escribir una función que calcule el total de una factura tras aplicarle el IVA.
La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 19%.
"""


def total_de_factura(cantidad, IVA = 19):
    return cantidad + cantidad * IVA / 100


print(total_de_factura(5490, 30))
print(total_de_factura(300))

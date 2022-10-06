"""
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar
segun imagen adjunta
"""
def renta_anual(renta, tipo_impositivo):
    renta = float(input("Ingrese su renta anual: "))
    if renta < 10000:
        tipo_impositivo = 5
    elif renta < 20000:
        tipo_impositivo = 15
    elif renta < 35000:
        tipo_impositivo = 20
    elif renta < 60000:
        tipo_impositivo = 30
    else:
        tipo_impositivo = 45
    print ("debe pagar", renta * tipo_impositivo / 100, "€", sep='' )

renta = float(input("Ingrese su renta anual: "))
if renta < 10000:
    tipo_impositivo = 5
elif renta < 20000:
    tipo_impositivo = 15
elif renta < 35000:
    tipo_impositivo = 20
elif renta < 60000:
    tipo_impositivo = 30
else:
    tipo_impositivo = 45
print ("debe pagar", renta * tipo_impositivo / 100, "€", sep='' )


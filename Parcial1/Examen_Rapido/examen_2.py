# consumo=print("Cantidad de kWh consumidos por el cliente: ")

# basica=consumo * 0.987
# iva=basica * 0.16

# if consumo<=150:
#     print("El precio de la tarifa basica es de: {basica}")

# if consumo>=150:
#     print("El precio por el excedente con tarifa intermedia es de: ")


#     if 1 <= consumo <= 150:
#         costo = consumo * 0.987
#     else:
#         costo = consumo * 1.203


def calcular_costo_consumo(kwh_consumidos):
    tarifa_base = 0.987  
    tarifa_excedente = 1.203  

    if kwh_consumidos <= 150:
        costo_total = kwh_consumidos * tarifa_base
    else:
        kwh_base = 150
        kwh_excedente = kwh_consumidos - kwh_base
        costo_total = kwh_base * tarifa_base + kwh_excedente * tarifa_excedente

    return costo_total

kwh_consumidos_usuario = float(input("Ingresa la cantidad de kWh consumidos: "))
costo_total_usuario = calcular_costo_consumo(kwh_consumidos_usuario)
print(f"El costo total es: ${costo_total_usuario:.2f}")

iva=costo_total_usuario * .16
print(f"El iva que se obtiene es de {iva}")

alumbrado= 12.56

final1= costo_total_usuario + iva + alumbrado
print(f"El costo final es de {final1}")

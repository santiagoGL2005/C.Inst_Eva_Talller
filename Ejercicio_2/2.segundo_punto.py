# Función para definir tarifas por minuto en pesos
tarifas = {"Estados Unidos": 900, "Canada": 800, "Europa": 950, "Resto del mundo": 1.250}

# Función para calcualar el costo de una llamada
def calcular_costo(region, minutos):
    if region in tarifas:
        costo = tarifas [region] * minutos
        return costo
    else:
        return "No se sabe que region"

# Función para uso de las llamadas
region = input("ingrese la region (Estados Unidos, Canada, Europa, Resto del mundo) ")
minutos = int(input("Ingrese cantidad de minutos: "))

costo_total = calcular_costo(region, minutos)
print(f"El costo total de la llamada es: {costo_total} pesos")
"""o	Escriba un programa que lea las cuatro notas (en escala de 1 a 5) de un estudiante y clasifique su rendimiento de acuerdo con el promedio de la siguiente forma:

Entre 4 y 5: Excelente
Entre 3 y 3.99: Bien
Entre 0 y 2.99: Deficiente"""

# Función para leer las cuatro notas
nota_1 = float(input("Ingrese la primera  nota de (1 a 5): "))
nota_2 = float(input("Ingrese la segunda nota de (1 a 5): "))
nota_3 = float(input("Ingrese la tercera nota de (1 a 5): "))
nota_4 = float(input(" Ingrese la cuarta nota de (1 a 5): "))

# Funcion para calcular el promedio
promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Función para clasificar el rendimiento y el promedio
if 4 <= promedio <= 5:
    rendimiento = "Excelente"
elif 3 <= promedio <= 3.99:
    rendimiento = "Bien"
elif 0 <= promedio <=2.99:
    rendimiento = "Deficiente"
else:
    rendimiento = "Las notas deben estar en el rango de 1 a 5"

# Función para mostrar el resultado
print((f"El promedio de notas es: {promedio:.2f}"))
print(f"rendimiento: {rendimiento}")

"""Adicionalmente, el programa debe calcular el costo de la matricula. A los estudiantes que obtienen un rendimiento "Exelente" se les otorga descuento del 20% en la matricula. Los demás estudiantes pagan el 100% del costo. El programa debe solicitar al usurio las cuatro notas del estudiante y el costo total de la matricula. Luego debe mostrar el promedio del estudiante, su clasificación de rendimiento y el monto final a pagar por matricula"""

# Función para calcular el costo de la matricula
def calcular_matricula(costo_base, clasificación):
    if clasificación == "Exelente":
        return costo_base * 0.8 # 20% de descuento
    else:
        return costo_base # 100% del costo

# Función para solicitar las notas y el costo de la matricula
notas = []
for i in range(4):
    nota = float(input(f"Ingrese la nota {i+1} (entre 1 y 5): "))
    notas.append(nota)

costo_base = float(input("Ingrese el costo total de la matricula: "))

# Función para calcular el promedio, clasificanción y costo final

"""o	Escriba un programa que lea las cuatro notas (en escala de 1 a 5) de un estudiante y clasifique su rendimiento de acuerdo con el promedio de la siguiente forma:

Entre 4 y 5: Excelente
Entre 3 y 3.99: Bien
Entre 0 y 2.99: Deficiente"""

# Leer las cuatro notas
nota_1 = float(input("Ingrese la primera  nota de (1 a 5): "))
nota_2 = float(input("Ingrese la segunda nota de (1 a 5): "))
nota_3 = float(input("Ingrese la tercera nota de (1 a 5): "))
nota_4 = float(input(" Ingrese la cuarta nota de (1 a 5): "))

# Calcular el proimedio
promedio = (nota_1 + nota_2 + nota_3 + nota_4) / 4

# Clasificar el rendimiento y el promedio
if 4 <= promedio <= 5:
    rendimiento = "Excelente"
elif 3 <= promedio <= 3.99:
    rendimiento = "Bien"
elif 0 <= promedio <=2.99:
    rendimiento = "Deficiente"
else:
    rendimiento = "Las notas deben estar en el rango de 1 a 5"

# Moatar el resultado
print((f"El promedio de notas es: {promedio:.2f}"))
print(f"rendimiento: {rendimiento}")


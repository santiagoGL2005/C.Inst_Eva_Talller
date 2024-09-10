# Solicitar al usuario que ingrese su nombre
nombre = input("Por favor, ingrese tu nombre: ")

# Saludar al usuario
print(f"Hola, {nombre}! ¡Bienvenido")

#Solicita al usuario que ingrese su peso y altura
peso = float(input("Por favor, ingresa tu peso en kilogramos: "))
altura =  float(input("Por favor, ingrese su altura en metros"))

# Calcular el indice de masa corporal (IMC)
imc = peso / (altura ** 2)

# Mostrar el resultado
print(f"Tu indice de masa corporal (IMC) es: {imc:.2f}")

# Clasificación del IMC
if imc < 18.5:
    print("Clasificación: Peso bajo")
elif 18.5 <= imc < 24.9:
    print("Clasificación: Peso normal")
elif 25 <= imc <29.9:
    print("Clacificación: Sobre peso")
else:
    print("Clasificación: Obesidad")

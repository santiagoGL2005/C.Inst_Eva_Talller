# Función para la primera verificación: verificar si "x" esta entre "y" y "z", y si "w" es par
x, y, z, w = 15, 10, 20, 8
verificación1 = (y < x < z) and (w % 2 == 0)
print(f" 'x' esta entre 'y' y 'z', y 'W' es par: {verificación1}")

# Función para la segunda verificación: comprobar si 'a' es mayor que 'b' o si 'c' es igual 'd', pero las dos
a, b, c, d = 7, 5, 3, 3
verificación2 = (a > b) ^ (c == d)
print(f" 'a' es masyor que 'b' o 'c' es igual a 'd' (pero no las dos): {verificación2}")

# Función para la tercera verificación: si 'x' es negativo, 'y' es positivo, y 'z' es cero
x, y, z = -3, 5, 0
verificación3 = (x < 0) and (y > 0) and (z == 0)
print(f" 'x' es negativo, 'y' es positivo, y 'z' es cero: {verificación3} ")
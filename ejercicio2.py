import math

def area_circulo(radio):
    return math.pi * radio ** 2

def volumen_cilindro(radio, altura):
    return area_circulo(radio) * altura

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calcular y mostrar el área del círculo
area = area_circulo(radio)
print(f"Área del círculo: {area}")

# Solicitar al usuario que ingrese la altura del cilindro
altura = float(input("Ingrese la altura del cilindro: "))

# Calcular y mostrar el volumen del cilindro
volumen = volumen_cilindro(radio, altura)
print(f"Volumen del cilindro: {volumen}")

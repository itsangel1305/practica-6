def decimal_a_binario(decimal):
    return bin(decimal)[2:]

def binario_a_decimal(binario):
    return int(binario, 2)

# Solicitar al usuario que ingrese un número decimal
decimal = int(input("Ingrese un número decimal para convertir a binario: "))

# Convertir decimal a binario y mostrar el resultado
binario = decimal_a_binario(decimal)
print(f"El número decimal {decimal} en binario es: {binario}")

# Solicitar al usuario que ingrese un número binario
binario_input = input("Ingrese un número binario para convertir a decimal: ")

# Convertir binario a decimal y mostrar el resultado
decimal_convertido = binario_a_decimal(binario_input)
print(f"El número binario {binario_input} en decimal es: {decimal_convertido}")


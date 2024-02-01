def calcular_total_factura(cantidad, iva):
    return cantidad + (cantidad * iva / 100)

# Solicitar al usuario que ingrese la cantidad sin IVA
cantidad = float(input("Ingrese la cantidad sin IVA: "))

# Solicitar al usuario que ingrese el porcentaje de IVA
iva = float(input("Ingrese el porcentaje de IVA a aplicar: "))

# Calcular y mostrar el total de la factura
total_factura = calcular_total_factura(cantidad, iva)
print(f"Total de la factura con IVA: {total_factura}")

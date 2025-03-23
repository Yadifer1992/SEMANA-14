def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento sobre un monto total de compra.
    :param monto_total: Monto total de la compra
    :param porcentaje_descuento: Porcentaje de descuento a aplicar (por defecto 10%)
    :return: Monto del descuento calculado
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento

# Mensaje de bienvenida
print("Bienvenido a la Cooperativa COCA LTDA.")

while True:
    try:
        total = float(input("Ingrese el monto total de la compra: "))
        tipo_pago = input("El pago es en efectivo? (si/no): ").strip().lower()
        
        if tipo_pago == "si":
            porcentaje_descuento = 20  # Descuento por pago en efectivo
        else:
            porcentaje_descuento = 10  # Descuento normal
        
        descuento = calcular_descuento(total, porcentaje_descuento)
        total_a_pagar = total - descuento
        
        print(f"Monto total: ${total:.2f}, Descuento: ${descuento:.2f}, Total a pagar: ${total_a_pagar:.2f}")
        
        continuar = input("¿Desea realizar otra compra? (si/no): ").strip().lower()
        if continuar != "si":
            break
    except ValueError:
        print("Por favor, ingrese un monto válido.")

print("Gracias por su compra. ¡Vuelva pronto!")

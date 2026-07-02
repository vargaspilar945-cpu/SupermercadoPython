
pedido_prueba = [
    {"nombre": "Hamburguesa", "precio": 3500, "cantidad": 2},
    {"nombre": "Gaseosa", "precio": 1200, "cantidad": 1},
    {"nombre": "Papas fritas", "precio": 2000, "cantidad": 1}
]


# --- CALCULAR SUBTOTAL ---
def calcular_subtotal(pedido):
    """
    Recorre la lista de productos y devuelve la suma
    de precio x cantidad de cada uno. (acumulador)
    """
    subtotal = 0
    for producto in pedido:
        subtotal = subtotal + (producto["precio"] * producto["cantidad"])
    return subtotal


# --- ELEGIR MEDIO DE PAGO ---
def elegir_medio_pago():
    """
    Muestra las opciones de pago y valida que el usuario
    ingrese una opción correcta. (estructura repetitiva + validación)
    """
    print("\n¿Con qué medio de pago vas a abonar?")
    print("  1. Efectivo  (10% de descuento)")
    print("  2. Débito")
    print("  3. Crédito")

    while True:
        opcion = input("Ingresá una opción (1/2/3): ")
        if opcion == "1":
            return "efectivo"
        elif opcion == "2":
            return "debito"
        elif opcion == "3":
            return "credito"
        else:
            print("⚠️  Opción inválida. Por favor ingresá 1, 2 o 3.")


# --- APLICAR PROMOCIONES ---
def aplicar_promociones(subtotal, medio_pago):
    """
    Aplica descuentos según el medio de pago y el monto total.
    Devuelve el monto de descuento y un mensaje descriptivo.
    (condicionales)
    """
    descuento = 0
    mensaje = "Sin descuento"

    if medio_pago == "efectivo":
        descuento = subtotal * 0.10
        mensaje = "Descuento por pago en efectivo (10%)"
    elif subtotal > 10000:
        descuento = subtotal * 0.05
        mensaje = "Descuento por compra mayor a $10.000 (5%)"

    return descuento, mensaje


# --- MOSTRAR TICKET ---
def mostrar_ticket(pedido, subtotal, descuento, mensaje_descuento, medio_pago):
    """
    Imprime el ticket de compra con todos los detalles.
    (estructura repetitiva + formato de salida)
    """
    print("\n")
    print("=" * 42)
    print("         🧾 TICKET DE COMPRA")
    print("=" * 42)

    for producto in pedido:
        total_linea = producto["precio"] * producto["cantidad"]
        print(f"  {producto['nombre']:<22} ${total_linea:>7}")

    print("-" * 42)
    print(f"  Subtotal:                  ${subtotal:>7}")

    if descuento > 0:
        print(f"  {mensaje_descuento}")
        print(f"  Descuento:                -${descuento:>7.0f}")

    total_final = subtotal - descuento
    print(f"  TOTAL FINAL:               ${total_final:>7.0f}")
    print(f"  Medio de pago:             {medio_pago.upper()}")
    print("=" * 42)
    print("       ¡Gracias por su compra!")
    print("=" * 42)

    return total_final


# --- CERRAR COMPRA ---
def cerrar_compra(pedido):
    """
    Función principal del módulo. Ejecuta todo el flujo
    de compra y devuelve un registro para el módulo 5
    (estadísticas).
    """
    print("\n" + "=" * 42)
    print("   SISTEMA DE PEDIDOS - COMPRA FINAL")
    print("=" * 42)

    # Mostramos resumen del pedido recibido
    print("\nResumen de tu pedido:")
    for producto in pedido:
        print(f"  - {producto['nombre']} x{producto['cantidad']} = ${producto['precio'] * producto['cantidad']}")

    # Ejecutamos las funciones en orden
    subtotal = calcular_subtotal(pedido)
    print(f"\nSubtotal: ${subtotal}")

    medio_pago = elegir_medio_pago()
    descuento, mensaje_descuento = aplicar_promociones(subtotal, medio_pago)
    total_final = mostrar_ticket(pedido, subtotal, descuento, mensaje_descuento, medio_pago)

    # Registro para el módulo 5 (estadísticas)
    registro = {
        "pedido": pedido,
        "subtotal": subtotal,
        "descuento": descuento,
        "total_final": total_final,
        "medio_pago": medio_pago
    }
    return registro


# --- PROGRAMA PRINCIPAL (solo para pruebas) ---
# Este bloque se elimina cuando el grupo conecte todo.
# El módulo 1 va a llamar a cerrar_compra(pedido) directamente.
if __name__ == "__main__":
    registro = cerrar_compra(pedido_prueba)
    print(f"\n✅ Registro generado para estadísticas: {registro}")
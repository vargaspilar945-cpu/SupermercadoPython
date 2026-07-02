
menu = [
    {"codigo": 1, "nombre": "Hamburguesa Clásica",        "categoria": "Comida",          "precio": 3500, "stock": 10},
    {"codigo": 2, "nombre": "Hamburguesa Doble Cheddar",  "categoria": "Comida",          "precio": 4500, "stock": 8},
    {"codigo": 3, "nombre": "Papas Fritas",               "categoria": "Acompañamiento",  "precio": 2000, "stock": 15},
    {"codigo": 4, "nombre": "Empanada de Carne",          "categoria": "Comida",          "precio": 900,  "stock": 20},
    {"codigo": 5, "nombre": "Pizza Muzzarella (porción)", "categoria": "Comida",          "precio": 2500, "stock": 12},
    {"codigo": 6, "nombre": "Gaseosa 500ml",              "categoria": "Bebida",          "precio": 1500, "stock": 25},
    {"codigo": 7, "nombre": "Agua Mineral 500ml",         "categoria": "Bebida",          "precio": 1000, "stock": 25},
    {"codigo": 8, "nombre": "Helado (postre)",            "categoria": "Postre",          "precio": 2200, "stock": 6},
]

def mostrar_carta():
    print("\n" + "=" * 55)
    print(f"{'COD':<4}{'PRODUCTO':<30}{'PRECIO':>10}{'STOCK':>8}")
    print("=" * 55)
    for producto in menu:
        estado_stock = str(producto["stock"]) if producto["stock"] > 0 else "AGOTADO"
        print(f"{producto['codigo']:<4}{producto['nombre']:<30}"
              f"${producto['precio']:>8}{estado_stock:>9}")
    print("=" * 55)

def buscar_producto(codigo):
    for producto in menu:
        if producto["codigo"] == codigo:
            return producto
    return None

def hay_stock_suficiente(producto, cantidad):
    return producto["stock"] >= cantidad

def descontar_stock(producto, cantidad):
    if hay_stock_suficiente(producto, cantidad):
        producto["stock"] -= cantidad
        return True
    return False

def pedir_codigo_valido():
    while True:
        entrada = input("Ingrese el código del producto (0 para cancelar): ")
        try:
            codigo = int(entrada)
        except ValueError:
            print("Error: debe ingresar un número entero.")
            continue
        if codigo == 0:
            return None
        producto = buscar_producto(codigo)
        if producto is None:
            print("Error: no existe un producto con ese código.")
            continue
        if producto["stock"] <= 0:
            print(f"Lo sentimos, '{producto['nombre']}' está agotado.")
            continue
        return producto

def pedir_cantidad_valida(stock_disponible):
    while True:
        entrada = input(f"Ingrese cantidad (stock disponible: {stock_disponible}): ")
        try:
            cantidad = int(entrada)
        except ValueError:
            print("Error: ingrese un número entero válido.")
            continue
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor a 0.")
            continue
        if cantidad > stock_disponible:
            print(f"Error: no hay stock suficiente. Disponible: {stock_disponible}.")
            continue
        return cantidad


carrito = []  # lista de items del pedido actual: {"producto": nombre, "precio": ..., "cantidad": ...}

def agregar_al_carrito():
    mostrar_carta()
    producto = pedir_codigo_valido()
    if producto is None:
        print("Operación cancelada.")
        return
    cantidad = pedir_cantidad_valida(producto["stock"])
    # Buscamos si ya está en el carrito para sumar cantidad
    for item in carrito:
        if item["producto"] == producto["nombre"]:
            item["cantidad"] += cantidad
            descontar_stock(producto, cantidad)
            print(f"✅ Se sumaron {cantidad} unidades de {producto['nombre']} al carrito.")
            return
    # Si no estaba, lo agregamos
    descontar_stock(producto, cantidad)
    carrito.append({
        "producto": producto["nombre"],
        "precio": producto["precio"],
        "cantidad": cantidad
    })
    print(f"✅ {cantidad} x {producto['nombre']} agregado al carrito.")

def ver_carrito():
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return
    print("\n===== CARRITO ACTUAL =====")
    subtotal = 0
    for i, item in enumerate(carrito, start=1):
        total_linea = item["precio"] * item["cantidad"]
        print(f"  {i}. {item['producto']} x{item['cantidad']} = ${total_linea}")
        subtotal += total_linea
    print(f"  Subtotal: ${subtotal}")
    print("=" * 26)

def eliminar_del_carrito():
    if len(carrito) == 0:
        print("\nEl carrito está vacío.")
        return
    ver_carrito()
    try:
        posicion = int(input("Ingrese el número del producto a eliminar: "))
    except ValueError:
        print("Error: debe ingresar un número.")
        return
    if posicion < 1 or posicion > len(carrito):
        print("Error: posición inválida.")
    else:
        # Reponer stock al menu
        item = carrito[posicion - 1]
        producto = buscar_producto_por_nombre(item["producto"])
        if producto:
            producto["stock"] += item["cantidad"]
        eliminado = carrito.pop(posicion - 1)
        print(f"❌ '{eliminado['producto']}' eliminado del carrito.")

def buscar_producto_por_nombre(nombre):
    for p in menu:
        if p["nombre"] == nombre:
            return p
    return None

def calcular_subtotal():
    subtotal = 0
    for item in carrito:
        subtotal += item["precio"] * item["cantidad"]
    return subtotal

def vaciar_carrito():
    carrito.clear()


def elegir_medio_pago():
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
            print("⚠️  Opción inválida. Ingresá 1, 2 o 3.")

def aplicar_promociones(subtotal, medio_pago):
    descuento = 0
    mensaje = "Sin descuento"
    if medio_pago == "efectivo":
        descuento = subtotal * 0.10
        mensaje = "Descuento por pago en efectivo (10%)"
    elif subtotal > 10000:
        descuento = subtotal * 0.05
        mensaje = "Descuento por compra mayor a $10.000 (5%)"
    return descuento, mensaje

def mostrar_ticket(subtotal, descuento, mensaje_descuento, medio_pago):
    print("\n" + "=" * 42)
    print("         🧾 TICKET DE COMPRA")
    print("=" * 42)
    for item in carrito:
        total_linea = item["precio"] * item["cantidad"]
        print(f"  {item['producto']:<22} ${total_linea:>7}")
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

def cerrar_compra(pedidos_del_dia):
    if len(carrito) == 0:
        print("\n⚠️  El carrito está vacío. Agregá productos primero.")
        return

    ver_carrito()
    confirmacion = input("\n¿Confirmar compra? (s/n): ").lower()
    if confirmacion != "s":
        print("Compra cancelada.")
        return

    subtotal = calcular_subtotal()
    medio_pago = elegir_medio_pago()
    descuento, mensaje_descuento = aplicar_promociones(subtotal, medio_pago)
    total_final = mostrar_ticket(subtotal, descuento, mensaje_descuento, medio_pago)

    # Guardar el pedido para estadísticas
    registro = {
        "items": [{"producto": i["producto"], "cantidad": i["cantidad"]} for i in carrito],
        "total": total_final,
        "medio_pago": medio_pago
    }
    pedidos_del_dia.append(registro)

    vaciar_carrito()
    print("\n✅ Pedido registrado correctamente.")


def cantidad_pedidos(pedidos):
    return len(pedidos)

def calcular_total_vendido(pedidos):
    total = 0
    contador = 0
    while contador < len(pedidos):
        total += pedidos[contador]["total"]
        contador += 1
    return total

def comida_mas_vendida(pedidos):
    conteo = {}
    i = 0
    while i < len(pedidos):
        items = pedidos[i]["items"]
        j = 0
        while j < len(items):
            producto = items[j]["producto"]
            cantidad = items[j]["cantidad"]
            if producto in conteo:
                conteo[producto] += cantidad
            else:
                conteo[producto] = cantidad
            j += 1
        i += 1
    if len(conteo) == 0:
        return None, 0
    producto_top = None
    cantidad_top = 0
    for producto, cantidad in conteo.items():
        if cantidad > cantidad_top:
            cantidad_top = cantidad
            producto_top = producto
    return producto_top, cantidad_top

def mostrar_estadisticas(pedidos):
    print("\n=== ESTADÍSTICAS DEL DÍA ===")
    if not pedidos:
        print("Todavía no se registraron pedidos.")
        return
    print(f"  Cantidad de pedidos: {cantidad_pedidos(pedidos)}")
    print(f"  Total vendido:       ${calcular_total_vendido(pedidos):.0f}")
    producto, veces = comida_mas_vendida(pedidos)
    if producto is not None:
        print(f"  Producto más vendido: {producto} ({veces} unidades)")
    else:
        print("  No hay datos de productos vendidos.")

def menu_estadisticas(pedidos):
    opcion = -1
    while opcion != 0:
        print("\n--- MENÚ ESTADÍSTICAS ---")
        print("1. Ver estadísticas generales")
        print("2. Ver cantidad de pedidos")
        print("3. Ver total vendido")
        print("4. Ver producto más vendido")
        print("0. Volver al menú principal")
        entrada = input("Elegí una opción: ")
        if not entrada.isdigit():
            print("Error: ingresá un número válido.")
            continue
        opcion = int(entrada)
        if opcion == 1:
            mostrar_estadisticas(pedidos)
        elif opcion == 2:
            print(f"  Cantidad de pedidos: {cantidad_pedidos(pedidos)}")
        elif opcion == 3:
            print(f"  Total vendido: ${calcular_total_vendido(pedidos):.0f}")
        elif opcion == 4:
            producto, veces = comida_mas_vendida(pedidos)
            if producto is None:
                print("  No hay pedidos registrados todavía.")
            else:
                print(f"  Producto más vendido: {producto} ({veces} unidades)")
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida, probá de nuevo.")


def pausar():
    input("\n  Presione Enter para continuar...")

def mostrar_menu_principal():
    print("\n" + "=" * 45)
    print("     SISTEMA DE PEDIDOS DE COMIDA")
    print("=" * 45)
    print("  1. Ver carta / menú")
    print("  2. Agregar producto al carrito")
    print("  3. Ver carrito")
    print("  4. Eliminar producto del carrito")
    print("  5. Confirmar compra / Medios de pago")
    print("  6. Ver pedidos del día")
    print("  7. Estadísticas de ventas")
    print("  8. Salir")
    print("=" * 45)

def validar_opcion(minimo, maximo):
    while True:
        try:
            opcion = int(input("  Ingrese una opción: "))
            if minimo <= opcion <= maximo:
                return opcion
            else:
                print(f"Opción inválida. Ingrese un número entre {minimo} y {maximo}.")
        except ValueError:
            print("Debe ingresar un número entero.")

def ver_pedidos_del_dia(pedidos):
    print("\n=== PEDIDOS DEL DÍA ===")
    if not pedidos:
        print("  No se registraron pedidos todavía.")
        return
    for i, pedido in enumerate(pedidos, start=1):
        print(f"\n  Pedido #{i} - Total: ${pedido['total']:.0f} - Pago: {pedido['medio_pago'].upper()}")
        for item in pedido["items"]:
            print(f"    - {item['producto']} x{item['cantidad']}")

def main():
    pedidos_del_dia = []
    print("\n  ¡Bienvenido al Sistema de Pedidos de Comida!")

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion = validar_opcion(1, 8)

        if opcion == 1:
            mostrar_carta()
            pausar()
        elif opcion == 2:
            agregar_al_carrito()
            pausar()
        elif opcion == 3:
            ver_carrito()
            pausar()
        elif opcion == 4:
            eliminar_del_carrito()
            pausar()
        elif opcion == 5:
            cerrar_compra(pedidos_del_dia)
            pausar()
        elif opcion == 6:
            ver_pedidos_del_dia(pedidos_del_dia)
            pausar()
        elif opcion == 7:
            menu_estadisticas(pedidos_del_dia)
        elif opcion == 8:
            print("\n  ¡Hasta luego! Cerrando el sistema...\n")
            continuar = False

if __name__ == "__main__":
    main()

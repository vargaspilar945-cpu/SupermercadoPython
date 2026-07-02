menu = [
    {"codigo": 1, "nombre": "Hamburguesa Clásica", "categoria": "Comida", "precio": 3500, "stock": 10},
    {"codigo": 2, "nombre": "Hamburguesa Doble Cheddar", "categoria": "Comida", "precio": 4500, "stock": 8},
    {"codigo": 3, "nombre": "Papas Fritas", "categoria": "Acompañamiento", "precio": 2000, "stock": 15},
    {"codigo": 4, "nombre": "Empanada de Carne", "categoria": "Comida", "precio": 900, "stock": 20},
    {"codigo": 5, "nombre": "Pizza Muzzarella (porción)", "categoria": "Comida", "precio": 2500, "stock": 12},
    {"codigo": 6, "nombre": "Gaseosa 500ml", "categoria": "Bebida", "precio": 1500, "stock": 25},
    {"codigo": 7, "nombre": "Agua Mineral 500ml", "categoria": "Bebida", "precio": 1000, "stock": 25},
    {"codigo": 8, "nombre": "Helado (postre)", "categoria": "Postre", "precio": 2200, "stock": 6},
]

def mostrar_menu(lista_productos):
    """
    Recorre la lista de productos (for) y la imprime ordenada por
    categoría, mostrando código, nombre, precio y stock disponible.
    """
    print("\n" + "=" * 55)
    print(f"{'COD':<4}{'PRODUCTO':<30}{'PRECIO':>10}{'STOCK':>8}")
    print("=" * 55)

    for producto in lista_productos:
        # Si no queda stock, lo aclaramos para que el usuario no lo pida
        estado_stock = str(producto["stock"]) if producto["stock"] > 0 else "AGOTADO"
        print(f"{producto['codigo']:<4}{producto['nombre']:<30}"
              f"${producto['precio']:>8}{estado_stock:>9}")

    print("=" * 55)


def mostrar_menu_por_categoria(lista_productos, categoria):
    """
    Variante de mostrar_menu que filtra por categoría
    (ej: 'Comida', 'Bebida', 'Postre', 'Acompañamiento').
    Útil si el equipo quiere armar un sub-menú por tipo de producto.
    """
    encontrados = False
    print(f"\n--- Categoría: {categoria} ---")
    for producto in lista_productos:
        if producto["categoria"].lower() == categoria.lower():
            print(f"{producto['codigo']} - {producto['nombre']} - ${producto['precio']}")
            encontrados = True

    if not encontrados:
        print("No hay productos en esa categoría.")

def buscar_producto(lista_productos, codigo):
    """
    Recibe un código de producto y devuelve el diccionario del
    producto si existe, o None si no se encontró.
    """
    for producto in lista_productos:
        if producto["codigo"] == codigo:
            return producto
    return None  # no se encontró

def hay_stock_suficiente(producto, cantidad):
    """Valida si hay stock suficiente para la cantidad pedida."""
    return producto["stock"] >= cantidad


def descontar_stock(producto, cantidad):
    """
    Descuenta del stock la cantidad indicada.
    Devuelve True si pudo descontar, False si no había stock suficiente.
    Esta función es la que usaría el módulo de "armado de pedidos"
    de mis compañeros/as para confirmar una compra.
    """
    if hay_stock_suficiente(producto, cantidad):
        producto["stock"] -= cantidad
        return True
    return False


def agregar_stock(lista_productos, codigo, cantidad):
    """
    Permite reponer stock de un producto (función administrativa,
    por si el local repone mercadería durante el día).
    """
    producto = buscar_producto(lista_productos, codigo)
    if producto is None:
        print("Error: no existe un producto con ese código.")
        return False
    if cantidad <= 0:
        print("Error: la cantidad a agregar debe ser mayor a 0.")
        return False
    producto["stock"] += cantidad
    print(f"Stock actualizado: {producto['nombre']} ahora tiene {producto['stock']} unidades.")
    return True

def pedir_codigo_valido(lista_productos):
    """
    Usa un while True para insistir hasta que el usuario ingrese
    un código válido (numérico y existente en el menú).
    Maneja el error de tipo (ValueError) si ingresan texto.
    """
    intentos_invalidos = 0  # contador de errores, por si lo quieren mostrar

    while True:
        entrada = input("Ingrese el código del producto (0 para cancelar): ")
        try:
            codigo = int(entrada)
        except ValueError:
            intentos_invalidos += 1
            print("Error: debe ingresar un número entero. Intente nuevamente.")
            continue

        if codigo == 0:
            return None  # el usuario canceló

        producto = buscar_producto(lista_productos, codigo)
        if producto is None:
            intentos_invalidos += 1
            print("Error: no existe un producto con ese código.")
            continue

        if producto["stock"] <= 0:
            print(f"Lo sentimos, '{producto['nombre']}' está agotado.")
            continue

        return producto  # código válido y con stock


def pedir_cantidad_valida(stock_disponible):
    """
    Pide una cantidad y valida que sea un entero positivo y que no
    supere el stock disponible.
    """
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

def demo_menu():
    total_unidades_vendidas = 0  # acumulador
    pedidos_realizados = 0       # contador

    while True:
        print("\n----- LOCAL DE COMIDAS -----")
        print("1) Ver menú completo")
        print("2) Ver menú por categoría")
        print("3) Simular un pedido (descuenta stock)")
        print("4) Reponer stock de un producto")
        print("5) Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_menu(menu)

        elif opcion == "2":
            categoria = input("Ingrese categoría (Comida/Bebida/Postre/Acompañamiento): ")
            mostrar_menu_por_categoria(menu, categoria)

        elif opcion == "3":
            mostrar_menu(menu)
            producto = pedir_codigo_valido(menu)
            if producto is None:
                print("Pedido cancelado.")
                continue
            cantidad = pedir_cantidad_valida(producto["stock"])
            if descontar_stock(producto, cantidad):
                subtotal = producto["precio"] * cantidad
                total_unidades_vendidas += cantidad
                pedidos_realizados += 1
                print(f"OK: {cantidad} x {producto['nombre']} = ${subtotal}")
            else:
                print("Error inesperado al descontar stock.")

        elif opcion == "4":
            try:
                codigo = int(input("Código del producto a reponer: "))
                cantidad = int(input("Cantidad a agregar: "))
                agregar_stock(menu, codigo, cantidad)
            except ValueError:
                print("Error: ingrese valores numéricos.")

        elif opcion == "5":
            print(f"\nResumen de la sesión:")
            print(f"  - Pedidos realizados: {pedidos_realizados}")
            print(f"  - Unidades vendidas: {total_unidades_vendidas}")
            print("Saliendo del módulo de menú. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Elija una opción entre 1 y 5.")

if __name__ == "__main__":
    demo_menu()

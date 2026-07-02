Módulo de ESTADÍSTICAS - Sistema de Pedidos de Comida
--------------------------------------------------------
Responsable: Brisa Alanis Rodriguez

# ---------- FUNCIONES DE CÁLCULO ----------
 
def cantidad_pedidos(pedidos):
    """Devuelve cuántos pedidos se registraron."""
    return len(pedidos)

def calcular_total_vendido(pedidos):
    """Suma el total de todos los pedidos usando un acumulador y un while."""
    total = 0
    contador = 0
    while contador < len(pedidos):
        total += pedidos[contador]["total"]
        contador += 1
    return total

def comida_mas_vendida(pedidos):
    """
    Recorre todos los pedidos y cuenta cuántas unidades se vendieron
    de cada producto. Devuelve una tupla (producto, cantidad).
    Si no hay pedidos, devuelve (None, 0).
    """
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
 
# ---------- FUNCIONES DE PRESENTACIÓN ----------
 
def mostrar_estadisticas(pedidos):
    """Imprime en consola un resumen con todas las estadísticas."""
    print("\n=== ESTADÍSTICAS DEL DÍA ===")
 
    if not pedidos:
        print("Todavía no se registraron pedidos.")
        return
 
    total_pedidos = cantidad_pedidos(pedidos)
    total_vendido = calcular_total_vendido(pedidos)
    producto, veces = comida_mas_vendida(pedidos)
 
    print(f"Cantidad de pedidos: {total_pedidos}")
    print(f"Total vendido: ${total_vendido}")
 
    if producto is not None:
        print(f"Producto más vendido: {producto} ({veces} unidades)")
    else:
        print("No hay datos de productos vendidos.")
 
def menu_estadisticas(pedidos):
    """
    Menú interactivo del módulo de estadísticas.
    Se puede llamar desde el menú principal del sistema.
    """
    opcion = -1
 
    while opcion != 0:
        print("\n--- MENÚ ESTADÍSTICAS ---")
        print("1. Ver estadísticas generales")
        print("2. Ver cantidad de pedidos")
        print("3. Ver total vendido")
        print("4. Ver producto más vendido")
        print("0. Volver al menú principal")
 
        entrada = input("Elegí una opción: ")
 
        # Validación: que lo ingresado sea un número
        if not entrada.isdigit():
            print("Error: ingresá un número válido.")
            continue
 
        opcion = int(entrada)
 
        if opcion == 1:
            mostrar_estadisticas(pedidos)
        elif opcion == 2:
            print(f"Cantidad de pedidos: {cantidad_pedidos(pedidos)}")
        elif opcion == 3:
            print(f"Total vendido: ${calcular_total_vendido(pedidos)}")
        elif opcion == 4:
            producto, veces = comida_mas_vendida(pedidos)
            if producto is None:
                print("No hay pedidos registrados todavía.")
            else:
                print(f"Producto más vendido: {producto} ({veces} unidades)")
        elif opcion == 0:
            print("Volviendo al menú principal...")
        else:
            print("Opción inválida, probá de nuevo.")
 


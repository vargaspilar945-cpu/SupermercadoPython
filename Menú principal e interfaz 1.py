# ============================================================
#   SISTEMA DE PEDIDOS DE COMIDA
#   Trabajo Final Integrador - Escenario 5
# ============================================================

def mostrar_menu_principal():
    print("\n" + "=" * 45)
    print("SISTEMA DE PEDIDOS DE COMIDA")
    print("=" * 45)
    print("  1. Ver carta / menú")
    print("  2. Nuevo pedido")
    print("  3. Ver pedidos del día")
    print("  4. Medios de pago")
    print("  5. Estadísticas de ventas")
    print("  6. Salir")
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


def opcion_ver_carta():
    print("\n---VER CARTA ---")
    print("  (Función en desarrollo)")


def opcion_nuevo_pedido():
    print("\n---NUEVO PEDIDO ---")
    print("  (Función en desarrollo)")


def opcion_ver_pedidos():
    print("\n--- PEDIDOS DEL DÍA ---")
    print("  (Función en desarrollo)")


def opcion_medios_pago():
    print("\n---MEDIOS DE PAGO ---")
    print("  (Función en desarrollo)")


def opcion_estadisticas():
    print("\n---ESTADÍSTICAS DE VENTAS ---")
    print("  (Función en desarrollo)")


def main():
    print("\n  Bienvenido al Sistema de Pedidos de Comida")

    continuar = True
    while continuar:
        mostrar_menu_principal()
        opcion = validar_opcion(1, 6)

        if opcion == 1:
            opcion_ver_carta()
        elif opcion == 2:
            opcion_nuevo_pedido()
        elif opcion == 3:
            opcion_ver_pedidos()
        elif opcion == 4:
            opcion_medios_pago()
        elif opcion == 5:
            opcion_estadisticas()
        elif opcion == 6:
            print("\n ¡Hasta luego! Cerrando el sistema...\n")
            continuar = False

if __name__ == "__main__":
    main()
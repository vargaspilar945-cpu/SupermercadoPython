productos = [
    {"id": 1, "nombre": "Hamburguesa", "categoria": "Comida", "precio": 4500},
    {"id": 2, "nombre": "Pizza muzzarella", "categoria": "Comida", "precio": 7000},
    {"id": 3, "nombre": "Papas fritas", "categoria": "Acompañamiento", "precio": 3000},
    {"id": 4, "nombre": "Gaseosa", "categoria": "Bebida", "precio": 1800},
    {"id": 5, "nombre": "Helado", "categoria": "Postre", "precio": 2500}
]

carrito = []  


def mostrar_productos():# funcion paa mostrar productos
    print("\n===== MENÚ DE PRODUCTOS =====") #titulo

    for producto in productos: # iteramos los productos disponibles
        print(f"{producto['id']}. {producto['nombre']} - {producto['categoria']} - ${producto['precio']}") 
        #mostramos producto

def buscar_producto_por_id(id_producto): #funcion para buscar producto por id
    for producto in productos:  #buscamos en la lista de productos 
        if producto["id"] == id_producto:  # se valida si el id de producto es igual al id del parametro
            return producto   #si el id coincide me va a retornar el producto 

    return None  #si no coincide el id me va a retornar vacio
           #el return siempre va a indicar el final de una funcion
     
def agregar_producto_al_carrito():   #funcion para agregar producto al carrito
    mostrar_productos()        #si el producto existe se va a agregar al carrito
    #si retorna none no se va a agregar nada y va a dar error
    try:    #metodo para capturar errores
        id_producto = int(input("\nIngrese el ID del producto que desea agregar: ")) #aseguramos que el id sea numerico
    except ValueError: #capturamos el error para mostrar
        print("Error: debe ingresar un número.")
        return #la funcion se cierra

    producto = buscar_producto_por_id(id_producto)

    if producto is None:
        print("Error: no existe un producto con ese ID.")
    else:
        carrito.append(producto)  # .append metodo para agregar UN elemento al carrito
        print(f"Producto agregado al carrito: {producto['nombre']}") #mostramos el nombre del producto


def ver_carrito(): 
    if len(carrito) == 0:  #si la longitud del carrito es 0 (vacio)
        print("\nEl carrito está vacío.")
        return

    print("\n===== CARRITO =====")

    subtotal = 0

    for i, producto in enumerate(carrito, start=1): #usamos enumerate para manejar el iidice
        print(f"{i}. {producto['nombre']} - ${producto['precio']}")
        subtotal= subtotal + producto["precio"] #se puede abrebiar subtotal += precio
             
    print(f"\nSubtotal: ${subtotal}")  #termina el bucle y nos da el subtotal de los precios acumulados


def eliminar_producto_del_carrito():
    if len(carrito) == 0:
        print("\nNo se puede eliminar porque el carrito está vacío.")
        return

    ver_carrito()  #todos los productos

    try:
        posicion = int(input("\nIngrese el número del producto que desea eliminar: "))
    except ValueError:
        print("Error: debe ingresar un número.")
        return

    if posicion < 1 or posicion > len(carrito):  
        print("Error: posición inválida.")
    else:
        producto_eliminado = carrito.pop(posicion - 1) # guardamos lo que eliminamos con pop
        print(f"Producto eliminado: {producto_eliminado['nombre']}") #mostramos lo que eliminamos


def calcular_subtotal():
    subtotal = 0

    for producto in carrito:
        subtotal += producto["precio"]  #subtotal=subtotal+precio de todos los productos del carrito

    return subtotal  


def mostrar_menu():
    print("\n===== SISTEMA DE PEDIDOS =====")
    print("1. Ver productos")
    print("2. Agregar producto al carrito")
    print("3. Ver carrito")
    print("4. Eliminar producto del carrito")
    print("5. Calcular subtotal")
    print("0. Salir")


def main():
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            agregar_producto_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            eliminar_producto_del_carrito()
        elif opcion == "5":
            subtotal = calcular_subtotal()
            print(f"\nEl subtotal del carrito es: ${subtotal}")
        elif opcion == "0":
            print("Saliendo del sistema...")
        else:
            print("Opción inválida. Intente nuevamente.")

main()
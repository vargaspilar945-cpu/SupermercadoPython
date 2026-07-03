# Sistema de Pedidos de Comida: Caja Express

Trabajo Final Integrador - Python - AED

## Integrantes del grupo

- Abril Nahir LORINCZ
- Larisa Selene OCAMPO
- Brisa Alanis RODRIGUEZ
- Gisela Mabel SOLOAGA
- Pilar Agostina VARGAS

## Comisión

Comisión 3. Grupo Nro 24.

## Descripción general del sistema

El sistema simula la gestión de pedidos de un local gastronómico. Permite:

- Seleccionar productos y armar pedidos (carrito de compra).
- Calcular importes, aplicar promociones y/o descuentos según el medio de pago.
- Elegir medio de pago (efectivo, débito o crédito).
- Registrar los pedidos realizados durante el día y consultarlos.
- Consultar estadísticas de ventas: total vendido, comida más vendida y
  cantidad de pedidos realizados.

Todo el sistema se ejecuta por consola, mediante un menú principal con
8 opciones.

## Estructura del repositorio

| Archivo | Descripción |
|---|---|
| `Caja-Express_Código_Completo.py` | **Archivo final, listo para ejecutar.** Contiene todo el sistema integrado (menú, carrito, pagos y estadísticas). |
| `carrito.py` | Módulo individual del carrito de compra (desarrollo por separado). |
| `compra_final.py` | Módulo individual de cierre de compra y medios de pago (desarrollo por separado). |
| `menu_comidas (2).py` | Módulo individual del menú de productos (desarrollo por separado). |
| `5.estadisticas.py` | Módulo individual de estadísticas (desarrollo por separado). |
| `README.md` | Este archivo. |

> Los archivos individuales (`carrito.py`, `compra_final.py`, `menu_comidas (2).py`,
> `5.estadisticas.py`) corresponden al desarrollo de cada módulo por separado
> durante el proceso de trabajo del equipo, y se dejan en el repositorio como
> evidencia de ese proceso. **No se ejecutan de forma independiente**, ya que
> dependen de datos y funciones definidos en el archivo principal.
> Para probar el sistema completo hay que ejecutar únicamente
> `Caja-Express_Código_Completo.py`.

## Instrucciones de ejecución

**Requisito previo:** tener instalado Python 3.10 o superior.

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/vargaspilar945-cpu/Caja-Express.git
   ```

2. Ubicarse en la carpeta del proyecto:
   ```bash
   cd Caja-Express
   ```

3. Ejecutar el archivo principal (recordar las comillas, porque el nombre
   tiene tilde y guiones):
   ```bash
   python "Caja-Express_Código_Completo.py"
   ```
   Si en tu sistema el comando `python` no funciona, probá con `python3`:
   ```bash
   python3 "Caja-Express_Código_Completo.py"
   ```

4. Se va a mostrar el menú principal por consola:
   ```
   1. Ver carta / menú
   2. Agregar producto al carrito
   3. Ver carrito
   4. Eliminar producto del carrito
   5. Confirmar compra / Medios de pago
   6. Ver pedidos del día
   7. Estadísticas de ventas
   8. Salir
   ```
   Ingresá el número de la opción deseada y seguí las indicaciones en pantalla.

5. Para cerrar el sistema, elegí la opción **8**.

## Nota

El sistema fue desarrollado de forma colaborativa, utilizando commits
periódicos para reflejar el avance de cada módulo. Se utilizaron estructuras
condicionales, estructuras repetitivas, funciones, validaciones de datos,
acumuladores/contadores y manejo básico de errores.

## Uso de Inteligencia Artificial

Durante el desarrollo de este proyecto utilizamos Claude (Anthropic) como
herramienta de apoyo. La IA fue utilizada para:

- Proponer la estructura inicial del código de cada módulo.
- Resolver dudas sobre sintaxis de Python.
- Analizar y corregir errores durante el desarrollo.
- Unificar los módulos desarrollados por cada integrante en un único
  archivo funcional (`Caja-Express_Código_Completo.py`).
- Asistir en la depuración del sistema.

Todas las integrantes del grupo revisamos, comprendemos y podemos explicar
el código generado. Las soluciones propuestas por la IA fueron analizadas,
adaptadas y validadas por el equipo antes de incorporarlas al proyecto.

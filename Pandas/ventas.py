# Supongamos que tenemos un archivo CSV ("ventas.csv") con información de ventas de "Relojes" que incluye columnas como "Producto", "Cantidad Vendida", "Precio Unitario", y "Fecha".

import pandas as pd

# Función para cargar los datos desde un archivo CSV
def cargar_datos(archivo):
    try:
        datos = pd.read_csv(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo {archivo} no se encontró.")
        return None

# Función para mostrar las estadísticas de ventas
def estadisticas_ventas(datos):
    if datos is not None:
        print("Estadísticas de Ventas:")
        print("-----------------------")
        print(f"Total de Unidades Vendidas: {datos['Unidades Vendidas'].sum():,.2f} Unidades vendidas")
        print(f"Promedio de precio unitario: {datos['Precio Unitario'].mean():,.2f}$")
        print(f"Producto más vendido: {datos['Producto'].mode().values[0]}")
        print(f"Fecha de la venta más reciente: {datos['Fecha'].max()}")
        print("-----------------------")
    else:
        print("No hay datos para mostrar estadísticas.")

# Función para agregar una nueva venta
def agregar_venta(datos, producto, unidades, precio_unitario, fecha):
    nueva_venta = pd.DataFrame({
        'Producto': [producto],
        'Unidades Vendidas': [unidades],
        'Precio Unitario': [precio_unitario],
        'Fecha': [fecha]
    })

    datos = pd.concat([datos, nueva_venta], ignore_index=True)
    return datos

# Función principal
def main():
    archivo = input("Ingrese el nombre del archivo CSV (o presione Enter para usar 'ventas.csv'): ")
    
    # Si no se proporciona un nombre de archivo, se utiliza 'ventas.csv' por defecto
    if not archivo:
        archivo = 'ventas.csv'
    
    datos = cargar_datos(archivo)

    if datos is None:
        # Si no se pueden cargar los datos, se crea un DataFrame vacío
        datos = pd.DataFrame(columns=['Producto', 'Unidades Vendidas', 'Precio Unitario', 'Fecha'])

    while True:
        print("\n¡Bienvenido a la Aplicación de Ventas!")
        print("1. Mostrar Estadísticas de Ventas")
        print("2. Agregar Nueva Venta")
        print("3. Salir")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == '1':
            estadisticas_ventas(datos)
        elif opcion == '2':
            producto = input("Ingrese el nombre del producto: ")
            unidades = int(input("Ingrese las unidades vendida: "))
            precio_unitario = float(input("Ingrese el precio unitario: "))
            fecha = input("Ingrese la fecha de la venta (YYYY-MM-DD): ")

            datos = agregar_venta(datos, producto, unidades, precio_unitario, fecha)
            print("¡Venta agregada exitosamente!")
        elif opcion == '3':
            print("Gracias por usar la aplicación. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, o 3.")

        # Guardar los datos actualizados en el archivo CSV
        datos.to_csv(archivo, index=False)

if __name__ == "__main__":
    main()

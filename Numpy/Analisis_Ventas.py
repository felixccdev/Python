import numpy as np
import calendar
import locale
from datetime import datetime, timedelta

# Configurar la configuración regional en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Generar datos aleatorios de ventas para 12 meses y 10 productos (relojes)
np.random.seed(42)
productos_relojes = ['Reloj A', 'Reloj B', 'Reloj C', 'Reloj D', 'Reloj E', 'Reloj F', 'Reloj G', 'Reloj H', 'Reloj I', 'Reloj J']
ventas_mensuales = np.random.randint(500, 1000, (len(productos_relojes), 12))
fechas_de_compra = [datetime(2023, i + 1, np.random.randint(1, 28)) for i in range(12)]

def analizar_ventas(datos_ventas, fechas, productos):
    total_ventas = np.sum(datos_ventas)
    ventas_por_mes = np.sum(datos_ventas, axis=0)
    valor_ticket_medio = total_ventas / datos_ventas.size

    # Obtener los nombres de los meses en español
    nombres_meses = [calendar.month_name[i].capitalize() for i in range(1, 13)]

    # Encontrar los tres meses con mayores ventas totales
    meses_con_mayores_ventas = [nombres_meses[i] for i in np.argsort(ventas_por_mes)[::-1][:3]]

    # Asociar los nombres de los meses a los resultados
    meses_por_encima_nombres = [(nombres_meses[i], productos[j]) for j, i in np.argwhere(datos_ventas > valor_ticket_medio)]

    # Encontrar los tres productos más vendidos
    productos_mas_vendidos = [productos[i] for i in np.argsort(np.sum(datos_ventas, axis=1))[::-1][:3]]

    # Calcular el total vendido de cada reloj
    total_por_reloj = np.sum(datos_ventas, axis=1)
    ventas_por_reloj = dict(zip(productos, total_por_reloj))

    return total_ventas, ventas_por_mes, meses_por_encima_nombres, valor_ticket_medio, productos_mas_vendidos, meses_con_mayores_ventas, ventas_por_reloj

# Analizar las ventas
total_ventas, ventas_por_mes, meses_por_encima, valor_ticket_medio, productos_mas_vendidos, meses_con_mayores_ventas, ventas_por_reloj = analizar_ventas(ventas_mensuales, fechas_de_compra, productos_relojes)

# Muestra los resultados
print(f"Datos de ventas mensuales:\n{ventas_mensuales}")
print(f"Total de ventas: {total_ventas}")
print(f"Ventas por mes: {ventas_por_mes}")
print(f"Meses con mayores ventas totales: {', '.join(meses_con_mayores_ventas)}")
print(f"Valor del ticket medio: {valor_ticket_medio:.2f}")
print(f"Productos más vendidos: {', '.join(productos_mas_vendidos)}")
print("Total vendido por reloj:")
for reloj, total in ventas_por_reloj.items():
    print(f"{reloj}: {total}")

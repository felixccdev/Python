# Dates (Fechas)

from datetime import datetime

now = datetime.now() #Creamos la variable now

timestamp = now.timestamp() #Es un número que representa una fecha exacta en un único número
print(now.timestamp())

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(now)

# Quiero crear una fecha que represente en comienzo del año
year_2023 = datetime(2023, 1, 1) # Mínimo hay que meter año, mes y día
print_date(year_2023)

from datetime import time

current_time = time()

print(current_time.hour)
print(current_time.min)
print(current_time.minute)
print(current_time.second)

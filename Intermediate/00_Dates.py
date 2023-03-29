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

current_time = time(21, 6, 0) # Hora 21:06:00

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() # Imprime la fecha de hoy

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 11, 6) # Día 6 de Nov. del 2022

print(current_date.year)
print(current_date.month)
print(current_date.day)

#Modificamos una fecha que tenemos anteriormente, en este caso sumamos 1 al mes que era Nov. y ahora es Dic.
current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

# Operamos con fechas

#Resta la fecha year_2023 que era 1 Enero menos la fecha actual
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)


# Timedelta sirve para operar y trabajar con diferencias de fechas
from datetime import timedelta

# Vamos operar dos fechas que hemos introducido (start y end)
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)
print(end_timedelta - start_timedelta) # Aquí las restamos
print(end_timedelta + start_timedelta) # Aquí las sumamos
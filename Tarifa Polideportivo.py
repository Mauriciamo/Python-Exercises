'''Partiendo de la tarifa anual (que puede cambiar), nos piden que debemos calcular el 
precio de la tarifa de nuestro polideportivo, sabiendo las siguientes condiciones:

Criterio 1: Si es mayor de edad y está trabajando -> Paga el 100%
Criterio 2: Si es menor de edad y está trabajando -> Paga el 95%
Criterio 3: Si es mayor de edad y no está trabajando -> Paga el 75%
Criterio 4: Si es menor de edad y no está trabajando -> Paga el 50%'''

x = int(input('Introduce la tarifa polideportivo:'))

def Mayor_Work(x):
    return x * 1

def Menor_Work(x):
    return 0.95 * x

def Mayor_No_Work(x):
    return 0.75 * x

def Menor_No_Work(x):
    return 0.5 * x

print('Si es mayor y trabaja: {}'.format(Mayor_Work(x)))
print('Si es menor y trabaja: {}'.format(Menor_Work(x)))
print('Si es mayor y no trabaja: {}'.format(Mayor_No_Work(x)))
print('Si es menor y no trabaja: {}'.format(Menor_No_Work(x)))




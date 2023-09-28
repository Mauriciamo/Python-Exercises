'''Juego de adivinanza: En este juego, el usuario tiene que adivinar un número aleatorio generado 
por el programa en un rango determinado. El programa le da al usuario pistas sobre si el número 
ingresado es demasiado alto o demasiado bajo en relación al número generado. 
El juego continúa hasta que el usuario adivina el número correcto. 
Para este ejercicio, necesitarás usar bucles while y condicionales if-else para 
comprobar si la respuesta del usuario es correcta y dar pistas en consecuencia.'''

import random

numero = random.randint(1,100)
intentos = 0 

while True :
  pregunta = int(input("Dime un numero: "))
  intentos +=1

  if pregunta == numero:
    print("Has acertado!")
    break
  
  elif pregunta < numero:
    print("Te has quedado corto")
  
  else:
    print("Te has pasado")


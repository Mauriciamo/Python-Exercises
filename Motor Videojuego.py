'''Haz un motor de videojuegos para dos personajes (A y B). Funciona de la siguiente manera:

Empieza el combate y se decide aleatoriamente quien empieza.
Si ataca A restará su ataqueA a defensaB.
Cambio de turno. Le toca a B. Realiza el ataque.
Así hasta que alguno sea derrotado.'''

import random

Personajes = ['A' , 'B']

Primer_Personaje = random.choice(Personajes)
Segundo_Personaje = random.choice(Personajes)

Ataque_A = 4
Defensa_A = 4

Ataque_B = 4
Defensa_B = 4

print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A , Defensa_A))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
if command == 'si':
    Defensa_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
if command == 'si':
    Defensa_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
if command == 'si':
    Defensa_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
if command == 'si':
    Defensa_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
if command == 'si':
    Defensa_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
if command == 'si':
    Defensa_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))

command = input('Deseas Atacar? ')

if command == 'si':
    Ataque_A -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))
if command == 'si':
    Defensa_B -= 1
    print('El Ataque de {} es {} y la defensa es {}'.format(Segundo_Personaje, Ataque_B, Defensa_B))
else: 
    print('El Ataque de {} es {} y la defensa es {}'.format(Primer_Personaje, Ataque_A, Defensa_A))

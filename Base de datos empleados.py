'''1 Crea una clase llamada Empleado que tenga los siguientes atributos:

id (entero): Representa el ID del empleado.
nombre (cadena de caracteres): Representa el nombre del empleado.
salario (número decimal): Representa el salario del empleado.

La clase Empleado debe tener un método mostrar_informacion() que imprima por pantalla la información del 
empleado en el siguiente formato:

makefile

ID: <id>
Nombre: <nombre>
Salario: <salario>

2 Crea una clase llamada BaseDeDatosEmpleados que tenga los siguientes atributos:

    empleados (diccionario): Representa una base de datos de empleados, donde la clave es el ID 
    del empleado y el valor es una instancia de la clase Empleado.

 La clase BaseDeDatosEmpleados debe tener los siguientes métodos:

    agregar_empleado(empleado): Recibe un objeto de la clase Empleado y lo agrega a la base de datos 
    de empleados.
    eliminar_empleado(id): Recibe el ID de un empleado y lo elimina de la base de datos de empleados.
    mostrar_empleados(): Muestra por pantalla la información de todos los empleados en la base de datos, 
    utilizando el método mostrar_informacion() de la clase Empleado.

3 Crea una instancia de la clase BaseDeDatosEmpleados llamada bd_empleados.

4 Crea al menos tres instancias de la clase Empleado con diferentes valores para los atributos id, 
nombre y salario.

5 Agrega los empleados creados anteriormente a la base de datos bd_empleados utilizando
el método agregar_empleado().

6 Muestra por pantalla la información de todos los empleados en la base de datos utilizando el 
método mostrar_empleados().

7 Elimina uno de los empleados de la base de datos utilizando el método eliminar_empleado().

8 Muestra por pantalla la información actualizada de todos los empleados en la base de datos 
utilizando el método mostrar_empleados().'''

class Empleado:
    def __init__(self, Id, Nombre, Salario):
        self.Id = Id 
        self.Nombre = Nombre
        self.Salario = Salario

    def mostrar_informacion(self):
        print(f"\nID:", (self.Id))
        print(f'Nombre:', (self.Nombre))
        print(f'Salario:', (self.Salario))

class Basededatosempleados(Empleado):
    def __init__(self):
        self.Empleados = {}
                
    def agregar_empleados(self, empleado):
        self.Empleados[empleado.Id] = empleado
    
    def eliminar_empleados(self, Id):
        if Id in self.Empleados:
            del self.Empleados[Id]
    
    def mostrar_empleados(self):
        for empleado in self.Empleados.values():
            empleado.mostrar_informacion()

bd_empleados = Basededatosempleados() 

Empleado1 = Empleado('X45N678', 'Axel Rose', 25000)
Empleado2 = Empleado('Z62O542', 'Melinda Powers', 30000)
Empleado3 = Empleado('W54T883', 'Diana Crawford', 35000)

bd_empleados.agregar_empleados(Empleado1)
bd_empleados.agregar_empleados(Empleado2)
bd_empleados.agregar_empleados(Empleado3)

print('\nInformacion de todos los empleados:')
bd_empleados.mostrar_empleados()

bd_empleados.eliminar_empleados('W54T883')

print('\nInformacion de todos los empleados Actualizado:')
bd_empleados.mostrar_empleados()


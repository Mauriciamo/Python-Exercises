'''Implementa un programa en Python que gestione el inventario de una tienda de deportes.
Utiliza funciones, programación orientada a objetos, gestión de excepciones y diccionarios.
El programa debe realizar lo siguiente:

1.Define la clase "Producto" con los atributos nombre, precio y stock.
2.Implementa el método "mostrar_info()" en la clase Producto.
3.Crea la función "calcular_precio_total" que reciba un diccionario de inventario y calcule el precio total.
4.En la función principal, crea un diccionario de inventario con al menos tres productos y 
muestra su información.
5.Llama a la función "calcular_precio_total" con el diccionario de 
inventario y muestra el precio total resultante.
6.Gestiona las excepciones para claves inválidas en el diccionario y para cualquier excepción inesperada.'''

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"{self.nombre} - ${self.precio} - Stock: {self.stock}"
    
def calcular_precio_total():
    inv = {'Pelota Football' : 240, 'Pelota Basket': 300, 'Raqueta Tennis' : 220}
    print(inv)
    data = list(inv.values())
    total_price = sum(data)
    print(total_price)    


calcular_precio_total()

Football = Producto('Pelota Football', 24, 10)

print(Football)

Basket = Producto('Pelota Basket', 30, 10)

print(Basket)

Tennis = Producto('Raqueta Tennis', 44, 5)

print(Tennis)
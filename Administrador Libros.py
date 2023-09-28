'''Escribe un programa en Python que implemente un sistema de administración de libros 
utilizando programación orientada a objetos, funciones y programación funcional.

El programa debe tener las siguientes funcionalidades:

Definir una clase llamada "Libro" que tenga los siguientes atributos: título, autor,
año de publicación y precio.

Implementar métodos en la clase "Libro" para obtener y establecer los valores de los atributos.

Crear una función llamada "crear_libro" que solicite al usuario ingresar los datos de un libro 
(título, autor, año de publicación y precio) y devuelva un objeto de la clase 
"Libro" con los valores ingresados.

Implementar una función llamada "calcular_descuento" que tome como parámetro el precio de un libro y 
devuelva el precio con un descuento del 10%.

Crear una lista de libros utilizando la función "crear_libro" y almacenarlos en una lista llamada "biblioteca".

Utilizar la función "map" para aplicar la función "calcular_descuento" a todos los libros de la biblioteca y
obtener una lista con los precios actualizados.

Implementar una función llamada "imprimir_libros" que tome como parámetro una 
lista de libros y los imprima en el siguiente formato:
Título: [título], Autor: [autor], Año de publicación: [año], Precio: [precio]

Llamar a la función "imprimir_libros" para imprimir la lista de libros actualizada con los precios descontados.
'''
class Libro: 
  def __init__(self, titulo,autor,anyo,precio):
    self.titulo = titulo
    self.autor = autor
    self.anyo = anyo
    self.precio = precio
  
  def obtenertitulo(self):
    return self.titulo

  def obteneranyo(self):
    return self.anyo

  def obtenerautor(self):
    return self.autor

  def obtenerprecio(self):
    return self.precio 
  
  def obtenerlibro(self):
    return self.titulo, self.anyo, self.autor, self.precio   
  
  def establecertitulo(self,titulo):
    self.titulo = titulo

  def estableceranyo(self,anyo):
    self.anyo = anyo

  def establecerautor(self,autor):
    self.autor = autor

  def establecerprecio(self,precio):
    self.precio = precio

def crear_libro():
  titulo = input("Dime el titulo: ")
  autor = input("Dime el autor: ")
  anyo = input("Dime el año: ")
  precio = float(input("Dime el precio: "))
  return Libro(titulo,autor,anyo,precio)

def calculardescuento(precio):
  return precio*0.9

biblioteca = []

def rellenarbiblioteca():
  cantidad = int(input("¿Cuantos libros quieres agregar a la biblioteca? "))
  for _ in range(cantidad):
    libro = crear_libro()
    biblioteca.append(libro)

rellenarbiblioteca()
precios_actualizados = list(map(lambda libro: calculardescuento(libro.obtenerprecio()),biblioteca))

i=0
for libro in biblioteca:
  libro.establecerprecio(precios_actualizados[i])
  i+=1

def imprimirlibros(lista):
  for libro in lista:
    print("Titulo: ",libro.obtenertitulo())
    print("Año: ",libro.obteneranyo())
    print("Autor: ",libro.obtenerautor())
    print("Precio: ",libro.obtenerprecio())
    print()

imprimirlibros(biblioteca)
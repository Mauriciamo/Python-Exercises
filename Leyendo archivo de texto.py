'''Crear un programa que lea un archivo de texto y elimine todas las líneas que 
contienen una cadena específica. Además, el programa debe crear un nuevo archivo de texto con el resultado.

Para este ejercicio, se puede utilizar la función "with" para abrir y cerrar el archivo de texto. 
También se puede utilizar la sentencia "try-except" para manejar cualquier excepción 
que pueda surgir al abrir y leer el archivo.'''

try:
  with open("texto2.txt","r") as archivooriginal:
    with open("textonuevo.txt","w") as archivonuevo:
      for linea in archivooriginal:
        if "eliminar" not in linea:
          archivonuevo.write(linea)

except:
  print("El archivo de texto no existe.")
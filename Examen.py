#Ejercicio 1 - Realizar una función auto generadora de claves, similar a la que tiene Google 
# que le recomienda al usuario una clave segura para una adecuada gestión de su seguridad.

#La clave generada debe tener letras mayúsculas, minúsculas, números, símbolos y una longitud 
# mínima de 15  y una máxima de 20 caracteres.
#Para resolver este ejercicio se deben utilizartodos los conociminetos adquiridos en el curso.
#El resultado del programa es la clave segura generada por el programa

from random import choice
longitud = int(input("Ingrese la longitud de la contraseña: "))
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
if longitud < 15 or longitud > 20:
    print("La longitud de la contraseña debe estar entre 15 y 20 caracteres")
    print("Intente nuevamente")
    exit()
else:
    if longitud >= 15 and longitud <= 20:
        contraseña = ""
        contraseña = contraseña.join([choice(valores) for i in range(longitud)])
        print("\n"+contraseña+"\n")  




#Ejercicio 2 - Con los conocimientos adquiridos realice un menú cuya primera opción es un 
# programa que verifique si el texto ingresado es un palíndromo. En la segunda opción se 
# permitirá ingresar una frase al usuario por teclado y el programa debe:

#Realizar un conteo por cada una de las vocales que se encuentren en la frase ingresada por el usuario.
#Mostrar cuantas letras mayúsculas, cuantas minúsculas fueron ingresadas.
#Mostrar por cuantas palabras de más de dos letras o caracteres esta conformada la frase
def es_palindromo(texto):
  texto = texto.lower() 
  texto = texto.replace(" ", "") 
  return texto == texto[::-1] 

def contar_vocales(texto):
  vocales = "aeiou"
  contadores = {}
  for vocal in vocales:
    contadores[vocal] = 0
  for caracter in texto.lower():
    if caracter in vocales:
      contadores[caracter] += 1
  return contadores

def contar_mayusculas_minusculas(texto):
  mayusculas = 0
  minusculas = 0
  for caracter in texto:
    if caracter.isupper():
      mayusculas += 1
    elif caracter.islower():
      minusculas += 1
  return (mayusculas, minusculas)

def contar_palabras(texto):
  palabras = texto.split()
  contador = 0
  for palabra in palabras:
    if len(palabra) > 2:
      contador += 1
  return contador

while True:
  print("Menú de opciones - Realizado por: David Marcelo Guerra Andrade\n")  
  print("1. Verificar si el texto es un palíndromo")
  print("2. Realizar un conteo de vocales, cuantas mayúsculas y minusculas, palabras de mas de dos letras en una frase")
  print("3. Dar gracias al profesor")
  print("0. Salir")
  opcion = int(input("\nSelecciona una opción (0 para salir): "))
  if opcion == 0:
    print("\nExcelente clases, muchas gracias Profesor, Att: War\n")
    break
  elif opcion == 1:
    texto = input("Ingresa el texto a verificar: ")
    if es_palindromo(texto):
      print("\nEl texto es un palíndromo\n")
    else:
      print("\nEl texto no es un palíndromo\n")
  elif opcion == 2:
    texto = input("Ingresa la frase: ")
    contadores = contar_vocales(texto)
    for vocal, contador in contadores.items():
      print(f"La vocal '{vocal}' aparece {contador} veces")
      mayusculas, minusculas = contar_mayusculas_minusculas(texto)
    print(f"\nHay {mayusculas} mayúsculas y {minusculas} minúsculas\n")
    print(f"La frase tiene {contar_palabras(texto)} palabras de más de dos letras\n")
  elif opcion == 3:
    print("\nExcelente clases, muchas gracias Profesor, Att: War\n")






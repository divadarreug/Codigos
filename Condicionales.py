#Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
#si es mayor de edad o no.
#x = int(input("Escriba su edad: "))
#if (x < 18 and x >= 1) :
#    print("Es menor de edad")
#elif (x >= 18):
#    print("Mayor de edad")
#elif (x <= 0):
#    print("Edad no valida")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
#por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y 
#minúsculas.
key = "contraseña"
password = input("Introduce la contraseña: ")
if key == password:
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
#Si el divisor es cero el programa debe mostrar un error.
x = int(input("Escriba su numero a dividir: "))
y = int(input("Escribir el numero por el cual dividir: "))

if (y == 0):
    print("No se valido el divisor")
else:
    z =round(x/y,2)
    print("El resultado de la division es:",z)



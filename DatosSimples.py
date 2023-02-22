x = 3+2
y = 2*5
z = (x/y)**2
print("Hola",z )

x = int(input("Cuantas horas trabajaste? "))
y = int(input("Cual es valor por hora? "))

print("Tu pago es:", x*y)

x = int(input("Valor de x: "))
y = x*(x+1)/2
print(y)

#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
#Suele hacer venta por correo y la empresa de logística les cobra por peso de 
#cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán 
#en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un 
#programa que lea el número de payasos y muñecas vendidos en el último pedido y 
#calcule el peso total del paquete que será enviado.
peso_p = 112
peso_m = 75
p = int(input("Cuantos payaso va a enviar? "))
m = int(input("Cuantas muñecas va a enviar? "))
print("El peso total del parque es:", (peso_p * p)+(peso_m * m))

#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
#Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
#final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero 
#depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular 
#y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear 
#cada cantidad a dos decimales.
x = 0.04
y1 = float(input("Valor de la invesion del primer año? "))
y2 = float(input("Valor de la invesion del segundo año? "))
y3 = float(input("Valor de la invesion del tercer año? "))
z1 = round(y1*(1+x),2)
z2 = round((x*y2)+y2,2)
z3 = round((x*y3)+y3,2)
print(z1)
print(z2)
print(z3)

#Una panadería vende barras de pan a 3.49€ cada una. 
#El pan que no es el día tiene un descuento del 60%. 
#Escribir un programa que comience leyendo el número 
#de barras vendidas que no son del día. Después el programa 
#debe mostrar el precio habitual de una barra de pan, el 
#descuento que se le hace por no ser fresca y el coste final total.
x = 3.49
y = 0.60
z = int(input("Cuantas barras de pan se vendieron que no son al día? "))
t = (z*x)
t2 = round(t-(t*y),2)
print("El costo inicial de una barra es:",x,"El descuente que se hace por no ser al dia es 60%", "El valor total de los panes vendidos es",t2)
#Ejercicio 1
print('Ejercicio 1')
number = int(input('Ingrese un número: '))

if number % 2 == 0:
    print('El número es par')
else:
    print('El número es impar')

#Ejercicio 2
print('Ejercicio 2')
name = input('Ingrese su nombre: ')
sex = input('Ingrese su sexo (M/F): ')

if name[0].lower() < 'm' and name[0].lower() > 'a' and sex.lower() == 'F':
    print('Grupo A')
elif name[0].lower() > 'n' and name[0].lower() < 'z' and sex.lower() == 'M':
    print('Grupo A')
else:
    print('Grupo B')

#Ejercicio 3
password = 'password123'
user_password = input('Ingrese la contraseña: ')
user_password = user_password.lower()
if password == user_password:
    print('La contraseña es correcta')
else:
    print('La contraseña es incorrecta')

#Ejercicio 4: 
''''''
print("BIENVENIDO A PIZZERIA WAR\n")
pizza_vegetariana = input('¿Quiere una pizza vegetariana? (si/no): ')
if pizza_vegetariana == 'si':
    print('''
    1. Tipo 1
    2. Tipo 2
    3. Tipo 3
    4. Tipo 4
    ''')
    tipo_pizza = int(input('Ingrese el tipo de pizza: '))
    if tipo_pizza == 1:
        print("La pizza es vegetariana con los ingredientes:",'Pimiento, tofu')
    elif tipo_pizza == 2:
        print("La pizza es vegetariana con los ingredientes:",'Salsa de tomate, cebolla')
    elif tipo_pizza == 3:
        print("La pizza es vegetariana con los ingredientes:",'Champiñones, brócoli')
    elif tipo_pizza == 4:
        print("La pizza es vegetariana con los ingredientes:",'7 Quesos')
    else:
        print('Tipo de pizza no disponible')
elif pizza_vegetariana == 'no':
    print('''
    1. Tipo 1
    2. Tipo 2
    3. Tipo 3
    ''')
    tipo_pizza = int(input('Ingrese el tipo de pizza: '))
    if tipo_pizza == 1:
        print("La pizza no es vegetariana con ingredientes:",'Peperoni, Carne')
    elif tipo_pizza == 2:
        print("La pizza no es vegetariana con ingredientes:",'Pollo, Jamón')
    elif tipo_pizza == 3:
        print("La pizza no es vegetariana con ingredientes:",'Salchichón Italiano, Salami')
    else:
        print('Tipo de pizza no disponible')
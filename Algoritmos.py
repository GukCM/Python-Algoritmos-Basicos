# Ejercicio 
# Escribir un programa que muestre por pantalla la cadena ¡Hola Mundo!.

print("Hola mundo")

print("-" *20)

# Ejercicio 
# Escribir un programa que almacene la cadena ¡Hola Mundo! en una variable y luego muestre por pantalla el contenido de la variable.

saludo = "Hola mundo"
print(saludo)
print("-" * 20)

# Ejercicio 
# Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el usuario haya introducido.

saludoformal = input("Introduce tu nombre: ")
print("Hola ", saludoformal)
print("-" *20)

# Ejercicio
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

time_work = float(input("Ingresa tus horas trabajadas: "))
flag = float(input("Cuanto es el coste por hora: "))
payment = time_work * flag
print("Tu paga es: ", payment)
print("-" * 20)

# Ejercicio 
# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla
# en líneas distintas el nombre del usuario tantas veces como el número introducido.
name = input("Ingresa tu nombre: ")
times = int(input("Ingresa un numero: "))
print(name * times)
print("-" * 20)

# Ejercicio 
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
age = float(input("Ingresa tu edad: "))
if age < 18:
    print("Eres menor de edad")
else:
    print("Eres mayor de edad")
print("-" * 20)

# Ejercicio 
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla
#  si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

password = input("Ingrese su contraseña: ")
verify = input("Verifique su contraseña: ")
if verify != password:
    print("Contraseña incorrecta")
else:
    print("Contraseña verificada")
print("-" * 20)

# Ejercicio 
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. 
# Escribir un programa que pregunte
#  al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

edad = float(input("Ingresa tu edad: "))
monthly_payment = float(input("Tus ingresos mensuales: "))
if edad > 16 and monthly_payment > 1000:
    print("Debes presentar tributo")
else:
    print("No debes presentar tributo")
print("-" * 20)


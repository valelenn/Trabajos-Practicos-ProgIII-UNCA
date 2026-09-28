# Trabajo Práctico N° 4 - EJERCICIO 1

#Definimos una lista predefinida de números
lista_numeros=[2,4,6,8]

#Le pedimos al usuario el ingreso del numero
numero = int(input("Ingrese un numero del 0 al 9: "))

#Validamos si el dato ingresado es correcto
while numero < 0 or numero > 9:
    print("ERROR: Debe ingresar un numero del 0 al 9")
    numero = int(input("Por favor, ingrese un número válido: "))

#Salimos del bucle una vez que el número sea válido, ahora verifico si está en la lista predefinida
if numero in lista_numeros:
    print(f"El numero {numero} SI se encuentra en la lista")
else:
    print(f"El numero {numero} NO se encuentra en la lista")
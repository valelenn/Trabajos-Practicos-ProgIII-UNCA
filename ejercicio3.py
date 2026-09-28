# Trabajo Práctico N° 4 - EJERCICIO 3

#creamos una lista vacía que va a almacenar los usuario_info, así cumplimos el item 3
lista_usuarios = []
continuar="s"

#Ingreso de Varios usuarios (item 3)
while continuar== "s":

    print("Ingrese los datos del usuario")

# Item 1: solicitar nombre, edad, dirección y teléfono
    nombre=(input("Ingrese el nombre: "))
    edad= int((input("Ingrese la edad: ")))
    direccion = (input("Ingrese la dirección: "))
    telefono = int((input("Ingrese el teléfono: ")))

# item 2: Almacenar los datos en un diccionario llamado usuario_info
    usuario_info={
        "nombre":nombre,
        "edad":edad,
        "direccion":direccion,
        "telefono":telefono
    }

# Guardamos el diccionario en la lista
    lista_usuarios.append(usuario_info)

#Verificar si quiere seguir agregando
    continuar=input("\n¿Desea ingresar otro usuario? (s/n): ").lower()

#item 4: Mostrar la información registrada
print(" - Mostrar Información de usuarios: ")

for posicion,usuario in enumerate(lista_usuarios, start=1):
    print(f"\n Usuario N° {posicion} ")
    # Recorremos el diccionario obteniendo clave y valor con .items()
    for clave, valor in usuario.items():
        print(f"{clave.capitalize()}: {valor}")
        #.capitalize() pone la primera letra en mayúscula.

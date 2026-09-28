# Trabajo Práctico N° 4 - EJERCICIO 2

#Crear conjunto llamado usuarios
usuarios = {"Marcela","David","Elvira","Juan","Marcos"}

#Crear conjunto llamado administradores
administradores = {"Juan","Marcela"}

#Eliminar a Juan del conjunto de administradores
administradores.discard("Juan")

#Añadir a Marcos como administrador
administradores.add("Marcos")

# Recorremos cada nombre dentro del conjunto de usuarios
for usuario in usuarios:
    # Verificamos si este usuario en particular pertenece al conjunto de administradores
    if usuario in administradores:
        print(f"{usuario}: Es Administrador")
    else:
        print(f"{usuario}: No es Administrador")
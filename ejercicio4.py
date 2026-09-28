# TRABAJO PRÁCTICO N° 4 - Ejercicio 4

# Creamos una lista[] de diccionarios {} donde cada sucursal tiene una lista de instrumentos, seria la fabrica entera
sucursales = [
    #Para almacenar una sucursal con su nombre e instrumentos usamos un diccionario
    {
        "nombre": "Centro",
    #Como los instrumentos son muchos, usamos una lista dentro de otro diccionario
        "instrumentos": [
    #Para almacenar los datos de un instrumento utilizo un diccionario
            {"id": "INS01", "precio": 150000, "tipo": "Percusión"},
            {"id": "INS02", "precio": 85000, "tipo": "Viento"},
            {"id": "INS03", "precio": 230000, "tipo": "Cuerda"}
        ]
    },
    {
        "nombre": "Norte",
        "instrumentos": [
            {"id": "INS04", "precio": 120000, "tipo": "Cuerda"},
            {"id": "INS05", "precio": 95000, "tipo": "Viento"},
            {"id": "INS06", "precio": 180000, "tipo": "Percusión"}
        ]
    }
]
#Tenemos 2 sucursales, en el centro con 3 instrumentos y en el norte con 3 instrumentos más

# Requisito 1: listarInstrumentos()
def listarInstrumentos():

    print("\n LISTADO COMPLETO DE INSTRUMENTOS ")
    #Como tenemos 2 listas, uso 2 bucles, primero para la sucursal y luego para los instrumentos de esa sucursal
    for suc in sucursales:
        for inst in suc["instrumentos"]:
            print(f"Nombre de la sucursal: {suc["nombre"]} | ID: {inst["id"]} | Precio: {inst["precio"]} | Tipo: {inst["tipo"]}")

# Requisito 2: instrumentosPorTipo(tipo)
def instrumentosPorTipo(tipo):
#necesitamos devolver una lista con los instrumentos del mismo tipo
    resultado = []
    for suc in sucursales:
        for inst in suc["instrumentos"]:
            if inst["tipo"].lower() == tipo.lower():
                resultado.append(inst)
    return resultado

# Requisito 3: borrarInstrumento(id)
def borrarInstrumento(id_buscado):
    for suc in sucursales:
        for inst in suc["instrumentos"]:
            if inst["id"] == id_buscado:
                suc["instrumentos"].remove(inst)
                print(f"\n Instrumento '{id_buscado}' eliminado con éxito de la sucursal {suc['nombre']}.")
                return True
    print(f"\n No se encontró ningún instrumento con el ID '{id_buscado}'.")
    return False


# Requisito 4: porcInstrumentosPorTipo(sucursal)
def porcInstrumentosPorTipo(nombre_sucursal):

    for suc in sucursales:
        if suc["nombre"].lower() == nombre_sucursal.lower():
            total_instrumentos = len(suc["instrumentos"])

            if total_instrumentos == 0:
                print(f"\n La sucursal {suc['nombre']} no tiene instrumentos registrados.")
                return

            # Contadores por tipo -> Diccionario
            conteo = {"Percusión": 0, "Viento": 0, "Cuerda": 0}

            for inst in suc["instrumentos"]:
                tipo = inst["tipo"]
                if tipo in conteo:
                    conteo[tipo] += 1

            print(f"\n Porcentajes de instrumentos en sucursal -> {suc['nombre']} ")
            print(f"\n Total de instrumentos: {total_instrumentos}")
            for tipo, cantidad in conteo.items():
                porcentaje = (cantidad / total_instrumentos) * 100
                print(f"  • {tipo}: {porcentaje:.2f}% ({cantidad} de {total_instrumentos})")
            return

    print(f"\n No se encontró la sucursal '{nombre_sucursal}'.")


# Puebas
if __name__ == "__main__":
    # 1. Probar listar todos
    listarInstrumentos()

    # 2. Probar buscar por tipo
    print("\n Instrumentos de tipo 'Cuerda' ")
    cuerdas = instrumentosPorTipo("Cuerda")
    for inst in cuerdas:
        print(inst)

    # 3. Probar borrar instrumento
    borrarInstrumento("INS02")

    # 4. Probar porcentaje por sucursal
    porcInstrumentosPorTipo("Centro")
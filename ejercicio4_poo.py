# TRABAJO PRÁCTICO N° 4 - Ejercicio 4

# Primera clase: Instrumentos
class Instrumento:
    def __init__(self, id_instrumento, precio, tipo): # -> Constructor de una clase
        self.id = id_instrumento
        self.precio = precio
        self.tipo = tipo


# Segunda clase: Sucursal
class Sucursal:
    def __init__(self, nombre):
        self.nombre = nombre
        self.instrumentos = []

    def agregar_instrumento(self, instrumento):
        self.instrumentos.append(instrumento)


#Tercera clase: Fabrica con las funciones requeridas
#self -> instancia concreta del objeto que está ejecutando el métod
class Fabrica:
    def __init__(self):
        self.sucursales = []

    def agregar_sucursal(self, sucursal):
        self.sucursales.append(sucursal)

    # 1. listarinstrumentos()
    def listarinstrumentos(self):
        print("\n LISTADO COMPLETO DE INSTRUMENTOS ")
        for suc in self.sucursales:
            for inst in suc.instrumentos:
                print(f"Nombre de la sucursal: {suc.nombre} | ID: {inst.id} | Tipo: {inst.tipo} | Precio: ${inst.precio}")

    # 2. instrumentosPorTipo(tipo)
    def instrumentosPorTipo(self, tipo):
        resultado = []
        for suc in self.sucursales:
            for inst in suc.instrumentos:
                if inst.tipo.lower() == tipo.lower():
                    resultado.append(inst)
        return resultado

    # 3. borrarinstrumento(id)
    def borrarinstrumento(self, id_buscado):
        for suc in self.sucursales:
            for inst in suc.instrumentos:
                if inst.id == id_buscado:
                    suc.instrumentos.remove(inst)
                    print(f"\n Instrumento {id_buscado} eliminado con éxito de la sucursal {suc.nombre}.")
                    return True
        print(f"\n No se encontró ningún instrumento con el ID '{id_buscado}'.")
        return False

    # 4. porcinstrumentosPorTipo(sucursal)
    def porcinstrumentosPorTipo(self, nombre_sucursal):
        for suc in self.sucursales:
            if suc.nombre.lower() == nombre_sucursal.lower():
                total_instrumentos = len(suc.instrumentos)

                if total_instrumentos == 0:
                    print(f"\n La sucursal {suc.nombre} no tiene instrumentos registrados.")
                    return

                conteo = {"Percusión": 0, "Viento": 0, "Cuerda": 0}

                for inst in suc.instrumentos:
                    tp = inst.tipo.lower()
                    if tp in conteo:
                        conteo[tp] += 1

                print(f"\n Porcentajes de instrumentos en sucursal -> {suc['nombre']} ")
                print(f"Total de instrumentos: {total_instrumentos}")
                for tipo, cantidad in conteo.items():
                    porcentaje = (cantidad / total_instrumentos) * 100
                    print(f"  • {tipo}: {porcentaje:.2f}% ({cantidad} de {total_instrumentos})")
                return

        print(f"\n No se encontró la sucursal '{nombre_sucursal}'.")

#Pruebas
if __name__ == "__main__":
    fabrica = Fabrica()

    # Creación y carga de Sucursal Centro
    suc_centro = Sucursal("Centro")
    suc_centro.agregar_instrumento(Instrumento("INS01", 150000, "Percusión"))
    suc_centro.agregar_instrumento(Instrumento("INS02", 85000, "Viento"))
    suc_centro.agregar_instrumento(Instrumento("INS03", 230000, "Cuerda"))

    # Creación y carga de Sucursal Norte
    suc_norte = Sucursal("Norte")
    suc_norte.agregar_instrumento(Instrumento("INS04", 120000, "Cuerda"))
    suc_norte.agregar_instrumento(Instrumento("INS05", 95000, "Viento"))
    suc_norte.agregar_instrumento(Instrumento("INS06", 180000, "Percusión"))

    # Asociar sucursales a la fábrica
    fabrica.agregar_sucursal(suc_centro)
    fabrica.agregar_sucursal(suc_norte)

    # 1. Probar listar todos
    fabrica.listarinstrumentos()

    # 2. Probar buscar por tipo
    print("\n Instrumentos de tipo 'Cuerda' ")
    cuerdas = fabrica.instrumentosPorTipo("Cuerda")
    for inst in cuerdas:
        print(f"ID: {inst.id} | Precio: ${inst.precio}")

    # 3. Probar borrar instrumento
    fabrica.borrarinstrumento("INS02")

    # 4. Probar porcentaje por sucursal
    fabrica.porcinstrumentosPorTipo("Centro")
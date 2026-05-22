import json

class MostrarMixin:
    
    def consultar(self):
        print(f"--- {self.__class__.__name__} ---")

        for a, b in self.__dict__.items():
            print(f"{a}: {b}")


class ArchivoMixin:

    def guardar(self, basededatos_biblioteca):
        with open(basededatos_biblioteca, "w") as archivo:
            json.dump(self.__dict__, archivo)

        print(f"Archivo {basededatos_biblioteca} guardado.")

    @classmethod
    def cargar(cls, basededatos_biblioteca):
        with open(basededatos_biblioteca, "r") as archivo:
            datos = json.load(archivo)

        print(f"--- Cargando {basededatos_biblioteca} ---")

        for clave, valor in datos.items():
            print(f"{clave}: {valor}")


class Libro(MostrarMixin, ArchivoMixin):

    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible


class Socio(MostrarMixin, ArchivoMixin):

    def __init__(self, nombre, cedula, activo):
        self.nombre = nombre
        self.cedula = cedula
        self.activo = activo


libro1 = Libro("Cien años de soledad", "García Márquez", True)
socio1 = Socio("Ana Torres", "0912345678", True)


libro1.consultar()
socio1.consultar()


libro1.guardar("libro.json")
socio1.guardar("socio.json")


Libro.cargar("libro.json")
Socio.cargar("socio.json")

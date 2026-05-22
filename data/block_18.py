import json


class MostrarMixin:
    def consultar(self):
        print(f"\n--- {self.__class__.__name__} ---")
        for atributo, valor in self.__dict__.items():
            print(f"{atributo}: {valor}")


class ArchivoMixin:
    def guardar(self, nombre_archivo):
        with open(nombre_archivo, "w", encoding="utf-8") as f:
            json.dump(self.__dict__, f, indent=2, ensure_ascii=False)
        print(f"\nArchivo {nombre_archivo} guardado.")

    @classmethod
    def cargar(cls, nombre_archivo):
        print(f"\n--- Cargando {nombre_archivo} ---")
        with open(nombre_archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        for clave, valor in datos.items():
            print(f"{clave}: {valor}")


class Libro(MostrarMixin, ArchivoMixin):
    def __init__(self, titulo, autor, disponible):
        self.titulo     = titulo
        self.autor      = autor
        self.disponible = disponible


class Socio(MostrarMixin, ArchivoMixin):
    def __init__(self, nombre, cedula, activo):
        self.nombre  = nombre
        self.cedula  = cedula
        self.activo  = activo


class Block18:
    title = "Block 18 - Taller 1: Mixins + Archivos JSON"

    def __init__(self):
        self.exercises = [
            "Ejercicio 1 - Biblioteca del Barrio (MostrarMixin + ArchivoMixin)",
        ]

    def exercise_1(self):
        libro = Libro("Cien años de soledad", "García Márquez", True)
        socio = Socio("María López", "1234567890", True)

        libro.consultar()
        socio.consultar()

        libro.guardar("libro.json")
        socio.guardar("socio.json")

        Libro.cargar("libro.json")
        Socio.cargar("socio.json")


if __name__ == "__main__":
    b = Block18()
    b.exercise_1()


class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.catalogo:
            if libro.titulo == titulo:
                return libro
        return None

    def prestar_libro(self, titulo, usuario):
        libro = self.buscar_libro_por_titulo(titulo)
        if libro:
            if libro.disponible:
                libro.disponible = False
                print(f"El libro '{titulo}' ha sido prestado a {usuario.nombre}.")
            else:
                print(f"El libro '{titulo}' no está disponible actualmente.")
        else:
            print(f"No se encontró el libro '{titulo}' en el catálogo.")

    def devolver_libro(self, titulo):
        libro = self.buscar_libro_por_titulo(titulo)
        if libro:
            libro.disponible = True
            print(f"El libro '{titulo}' ha sido devuelto correctamente.")
        else:
            print(f"No se encontró el libro '{titulo}' en el catálogo.")

# Ejemplo de uso
biblioteca = Biblioteca()

# Agregar libros al catálogo
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-84-9759-252-3")
libro2 = Libro("El principito", "Antoine de Saint-Exupéry", "978-84-261-1877-0")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Juan", "juan@example.com")
usuario2 = Usuario("María", "maria@example.com")

# Realizar préstamos
biblioteca.prestar_libro("Cien años de soledad", usuario1)
biblioteca.prestar_libro("El principito", usuario2)

# Devolver libros
biblioteca.devolver_libro("Cien años de soledad")

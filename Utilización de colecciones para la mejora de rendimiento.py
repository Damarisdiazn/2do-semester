class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor  # Almacena el autor como una tupla (nombre, apellido)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor[0]} {self.autor[1]} (ISBN: {self.isbn})"


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para almacenar libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario para almacenar libros por ISBN
        self.usuarios = set()  # Conjunto para almacenar IDs de usuarios únicos

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print(f"Libro añadido: {libro}")

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            removed_book = self.libros.pop(isbn)
            print(f"Libro quitado: {removed_book}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")
        else:
            print("El ID de usuario ya está registrado.")

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            self.usuarios.remove(id_usuario)
            print(f"Usuario dado de baja: {id_usuario}")
        else:
            print("El ID de usuario no se encuentra registrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            for usuario in self.usuarios:
                if usuario.id_usuario == id_usuario:
                    usuario.libros_prestados.append(libro)
                    print(f"Libro prestado: {libro} a {usuario.nombre}")
                    return
        print("No se puede prestar el libro. Verifique el ISBN o el ID de usuario.")

    def devolver_libro(self, isbn, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                for libro in usuario.libros_prestados:
                    if libro.isbn == isbn:
                        usuario.libros_prestados.remove(libro)
                        print(f"Libro devuelto: {libro} por {usuario.nombre}")
                        return
        print("No se puede devolver el libro. Verifique el ISBN o el ID de usuario.")

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor.lower() in libro.titulo.lower()) or \
               (criterio == "autor" and valor.lower() in libro.autor[0].lower()) or \
               (criterio == "categoria" and valor.lower() in libro.categoria.lower()):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario.libros_prestados
        return []
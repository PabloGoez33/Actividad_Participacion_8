from tiendalibros.modelo.libro import Libro

class ItemCompra:
    def __init__(self, libro: Libro, cantidad_libro: int):
        self.libro: Libro = libro
        self.cantidad_libro: int = cantidad_libro

    def calcular_subtotal(self):
        return self.libro.precio * self.cantidad_libro
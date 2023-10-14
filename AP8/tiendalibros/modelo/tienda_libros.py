from tiendalibros.modelo.carro_compra import CarroCompras
from tiendalibros.modelo.libro_existente_error import LibroExistenteError
from tiendalibros.modelo.libro import Libro
from tiendalibros.modelo.libro_agotado_error import LibroAgotadoError
from tiendalibros.modelo.existencias_insuficientes_error import ExistenciasInsuficientesError


class TiendaLibros:
    # Defina metodo inicializador __init__
    def __init__(self):
        self.catalogo: dict = {}
        self.carrito: CarroCompras = CarroCompras()

    # Defina metodo adicionar_libro_a_catalogo
    def adicionar_libro_a_catalogo (self, isbn:str, titulo:str, precio:float, existencias:int) -> Libro:
        if isbn in self.catalogo:
            raise LibroExistenteError(isbn)
        nuevo_libro = Libro(isbn, titulo, precio, existencias)
        self.catalogo[isbn] = nuevo_libro
        return nuevo_libro

    # Defina metodo agregar_libro_a_carrito
    def agregar_libro_a_carrito (self, isbn, cantidad):
        
        libro = self.catalogo.get(isbn)

        if libro.existencias == 0:
            raise LibroAgotadoError(libro)

        if cantidad > libro.existencias:
            raise ExistenciasInsuficientesError(libro, cantidad)

        self.carrito.agregar_item(libro, cantidad)

    # Defina metodo retirar_item_de_carrito
    def  retirar_item_de_carrito(self, isbn):
        self.carrito.quitar_item(isbn)
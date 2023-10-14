from tiendalibros.modelo.libro_error import LibroError


class ExistenciasInsuficientesError(LibroError):
    
    # Defina metodo inicializador
    def __init__(self, isbn, cantidad_a_comprar:int):
        super().__init__(isbn)
        self.cantidad_a_comprar = cantidad_a_comprar

    # Defina metodo espcial
    def __repr__(self):
        return (f"El libro con titulo {self.libro.titulo} y isbn {self.libro.isbn} no tiene suficientes existencias para realizar la compra: cantidad a comprar: {self.cantidad_a_comprar}, existencias: {self.libro.existencias}")

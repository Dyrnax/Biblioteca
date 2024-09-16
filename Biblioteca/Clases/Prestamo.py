class Prestamo:
    def __init__(self,isbn,n_identificador,fecha_prestamo,fecha_entrega,entregado):
        self.isbn = isbn
        self.idprestamo = n_identificador
        self.fprestamo = fecha_prestamo
        self.fentrega = fecha_entrega
        self.entregado = entregado
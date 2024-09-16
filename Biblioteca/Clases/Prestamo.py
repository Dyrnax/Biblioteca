class Prestamo:
    def __init__(self,isbn,n_identificador,fecha_prestamo,fecha_entrega,fecha_devolucion):
        self.__isbn = isbn
        self.__n_idenificador = n_identificador
        self.__f_prestamo = fecha_prestamo
        self.__f_entrega = fecha_entrega
        self.__d_devolucion = fecha_devolucion
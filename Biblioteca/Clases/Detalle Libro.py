class DetalleLibro:
    def __init__(self,isbn,categoria,n_paginas,id_editorial):
        self.__isbn = isbn
        self.__editorial = id_editorial
        self.__categoria = categoria
        self.__npaginas = n_paginas
import Libro
import Categoria
import Editorial

class Detalle_libro(Libro,Categoria,Editorial):
    def __init__(self,isbn, id_categoria, n_paginas, id_editorial, fecha_edicion, id_detalle_libro, stock_total, stock_disponible):
        Libro.__init__(isbn)
        Categoria.__init__(id_categoria)
        Editorial.__init__(id_editorial)
        self.n_paginas = n_paginas
        self.fecha_edicion = fecha_edicion
        self.id_detalle_libro = id_detalle_libro
        self.stock_disponible = stock_disponible
        self.stock_total = stock_total
        
    
    def actualizar_disponibilidad(self, cantidad, accion):
        if (self.stock_total >= self.stock_disponible + cantidad):
            if (accion.lower() == "retirar"):
                if (self.stock_disponible > 0):
                    self.stock_disponible -= cantidad
                else:
                    print("No hay suficientes ejemplares para el prestamo")
            if (accion.lower() == "agregar"):
                self.stock_disponible += cantidad
            else:
                print("Acción no válida")
        else:
            print("Hay problemas en las cantidades")
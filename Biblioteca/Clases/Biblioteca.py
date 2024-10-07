import Editorial
import Libro

class Biblioteca(Editorial, Libro): # Hereda de Editorial y Libro
    def __init__(self, isbn, id_editorial, id_biblioteca, nombre, direccion, telefono):
        Libro.__init__(isbn)
        Editorial.__init__(id_editorial)
        self.id_biblioteca = id_biblioteca
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def buscar_libro(self): # Permite buscar libro
        pass
    
    def prestar_libro(self): # Permite prestar libro
        pass
    
    def devolver_libro(self): # Permite devolver libro
        pass
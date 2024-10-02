import Editorial
import Libro

class Biblioteca(Editorial, Libro):
    def __init__(self, isbn, id_editorial, id_biblioteca, nombre, direccion, telefono):
        Libro.__init__(isbn)
        Editorial.__init__(id_editorial)
        self.id_biblioteca = id_biblioteca
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
    
    def buscar_libro(self):
        pass
    
    def prestar_libro(self):
        pass
    
    def devolver_libro(self):
        pass
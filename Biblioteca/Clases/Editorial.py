import re
import Pais

class Editorial(Pais): # Hereda de pais para asignarle un pais a la editorial
    def __init__(self, id_editorial, nombre, telefono, codigo_pais, correo, direccion):
        Pais.__init__(codigo_pais)
        self.id_editorial = id_editorial
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        
    def validar_correo(self): # Valida correo segun la Expresión Regular
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo)):
            return True 
        else:
            return False
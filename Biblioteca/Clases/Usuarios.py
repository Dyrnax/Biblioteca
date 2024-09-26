import Pais
import re
from rut_chile import rut_chile

class Usuario(Pais):
    def __init__(self, nombre, n_identificador, correo, telefono, habilitado, codigo_pais, rut_usuario):
        Pais.__init__(codigo_pais) = codigo_pais
        self.nombre = nombre
        self.n_identificador = n_identificador
        self.correo = correo
        self.telefono = telefono
        self.habilitado = habilitado
        self.rut_usuario = rut_usuario
    
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)
    
    def validar_correo(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo)):
            return True 
        else:
            return False
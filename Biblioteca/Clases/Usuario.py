import Pais
import Tipo_usuario
import re
from rut_chile import rut_chile # Libreria para validacion de rut

class Usuario(Pais,Tipo_usuario): # Hereda de las clases Pais y Tipo usuario
    def __init__(self, nombre, n_identificador, correo, telefono, habilitado, codigo_pais, codigo_tipo_usuario, rut_usuario):
        Pais.__init__(codigo_pais)
        Tipo_usuario.__init__(codigo_tipo_usuario)
        self.nombre = nombre
        self.n_identificador = n_identificador
        self.correo = correo
        self.telefono = telefono
        self.habilitado = habilitado
        self.rut_usuario = rut_usuario
    
    def validar_rut(self): # Valida el rut del usuario según libreria
        return rut_chile.is_valid_rut(self.rut_usuario)
    
    def validar_correo(self): # Valida correo según Expresión Regular
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if(re.fullmatch(regex, self.correo)):
            return True 
        else:
            return False
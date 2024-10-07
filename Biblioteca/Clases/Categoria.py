import Tipo_de_texto as tipo_texto

class Categoria(tipo_texto): # Hereda de la clase Tipo de texto
    def __init__(self, id_categoria, id_tipo_texto, categoria):
        tipo_texto.__init__(id_tipo_texto)
        self.id_categoria = id_categoria
        self.categoria = categoria
        

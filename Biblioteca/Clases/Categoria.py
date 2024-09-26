import Tipo_de_texto as tipo_texto

class Categoria(tipo_texto):
    def __init__(self, id_categoria, id_tipo, categoria):
        tipo_texto.__init__(id_tipo) = id_tipo
        self.id_categoria = id_categoria
        self.categoria = categoria
        

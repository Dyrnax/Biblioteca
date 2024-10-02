import Pais

class Autor(Pais):
    def __init__(self, id_autor, codigo_pais, nombre, apellido, seudonimo, fecha_nac, fecha_def, biografia, foto):
        Pais.__init__(codigo_pais)
        self.id_autor = id_autor
        self.nombre = nombre
        self.apellido = apellido
        self.seudonimo = seudonimo
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia = biografia
        self.foto = foto
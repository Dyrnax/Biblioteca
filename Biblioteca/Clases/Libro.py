import Autor

class Libro(Autor): # Hereda de autor parasaber quien hizo el libro
    def __init__(self,isbn,titulo,id_autor,n_copias):
        Autor.__init__(id_autor)
        self.isbn = isbn
        self.titulo = titulo
        self.n_copias = n_copias
    
    def validar_isbn(self): # Valida el isbn del libro para saber si es auentico
        if(10 <= len(self.isbn) <= 13 and self.isbn.isdigit()):
            return True
        else:
            return False
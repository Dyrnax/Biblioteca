from datetime import datetime, timedelta # Libreria para manejo de fechas
import Detalle_Libro
from Constantes import constantes # Archivo que contiene dias festivos
import Usuario


class Prestamo(Detalle_Libro, Usuario): # Hereda de las clases Detalle Libro y Usuario
    def __init__(self, isbn, n_identificador, id_prestamo, fecha_prestamo, fecha_entrega, fecha_devolucion, cantidad_solicitada):
        Detalle_Libro.__init__(isbn)
        Usuario.__init__(n_identificador)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.cantidad_solicitada = cantidad_solicitada
        
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo): #Suma dias laborales para devolver la fecha de devolucion
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1
        return fecha_prestamo    
    
    def calcular_fechas(self): # Termina de calcular la fecha de devolucion según el método anterior
        if(self.stock_disponible > 0):
            if(self.stock_disponible > self.cantidad_solicitada):
                self.fecha_prestamo = datetime.datetime.now()
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)
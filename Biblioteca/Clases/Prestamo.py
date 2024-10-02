from datetime import datetime, timedelta
import Detalle_Libro
from Constantes import constantes
import Usuarios


class Prestamo(Detalle_Libro, Usuarios):
    def __init__(self, isbn, n_identificador, id_prestamo, fecha_prestamo, fecha_entrega, fecha_devolucion, cantidad_solicitada):
        Detalle_Libro.__init__(isbn)
        Usuarios.__init__(n_identificador)
        self.id_prestamo = id_prestamo
        self.fecha_prestamo = fecha_prestamo
        self.fecha_entrega = fecha_entrega
        self.fecha_devolucion = fecha_devolucion
        self.cantidad_solicitada = cantidad_solicitada
        
    def sumar_dias_laborales(fecha_prestamo, dias_prestamo):
        dias_agregados = 0  
        while dias_agregados < dias_prestamo:
            fecha_prestamo += timedelta(days=1)
            if fecha_prestamo.weekday() < 5 and fecha_prestamo not in constantes.festivos:
                dias_agregados += 1
        return fecha_prestamo    
    
    def calcular_fechas(self):
        if(self.stock_disponible > 0):
            if(self.stock_disponible > self.cantidad_solicitada):
                self.fecha_prestamo = datetime.datetime.now()
                self.fecha_devolucion = Prestamo.sumar_dias_laborales(self.fecha_prestamo, 5)
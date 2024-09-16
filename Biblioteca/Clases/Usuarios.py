class Usuario:
    def __init__(self,nombre,n_identificador,correo,telefono,habilitado):
        self.__nombre = nombre
        self.__idusuario = n_identificador
        self.__correo = correo
        self.__telefono = telefono
        self.__habilitado = habilitado
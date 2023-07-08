class Usuario:
    
    """
    Clase Usuario
    
    """
    
    
    def __init__(self,nombre="", contrasena="", tipoDeUsuario="", idUsuario=0):
        self.__idUsuario = idUsuario
        self.__nombre = nombre
        self.__contrasena = contrasena
        self.__tipoDeUsuario = tipoDeUsuario
        
        
        """
        Constructor de la clase Usuario
        
        """
        
    def __str__(self):
        return "IdUsuario: " + str(self.__idUsuario) + "\n" + "Nombre: " + self.__nombre + "\n" + "Contrasena: " + self.__contrasena + "\n" + "TipoDeUsuario: " + self.__tipoDeUsuario
    
    """
    Metodo toString de la clase Usuario
    
    """
    
    
    "Setters & Getters"
    
    def getIdUsuario(self):
        return self.__idUsuario
    def setIdUsuario(self, idUsuario):
        self.__idUsuario = idUsuario
    
    
    def getNombre(self):
        return self.__nombre
    def setNombre(self, nombre):
        self.__nombre = nombre
    
    
    def getContrasena(self):
        return self.__contrasena
    def setContrasena(self, contrasena):
        self.__contrasena = contrasena
    
    
    def getTipoDeUsuario(self):
        return self.__tipoDeUsuario
    def setTipoDeUsuario(self, tipoDeUsuario):
        self.__tipoDeUsuario = tipoDeUsuario
        
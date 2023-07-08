class Cliente:
    
    """
        Se crea la clase Cliente
    """
    
    __listaClientes = []
    
    """
        Se crea la lista de clientes
    """
    
    def __init__(self, rut="", razonSocial="", giro="", direccion=""):
        self.__rut = rut
        self.__razonSocial = razonSocial
        self.__giro = giro
        self.__direccion = direccion
        
        """
            Se crea el constructor de la clase Cliente
        """
    
    def __str__(self):
        return "Rut: " + self.__rut + " Razon social: " + self.__razonSocial + " Giro: " + self.__giro + " Direccion: " + self.__direccion
    
    """
        Se crea el metodo toString de la clase Cliente
    """

    "SETTERS & GETTERS"
    
    def setRut(self, rut):
        self.__rut = rut
    def getRut(self):
        return self.__rut
    
    def setRazonSocial(self, razonSocial):
        self.__razonSocial = razonSocial
    def getRazonSocial(self):
        return self.__razonSocial
    
    def setGiro(self, giro):
        self.__giro = giro
    def getGiro(self):
        return self.__giro
    
    def setDireccion(self, direccion):
        self.__direccion = direccion
    def getDireccion(self):
        return self.__direccion
    
    def setListaClientes(self, listaClientes):
        self.__listaClientes = listaClientes
    def getListaClientes(self):
        return self.__listaClientes
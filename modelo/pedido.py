class Pedido():
    
    """
    
    Clase Pedido
    
    """
    
    __listaPedidos = []
    
    """
    
    Lista de pedidos
    
    """
    
    def __init__(self, idPedido=0,rutCliente="",fecha="",tipoDeDocumento="",totalNeto=0,iva=0,totalFinal=0):
        self.__idPedido = idPedido
        self.__rutCliente = rutCliente
        self.__fecha = fecha
        self.__tipoDeDocumento = tipoDeDocumento
        self.__totalNeto = totalNeto
        self.__iva = iva
        self.__totalFinal = totalFinal
        
    """
        Atributos de la clase Pedido
    
    """

    def __str__(self):
        return "ID Pedido: " + str(self.__idPedido) + " Rut Cliente: " + self.__rutCliente + " Fecha: " + self.__fecha + " Tipo de documento: " + self.__tipoDeDocumento + " Total neto: " + str(self.__totalNeto) + " IVA: " + str(self.__iva) + " Total final: " + str(self.__totalFinal)
    
    """
        Metodo toString de la clase Pedido
    
    """

    "SETTERS & GETTERS"
    
    def setIdPedido(self, idPedido):
        self.__idPedido = idPedido
    def getIdPedido(self):
        return self.__idPedido
    
    def setRutCliente(self, rutCliente):
        self.__rutCliente = rutCliente
    def getRutCliente(self):
        return self.__rutCliente
    
    def setFecha(self, fecha):
        self.__fecha = fecha
    def getFecha(self):
        return self.__fecha
    
    def setTipoDeDocumento(self, tipoDeDocumento):
        self.__tipoDeDocumento = tipoDeDocumento
    def getTipoDeDocumento(self):
        return self.__tipoDeDocumento
    
    def setTotalNeto(self, totalNeto):
        self.__totalNeto = totalNeto
    def getTotalNeto(self):
        return self.__totalNeto
    
    def setIva(self, iva):
        self.__iva = iva
    def getIva(self):
        return self.__iva

    def setTotalFinal(self, totalFinal):
        self.__totalFinal = totalFinal
    def getTotalFinal(self):
        return self.__totalFinal
    
    def setListaPedidos(self, listaPedidos):
        self.__listaPedidos = listaPedidos
    def getListaPedidos(self):
        return self.__listaPedidos
    
    def setHabilitado(self, habilitado):
        self.__habilitado = habilitado
    def getHabilitado(self):
        return self.__habilitado
    
    "METODOS"
    
    """
    
    Metodos de la clase Pedido
    
    """
    
    """        
        Revisa si el registro esta habilitado o no
    """
    
    def revisarHabilitado(self):
        return habilitado_global
    
    """
        Habilita el registro
    
    """
    
    
    def habilitarRegistro(self):
        global habilitado_global
        habilitado_global = True
        return habilitado_global
    
    
    """
        Deshabilita el registro
    
    """

    def deshabilitarRegistro(self):
        global habilitado_global
        habilitado_global = False
        return habilitado_global

"""
Se crea la variable global habilitado_global para poder habilitar o deshabilitar el registro
"""

habilitado_global = False
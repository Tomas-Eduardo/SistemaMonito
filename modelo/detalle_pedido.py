from modelo.pedido import Pedido
from modelo.producto import Producto


class DetallePedido(Pedido, Producto):
    
    """
        Clase DetallePedido hereda de las clases Pedido y Producto
    """
    
    def __init__(self, idPedido=0, codigo=0, cantidad=0, totalFinal=0):
        Pedido.__init__(self, idPedido, totalFinal)
        Producto.__init__(self, codigo)
        self.__cantidad = cantidad
        
        """
            Constructor de la clase DetallePedido
        
        """
    
    def __str__(self):
        return "ID Pedido: " + str(self.getIdPedido()) + " Código: " + str(self.getCodigo()) + " Cantidad: " + str(self.__cantidad) + " Total pedido: " + str(self.getTotalPedido())
    
    """
        Método toString de la clase DetallePedido
    """
    
    "SETTERS & GETTERS"
    
    def setCantidad(self, cantidad):
        self.__cantidad = cantidad
    def getCantidad(self):
        return self.__cantidad
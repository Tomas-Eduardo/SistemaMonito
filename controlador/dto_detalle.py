from modelo.detalle_pedido import DetallePedido
from dao.dao_detalle import DaoDetalle

class DetalleDTO:
    
    """
    Clase que permite realizar la validación de un detalle
    """
    
    
    """
    Metodo que permite validar la existencia de un detalle
    """
    def findDetallePedido(self, idPedido):
        daodetalle = DaoDetalle()
        resultado = daodetalle.findDetallePedido(DetallePedido(idPedido=idPedido))
        return resultado
    
    """
    Metodo que permite agregar un detalle
    """
    
    def addDetalle(self, idPedido, listaProductosVenta, listaCantidadProductos, totalPedido):
        daodetalle = DaoDetalle()
        listaCantidadProductos.pop()
        resultado = daodetalle.addDetalle(DetallePedido(idPedido=idPedido), listaProductosVenta, listaCantidadProductos, totalPedido)
        return resultado
    
    def calcularTotal(self, listaProductosVenta, listaCantidadProductos):
        daodetalle = DaoDetalle()
        total = daodetalle.calcularTotal(listaProductosVenta, listaCantidadProductos)
        return total
    
    """
    Metodo eliminar detalle
    """
    def deleteDetalle(self, idPedido):
        daodetalle = DaoDetalle()
        resultado = daodetalle.deleteDetalle(DetallePedido(idPedido=idPedido))
        return resultado
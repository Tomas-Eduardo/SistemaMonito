from modelo.pedido import Pedido
from dao.dao_pedido import daoPedido

class PedidoDTO:
    
    """
    Clase que permite realizar la validación de un pedido
    """
    
    
    """
    Metodo que permite validar la existencia de un pedido
    """
    
    def findIdPedido(self, idPedido):
        daopedido = daoPedido()
        resultado = daopedido.findIdPedido(Pedido(idPedido=idPedido))
        return Pedido(resultado[0]) if resultado is not None else None
    
    
    """
    Metodo que permite validar si la caja esta habilitada
    """
    
    def findHabilitado(self):
        pedido = Pedido()
        resu = pedido.revisarHabilitado()
        if resu == False:
            print("La caja esta cerrada")
            return resu
        else:
            return resu
    
    
    """
    Metodo que permite agregar un pedido
    """
    def addPedido(self, idPedido, rutCliente, fecha, tipoDocumento, valorNeto, iva, totalFinal):
        daopedido = daoPedido()
        if Pedido.revisarHabilitado == False:
            return "El pedido no se puede agregar porque no se ha abierto el día"
        else:
            pedido = Pedido(idPedido=idPedido, rutCliente=rutCliente, fecha=fecha, tipoDeDocumento=tipoDocumento, totalNeto=valorNeto, iva=iva, totalFinal=totalFinal)
            resultado = daopedido.addPedido(pedido)
            return resultado
    
    """
    Metodo que permite buscar los pedidos
    """
    def findVentasDia(self, fecha):
        daopedido = daoPedido()
        resultado = daopedido.findVentasDia(Pedido(fecha=fecha))
        return resultado
    
    """
    Metodo que permite abrir la caja
    """
    
    def abrirCaja(self):
        pedido = Pedido()
        pedido.habilitarRegistro()
        return "Se ha abierto la caja"
    
    """
    Metodo que permite cerrar la caja
    """
    
    def cerrarCaja(self):
        pedido = Pedido()
        pedido.deshabilitarRegistro()
        return "Se ha cerrado la caja"
    
    """
    
    Metodo eliminar pedido
    
    """
    
    def deletePedido(self, idPedido):
        daopedido = daoPedido()
        resultado = daopedido.deletePedido(idPedido)
        return resultado
    
    """
    Metodo buscar todos los pedidos
    """
    
    def allPedidos():
        daopedido = daoPedido()
        resultado = daopedido.allPedidos()
        return resultado
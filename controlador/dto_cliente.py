from modelo.cliente import Cliente
from dao.dao_cliente import daoCliente

class ClienteDTO:
    
    """
    Clase que permite realizar la validación de un cliente
    """
    
    
    """
    Metodo que permite validar la existencia de un cliente
    """
    
    def findRutCliente(self, rutCliente):
        daocliente = daoCliente()
        resultado = daocliente.findRutCliente(Cliente(rut=rutCliente))
        return Cliente(resultado[0]) if resultado is not None else None
    
    """
    Metodo que permite buscar todos los clientes
    """
    
    def findAllCliente():
        daocliente = daoCliente()
        resultado = daocliente.findAllCliente()
        return resultado
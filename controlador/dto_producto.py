from modelo.producto import Producto
from dao.dao_producto import daoProducto

class ProductoDTO:
    
    """
    Clase que permite realizar la validación de un producto
    """
    
    
    """
    Metodo que permite validar la existencia de un producto
    """
    
    def findCodigo(self, codigo):
        daoproducto = daoProducto()
        resultado = daoproducto.findCodigo(Producto(codigo=codigo))
        return Producto(resultado[0]) if resultado is not None else None
    
    """
    Metodo que permite agregar un producto
    """
    
    def addProducto(self, codigo, nombre, valorUnitario):
        daoproducto = daoProducto()
        producto = Producto(codigo=codigo, nombre=nombre, valorUnitario=valorUnitario)
        resultado = daoproducto.addProducto(producto)
        return resultado
    
    """
    Metodo que permite buscar todos los productos
    """
    def findAllProducto():
        daoproducto = daoProducto()
        resultado = daoproducto.allProductos()
        return resultado
    
    """
    Metodo que permite calcular el valor final de un pedido
    """
    
    def calcularPedido(self, listaProductosVenta):
        daoproducto = daoProducto()
        valorNeto = daoproducto.calcPedido(listaProductosVenta)
        return valorNeto
    
    """
    
        Metodo que permite buscar un producto por su codigo
    
    """
    
    def findProducto(self, codigo):
        daoproducto = daoProducto()
        resultado = daoproducto.findProducto(codigo)
        return resultado
    
    """
    
        Metodo que permite modificar producto
    
    """
    
    
    def updateProducto(self, nombre, valorUnitario, codigo):
        daoproducto = daoProducto()
        resultado = daoproducto.updateProducto(codigo, nombre, valorUnitario)
        return resultado
class Producto():
    
    """
    
    Clase Producto
    
    """
    
    def __init__(self, codigo=0, nombre="", valorUnitario=0):
        self.codigo = codigo
        self.nombre = nombre
        self.valorUnitario = valorUnitario
    
    
    """
    
    Constructor de la clase Producto
    
    """
    
    def __str__(self):
        return "Código: " + str(self.codigo) + " Nombre: " + self.nombre + " Valor unitario: " + str(self.valorUnitario)
    
    
    """
    
    Método toString de la clase Producto
    
    """
    
    "SETTERS & GETTERS"
    
    def setCodigo(self, codigo):
        self.codigo = codigo
    def getCodigo(self):
        return self.codigo
    
    def setNombre(self, nombre):
        self.nombre = nombre
    def getNombre(self):
        return self.nombre
    
    def setValorUnitario(self, valorUnitario):
        self.valorUnitario = valorUnitario
    def getValorUnitario(self):
        return self.valorUnitario
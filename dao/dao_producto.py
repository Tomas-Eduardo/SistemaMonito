from conex import conn
import traceback
from tabulate import tabulate

class daoProducto:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "monitodb")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    def getConex(self):
        return self.__conn
    
    """
        Clase que permite realizar la validación de un producto
    """
    
    """
        Metodo que permite validar la existencia de un producto
    """
    
    def findCodigo(self, codigo):
        sql = "SELECT codigo FROM producto where codigo = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (codigo.getCodigo(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    """
        Metodo que permite agregar un producto
    """
    
    def addProducto(self, codigo):
        sql = "INSERT INTO producto (codigo, nombre, valor_unitario, stock) VALUES (%s, %s, %s, 999)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (codigo.getCodigo(), codigo.getNombre(), codigo.getValorUnitario()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Producto agregado sastifactoriamente"
            else:
                mensaje = "No se pudo agregar el producto"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos... vuelve a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    """
        Metodo que permite mostrar todos los productos
    """
    
    def allProductos(self):
        sql = "SELECT * FROM producto"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()

            headers = [i[0] for i in cursor.description]
            tabla = tabulate(resultado, headers=headers, tablefmt="fancy_grid")
            print(tabla)
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    
    """
        Metodo que permite calcular el valor total de un pedido
    """

    def calcPedido(self, listaProductosVenta):
        sql = "SELECT SUM(valor_unitario) FROM producto WHERE codigo IN (%s)"
        marcadores = ', '.join(['%s'] * len(listaProductosVenta))
        sql = sql % marcadores
        valores = tuple(listaProductosVenta)
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, valores)
            resultado = cursor.fetchone()[0]  # Obtener el primer valor directamente
        except Exception as ex:
            print(traceback.print_exc(ex))
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    """
    
        Metodo que permite buscar un producto por su codigo
    
    """
    
    def findProducto(self, codigo):
        sql = "SELECT * FROM producto WHERE codigo = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (codigo,))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    
    """
        Metodo para modificar un producto
    
    """
    
    def updateProducto(self, codigo, nombre, valorUnitario):
        sql = "UPDATE producto SET nombre = %s, valor_unitario = %s WHERE codigo = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (nombre, valorUnitario, codigo))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Producto modificado satisfactoriamente"
            else:
                mensaje = "No se pudo modificar el producto"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos... vuelve a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje

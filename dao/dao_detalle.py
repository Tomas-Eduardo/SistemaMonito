from conex import conn
import traceback

class DaoDetalle:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "monitodb")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    def getConex(self):
        return self.__conn
        
        
    
    """
    Clase que permite realizar la validación de un detalle
    """
    
    """
    Metodo que permite validar la existencia de un detalle
    """
    
    def findDetallePedido(self, idPedido):
        sql = """
            SELECT dp.codigo_producto, dp.cantidad, p.nombre, p.valor_unitario, (p.valor_unitario * dp.cantidad) AS total
            FROM detalle_pedido dp
            JOIN producto p ON dp.codigo_producto = p.codigo
            WHERE dp.id_pedido = %s
        """
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (idPedido.getIdPedido(),))
            resultado = cursor.fetchall()
            for row in resultado:
                codigo_producto = row[0]
                cantidad = row[1]
                nombre_producto = row[2]
                valor_unitario = row[3]
                total = row[4]
                print(f"Producto: {nombre_producto}, Cantidad: {cantidad}, Codigo de Producto: {codigo_producto}, Precio: {valor_unitario}, Total: {total}")
                print("------------------------------------------------------------------------------------------")
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado


    """
    Metodo que permite agregar un detalle
    """
    
    def addDetalle(self, idPedido, listaProductosVenta, listaCantidadProductos, totalPedido):
        sql = "INSERT INTO detalle_pedido (id_pedido, codigo_producto, cantidad, total_producto) VALUES (%s, %s, %s, %s)"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            for i in range(len(listaProductosVenta)):
                cursor.execute(sql, (idPedido.getIdPedido(), listaProductosVenta[i], listaCantidadProductos[i], totalPedido))
            c.getConex().commit()
            resultado = True
        except Exception as ex:
            print(traceback.print_exc())
            resultado = False
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    def calcularTotal(self, listaProductosVenta, listaCantidadProductos):
        valorNeto = 0
        iva = 0
        total = 0
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            for i in range(len(listaProductosVenta)):
                sql = "SELECT valor_unitario FROM producto WHERE codigo = %s"
                cursor.execute(sql, (listaProductosVenta[i],))
                valor_unitario = cursor.fetchone()[0]
                subtotal = valor_unitario * listaCantidadProductos[i]
                valorNeto += subtotal
            iva = valorNeto * 0.19
            total = valorNeto + iva
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return valorNeto, iva, total

    
    """
    Metodo eliminar detalle
    """
    
    def deleteDetalle(self, idPedido):
        sql = "DELETE FROM detalle_pedido WHERE id_pedido = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (idPedido.getIdPedido(),))
            c.getConex().commit()
            resultado = True
        except Exception as ex:
            print(traceback.print_exc())
            resultado = False
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
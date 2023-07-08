from conex import conn
import traceback
from tabulate import tabulate

class daoPedido:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "monitodb")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    def getConex(self):
        return self.__conn
    
    
    """
    Clase que permite realizar la validación de un pedido
    """
    
    """
    Metodo que permite validar la existencia de un pedidoS
    """
    
    def findIdPedido(self, idPedido):
        sql = "SELECT id_pedido FROM pedido WHERE id_pedido = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (idPedido.getIdPedido(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    """
    Metodo que permite agregar un pedido
    """
    
    def addPedido(self, pedido):
        sql = "INSERT INTO pedido (id_pedido, rut_cliente, fecha, tipo_documento, total_neto, iva,total_final) VALUES (%s, %s, %s, %s,%s,%s,%s)"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (pedido.getIdPedido(), pedido.getRutCliente(), pedido.getFecha(), pedido.getTipoDeDocumento(), pedido.getTotalNeto(), pedido.getIva(), pedido.getTotalFinal()))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Pedido agregado sastifactoriamente"
            else:
                mensaje = "No se pudo agregar el pedido"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos... vuelve a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    """
    Metodo que permite buscar un pedido
    """
    
    def findVentasDia(self, fecha):
        sql = "SELECT * FROM pedido WHERE fecha = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (fecha.getFecha(),))
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
    Metodo eliminar un pedido
    """
    
    def deletePedido(self, idPedido):
        sql = "DELETE FROM pedido WHERE id_pedido = %s"
        c = self.getConex()
        mensaje = ""
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (idPedido,))
            c.getConex().commit()
            filas = cursor.rowcount
            if filas > 0:
                mensaje = "Pedido eliminado sastifactoriamente"
            else:
                mensaje = "No se pudo eliminar el pedido"
        except Exception as ex:
            print(traceback.print_exc())
            mensaje = "Problemas con la base de datos... vuelve a intentarlo"
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return mensaje
    
    """
    Metodo que permite buscar todos los pedidos
    """
    
    def allPedidos(self):
        sql = "SELECT * FROM pedido"
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
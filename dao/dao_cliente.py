from conex import conn
import traceback
from tabulate import tabulate

class daoCliente:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "monitodb")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    def getConex(self):
        return self.__conn
    
    
    """
    Clase que permite realizar la validación de un cliente
    """
    
    
    """
    Metodo que permite validar la existencia de un cliente
    """
    def findRutCliente(self, rutCliente):
        sql = "SELECT rut FROM cliente WHERE rut = %s"
        resultado = None
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql,(rutCliente.getRut(),))
            resultado = cursor.fetchone()
        except Exception as ex:
            print(traceback.print_exc())
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
    
    """
    Metodo que permite buscar todos los clientes
    """
    
    def findAllCliente(self):
        sql = "SELECT * FROM cliente"
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
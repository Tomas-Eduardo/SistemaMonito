from conex import conn
import traceback

class daoUsuario:
    def __init__(self):
        try:
            self.__conn = conn.Conex("localhost", "root", "", "monitodb")
        except Exception as e:
            print(e)
            traceback.print_exc()
    
    def getConex(self):
        return self.__conn
    
    """
        Clase que permite realizar la validación de un usuario
    """
    
    """
        Metodo que permite validar la existencia de un usuario para el login
    """
    
    def validarLogin(self, resultado):
        sql = "SELECT nombre, contraseña,tipo_usuario FROM usuario WHERE nombre = %s AND contraseña = %s"
        c = self.getConex()
        try:
            cursor = c.getConex().cursor()
            cursor.execute(sql, (resultado.getNombre(), resultado.getContrasena()))
            
            resultado = cursor.fetchone()
        except Exception as e:
            print(e)
            traceback.print_exc()
        finally:
            if c.getConex().is_connected():
                c.closeConex()
        return resultado
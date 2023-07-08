import mysql.connector

class Conex:
    
    """
    Clase que permite realizar la conexión a la base de datos
    """

    def __init__(self,  host, user, passwd, database):
        try:
            self.__myconn = mysql.connector.connect(host=host, \
                                             user=user, \
                                             passwd=passwd, \
                                             database=database)
        except Exception as ex:
            print(ex)
            self.__myconn.rollback()
            return None


    """
    Metodo que permite cerrar la conexión a la base de datos
    """
    def closeConex(self):
        self.__myconn.close()

    """
    Metodo que permite obtener la conexión a la base de datos
    """

    def getConex(self):
        return self.__myconn
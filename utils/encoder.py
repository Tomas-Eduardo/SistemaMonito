import hashlib

class Encoder:
    
    """
    Clase que permite realizar la codificación y decodificación de una cadena
    """


    """
    Metodo que permite codificar una cadena
    """
    def encode(self, string):

        result = hashlib.md5(string.encode())
        return result.hexdigest()

    """
    Metodo que permite decodificar una cadena
    """
    def decode(self, string, claveMD5):

        if hashlib.md5(string.encode()).hexdigest() == claveMD5:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Encoder().encode("666"))
from modelo.usuario import Usuario
from utils.encoder import Encoder
from dao.dao_usuario import daoUsuario

class UsuarioDTO:
    
    """
    Clase que permite realizar la validación de un usuario
    """
    
    
    """
    Metodo que permite validar el login de un usuario
    """
    
    def validarLogin(self, nombre, contrasena):
        daousuario = daoUsuario()
        resultado = daousuario.validarLogin(Usuario(nombre=nombre, contrasena=Encoder().encode(contrasena)))
        return resultado
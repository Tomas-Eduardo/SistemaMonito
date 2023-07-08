from controlador.dto_usuario import UsuarioDTO
from controlador.dto_producto import ProductoDTO
from controlador.dto_pedido import PedidoDTO
from controlador.dto_cliente import ClienteDTO
from controlador.dto_detalle import DetalleDTO
from datetime import datetime


"""
    Realiza el proceso de validación de inicio de sesión.

    Esta función presenta un menú de opciones para iniciar sesión o salir.
    Solicita al usuario ingresar un nombre de usuario y una contraseña.
    Luego, realiza la validación de las credenciales ingresadas y determina el tipo de usuario (Vendedor o Jefe de Ventas).
    Si las credenciales son válidas, se muestra el menú correspondiente al tipo de usuario y se retorna el resultado.
    Si se selecciona la opción de salir, se retorna False.
    Si se ingresa una opción inválida, se muestra un mensaje de error y se solicita ingresar nuevamente.

    Returns:
        - Si se inicia sesión correctamente:
            (tuple) Una tupla que contiene la información del usuario logueado.
                La tupla tiene la siguiente estructura: (nombre, contrasena, tipo_usuario).
                - nombre (str): El nombre del usuario logueado.
                - contrasena (str): La contraseña del usuario logueado.
                - tipo_usuario (str): El tipo de usuario (Vendedor o Jefe de Ventas).
        - Si se selecciona la opción de salir:
            (bool) False.
    """

def validarLogin():
    while True:
        opcion = input("1. Iniciar sesión\n2. Salir\nIngrese una opción: ")
        if opcion == "1":
            nombre = input("Ingrese nombre de usuario: ")
            contrasena = input("Ingrese contraseña: ")
            try:
                resultado = UsuarioDTO().validarLogin(nombre, contrasena)
                if resultado[2] == "Vendedor":
                    "AQUI COMIENZA EL MENU RESPECTIVO DE VENDEDOR"
                    inicialVendedor()
                    return resultado
                if resultado[2] == 'Jefe de Ventas':
                    "AQUI COMIENZA EL MENU RESPECTIVO DE JEFE DE VENTAS"
                    inicialJefe()
                    return resultado
            except:
                print("Ingrese un número válido")
        elif opcion == "2":
            return False
        else:
            print("Opción inválida. Intente de nuevo.")
    

"Funciones Vendedor"

"""
    Realiza el proceso de venta de productos.

"""

def validateRealizarVenta():
    try:
        resu = PedidoDTO().findHabilitado()
        if resu == False:
            print("Debes abrir la caja para realizar una venta")
            input("Presione enter para continuar")
            return inicialVendedor()
        else:
            idPedido = int(input("Ingrese id del pedido: "))
            if idPedido is str:
                print("Ingrese un id válido")
            resu = PedidoDTO().findIdPedido(idPedido)
            if resu is not None:
                print("El id ya existe, ingrese otro")
                return validateRealizarVenta()
            print("----- CLIENTES REGISTRADOS -----")
            ClienteDTO.findAllCliente()
            rutCliente = str(input("Ingrese rut del cliente: "))
            resu = ClienteDTO().findRutCliente(rutCliente)
            if resu is None:
                print("El rut no existe, ingrese otro")
                return validateRealizarVenta()
            print("----- DETALLE DE PRODUCTOS -----")
            ProductoDTO.findAllProducto()
            listaProductosVenta = []
            listaCantidadProductos = []
            idVenta = 1
            
            while idVenta != 0:
                try:
                    idVenta = int(input("Ingresa el ID del producto a agregar (Digita 0 para no agregar más productos): "))
                    if idVenta > 0:
                        resu = ProductoDTO().findCodigo(idVenta)
                        cantidad = int(input("Ingresa la cantidad del producto: "))
                        if cantidad <= 0:
                            print("La cantidad debe ser mayor a 0")
                            return validateRealizarVenta()
                    if resu is None:
                        print("El ID no existe, ingrese otro")
                    else:
                        listaCantidadProductos.append(cantidad)
                        listaProductosVenta.append(idVenta)
                    if idVenta == 0:
                        listaProductosVenta.pop()
                except Exception as e:
                    print(e)
            print("Selecciona que tipo de documento deseas: ")
            print("1. Boleta")
            print("2. Factura")
            tipoDocumento = int(input(""))
            if tipoDocumento == 1:
                tipoDocumento = "Boleta"
            elif tipoDocumento == 2:
                tipoDocumento = "Factura"
            else:
                print("Ingrese una opción válida")
                return validateRealizarVenta()
            
            "Ingresar funcion, traer valor neto y valor iva"
            """valorNeto = ProductoDTO().calcularPedido(listaProductosVenta)
            iva = float(valorNeto) * 0.19"""
            "totalFinal = float(valorNeto) + iva"
            
            
            "Calcular valor neto, iva y total"
            valorNeto, iva, totalFinal = DetalleDTO().calcularTotal(listaProductosVenta, listaCantidadProductos)
            
            "Ingresar funcion, traer fecha actual"
            now = datetime.now()
            format = now.strftime('%Y-%m-%d')
            
            print("----- DETALLE DE LA VENTA -----")
            print("ID Pedido: " + str(idPedido))
            print("Rut Cliente: " + str(rutCliente))
            print("Fecha: " + (format))
            print("Tipo de documento: " + str(tipoDocumento))
            print("Valor neto: " + str(valorNeto))
            print("IVA: " + str(iva))
            print("Total: " + str(totalFinal))
            conf = input("¿Desea confirmar la venta? (s/n)")
            if conf == "s":
                "Metodo para agregar pedido"
                PedidoDTO().addPedido(idPedido, rutCliente, format, tipoDocumento, valorNeto, iva, totalFinal)
                "Metodo guardar detalles pedido"
                DetalleDTO().addDetalle(idPedido, listaProductosVenta, listaCantidadProductos, totalFinal)
                return inicialVendedor()
            else:
                return inicialVendedor()
    except Exception as e:
        print(e)

"Funciones Jefe de Ventas"

"""

    Realiza el proceso de añadir un nuevo producto.
    

"""


def validateAddProducto():
    try:
        codigo = int (input("Ingrese código del producto: "))
        if codigo is str:
            print("Ingrese un código válido")
        resu = ProductoDTO().findCodigo(codigo)
        if resu is not None:
            print("El código ya existe, ingrese otro")
            return validateAddProducto()
        nombre = input("Ingrese nombre del producto: ")
        if len(nombre) == 0:
            print("Debe ingresar un nombre")
        valorUnitario = int(input("Ingrese valor unitario del producto: "))
        if valorUnitario is str:
            print("Ingrese un valor válido")
        print(ProductoDTO().addProducto(codigo, nombre, valorUnitario))
        otro = input("¿Desea agregar otro producto? (s/n): ")
        if otro == "s":
            return validateAddProducto()
        else:
            return inicialJefe()
    except:
        print("Ingrese un valor valido")
        

"""

    Realiza el proceso de generar las ventas del día.


"""

def validateVentasDia():
    try:
        opc = input("¿Desea ver las ventas de hoy? (s/n): ")
        if opc == "s":
            date = datetime.now()
            format = date.strftime('%Y-%m-%d')
            PedidoDTO().findVentasDia(format)
            input("Presione enter para continuar: ")
            return inicialJefe()
        elif opc == "n":
            fecha = input("Ingrese fecha (YYYY/MM/DD): ")
            PedidoDTO().findVentasDia(fecha)
            input("Presione enter para continuar: ")
            return inicialJefe()
    except:
        print("Ingrese una fecha válida")
        
"""

    Muestra el detalle de un pedido.
    

"""

def validateFindDetallePedido():
    try:
        idPedido = int(input("Ingrese id del pedido: "))
        if idPedido is str:
            print("Ingrese un id válido")
        resu = PedidoDTO().findIdPedido(idPedido)
        if resu is None:
            print("El id no existe, ingrese otro")
            return validateFindDetallePedido()
        print("----- DETALLE DEL PEDIDO -----")
        DetalleDTO().findDetallePedido(idPedido)
        input("Presione enter para continuar: ")
        return inicialJefe()
    except:
        print("Ingrese un id válido")

"""

    Realiza el proceso de apertura de caja.


"""

def validateAperturaDia():
    pedidoDTO = PedidoDTO()
    pedidoDTO.abrirCaja()
    print("Caja abierta")
    input("Presione enter para continuar: ")
    return inicialJefe()

"""

    Realiza el proceso de cierre de caja.

"""

def validateCerrarDia():
    pedidoDTO = PedidoDTO()
    pedidoDTO.cerrarCaja()
    print("Caja cerrada")
    input("Presione enter para continuar: ")
    return inicialJefe()

"""

    Realiza el proceso de modificar un producto.

"""

def validateUpdateProducto():
    try:
        ProductoDTO.findAllProducto()
        codigo = int(input("Ingrese código del producto: "))
        if codigo is str:
            print("Ingrese un código válido")
        resu = ProductoDTO().findProducto(codigo)
        print(resu)
        if resu is None:
            print("El código no existe, ingrese otro")
            return validateUpdateProducto()
        nombre = input("Ingrese nombre del producto: ")
        if len(nombre) == 0:
            print("Debe ingresar un nombre")
        valorUnitario = int(input("Ingrese valor unitario del producto: "))
        print(valorUnitario)
        if valorUnitario is str:
            print("Ingrese un valor válido")
        print(ProductoDTO().updateProducto(nombre, valorUnitario, codigo))
        otro = input("¿Desea modificar otro producto? (s/n): ")
        if otro == "s":
            return validateUpdateProducto()
        else:
            return inicialJefe()
    except Exception as e:
        print(e)
    
    
"""

    Realiza el proceso de eliminar un pedido.
    
"""

def validateDeletePedido():
    try:
        PedidoDTO.allPedidos()
        idPedido = int(input("Ingrese id del pedido: "))
        if idPedido is str:
            print("Ingrese un id válido")
        resu = PedidoDTO().findIdPedido(idPedido)
        if resu is None:
            print("El id no existe, ingrese otro")
            return validateDeletePedido()
        print("----- DETALLE DEL PEDIDO -----")
        DetalleDTO().findDetallePedido(idPedido)
        conf = input("¿Desea eliminar el pedido? (s/n): ")
        if conf == "s":
            DetalleDTO().deleteDetalle(idPedido)
            PedidoDTO().deletePedido(idPedido)
            print("Pedido eliminado")
            input("Presione enter para continuar: ")
            return inicialJefe()
        else:
            return inicialJefe()
    except Exception as e:
        print(e)

"MENUS CRUD"

"""

    Muestra el menú de opciones

"""

def mostrar_menu(opciones):
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}. {opcion}")
    opc = int(input("Ingrese una opción: "))
    return opc

"""

    Muestra el menú de opciones para el jefe de ventas

"""


def inicialJefe():
    while True:
        try:
            print("----- MENU JEFE DE VENTAS -----")
            opciones = [
                "Agregar productos al inventario",
                "Obtener ventas del día",
                "Apertura del día",
                "Cierre del día",
                "Buscar pedido",
                "Modificar producto",
                "Eliminar pedido",
                "Cerrar sesión"
            ]
            opc = mostrar_menu(opciones)
            if opc == 1:
                while True:
                    validateAddProducto()
            elif opc == 2:
                while True:
                    validateVentasDia()
            elif opc == 3:
                while True:
                    validateAperturaDia()
            elif opc == 4:
                while True:
                    validateCerrarDia()
            elif opc == 5:
                while True:
                    validateFindDetallePedido()
            elif opc == 6:
                while True:
                    validateUpdateProducto()
            elif opc == 7:
                while True:
                    validateDeletePedido()
            elif opc == 8:
                while True:
                    validarLogin()
        except Exception as e:
            print("Ocurrió un error:", str(e))
            return inicialJefe()


"""

    Muestra el menú de opciones para el vendedor

"""


def inicialVendedor():
    while True:
        try:
            print("----- MENU VENDEDOR -----")
            opciones = [
                "Realizar venta",
                "Cerrar sesión"
            ]
            opc = mostrar_menu(opciones)
            if opc == 1:
                while True:
                    validateRealizarVenta()
            elif opc == 2:
                validarLogin()
        except Exception as e:
            print("Ocurrió un error:", str(e))
            return inicialVendedor()
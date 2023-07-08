# Entrega Final Taller de Desarrollo de Aplicaciones Inacap 2023

El bazar “Los monitos de la Nona”, requiere para poder comenzar a operar un sistema que le permita registrar las ventas del día y emitir las boletas o facturas, a los clientes que visitan el local.
Dentro de las necesidades planteadas por la dueña de dicha librería se esperan los siguientes requerimientos de usuario.
1.	Poder agregar productos a ser adquiridos por un potencial cliente, detallándose:
  a.	Cantidad.
  b.	Nombre del producto.
  c.	Código del producto.
  d.	Valor unitario.
  e.	Total por producto (cantidad * costo unitario).
2.	Se deberá poder agregar más de un tipo de producto a una venta, y se deberá calcular el total a ser cancelado por el cliente.
3.	Deberá considerar el valor del IVA al 19%.
4.	De generarse una factura, esta deberá solicitar:
  a.	Razón social del cliente.
  b.	RUT del cliente.
  c.	Giro.
  d.	Dirección.
  e.	Detalle de productos, separando total neto, IVA (19%), total final (neto + IVA).
5.	De generarse una boleta por la venta, esta deberá considerar:
  a.	Detalle de productos.
  b.	Cantidades.
  c.	Total a pagar.
6.	Inicialmente el proyecto, no contará con un sistema de inventario desde donde obtener las cantidades reales de productos en bodega, se deberá trabajar con un inventario infinito.
7.	Existe un jefe de ventas que puede:
  a.	Agregar productos al inventario.
  b.	Obtener las ventas del día, separándose las ventas con boleta de las que son con factura.
8.	En este sistema inicial, no se consideran los medios de pago. Se asume que el flujo termina cuando se genera el documento tributario (boleta o factura).
9.	El vendedor es un usuario distinto al jefe de ventas.
10.	El usuario vendedor, solo puede generar ventas (indistinto del tipo de documento tributario).
11.	Se deberá almacenar toda venta generada por sistema, y esta deberá consolidarse en un informe de ventas del día.
12.	Se deberá contar con una opción de cierre de día, en donde se consolidarán las ventas generadas ese día en particular y no será posible agregar más ventas a ese día.
  a.	Esta opción deberá tenerla el jefe de ventas.
13.	Se deberá contar con una opción de apertura de día, que permita comenzar a vender productos en el local.
  a.	No se podrán generar ventas si no existe un día abierto.
  b.	Esta opción es solo para el jefe de ventas.
14.	Se deberá poder buscar productos para agregar a la venta a través de un código de barras (SKU) o nombre del producto.
  a.	Una vez encontrado, deberá ser posible agregar la cantidad deseada de productos a la venta.
15.	Cada una de las ventas deberá tener un identificador único dentro del sistema, en versiones superiores existirá la opción de buscar una venta específica.
16.	El documento tributario deberá desplegar una pantalla o documento PDF en donde sea posible apreciar la vista previa de éste (no es necesario implementar la funcionalidad de impresión, solo es necesaria la vista previa).
17.	El informe de ventas del día (visible sólo para el jefe de ventas), deberá indicar:
  a.	Cantidad de ventas con boleta.
  b.	Cantidad de dinero por ventas con boleta, separando valor neto, IVA y total (neto + IVA).
  c.	Número de facturas generadas:
i.	Por cada factura se deberá detallar:
  1.	Número de factura.
  2.	Valor en dinero, separando neto, IVA y total (neto + IVA).
  d.	El informe de ventas es de un día en particular, y deberá ser posible buscar informes de cualquier día que tenga ventas.
18.	Para el ingreso al sistema se deberá contar con usuario y contraseña, y éste deberá identificar el tipo de usuario que está ingresando (vendedor o jefe de ventas) y desplegar las opciones correspondientes.
  a.	No podrá un vendedor tener opciones de jefe de venta o viceversa.
19.	Un jefe de venta no puede generar ventas.
20.	En el informe de ventas, se deberá identificar al vendedor que estuvo trabajando en el día.
21.	Se deberá proveer una opción para filtrar los informes de ventas por vendedor, listando sólo los días que dicho vendedor trabajó o generó ventas efectivamente.
  a.	No deberán aparecer en el listado días donde el vendedor no trabajó o no realizó ventas.

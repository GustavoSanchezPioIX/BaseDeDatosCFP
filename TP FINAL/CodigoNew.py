import  sqlite3
from cte import *

#bd = sqlite3.connect("C:/Users/User/Desktop/baseDeDatos/LISTACOMPRAS.db")
#bd = sqlite3.connect("C:/Users/gusta/Desktop/rar/LISTACOMPRAS.db")
bd = sqlite3.connect("C:/Users/User/Desktop/bd/LISTACOMPRAS.db")
c = bd.cursor()

def OpcionElegida(menu):
    opcion = int(input("Ingresar Opcion Elegida: "))
    print(" ")
    if opcion in menu:
        menu[opcion]()
        valor = True
        print(" ")
    else:
        print("Eligio salir")
        valor = False
    return valor

def AltaProveedor():
    nombre = input("Ingresar Nombre Proveedor: ").upper()
    rubro = input("Ingresar rubro: ").upper()
    telefono = int(input("Ingresar numero Telefonico: "))
    direccion = input("Direccion: ").upper()

    print("Se da de alta a {}".format(nombre))
    c.execute(SQL_ALTA_PROVEEDOR.format(nombre, rubro, telefono, direccion))
    bd.commit()

def MostrarSector():
    print("Mostrara todos los datos de la tabla Tipos de Compras")
    c.execute(SQL_TIPO_TOTAL)
    resp = c.fetchall()
    for i in resp:
        print('{} - {} '.format(i[0],i[1]))

def AltaTipoCompra():
    nombre = input("Sector de Compra: ").upper()
    c.execute(SQL_REGISTRAR_TIPO.format(nombre))
    bd.commit()

def BajaTipoCompra():
    print("Tabla de Tipos de Compras")
    MostrarSector()
    idTipo = input("ID Sector de Compra: ".upper())
    c.execute(SQL_BORRAR_TIPO.format(idTipo))
    bd.commit()

def SubirCompra():
    resp = True
    while resp:
        fecha = input("Ingrese fecha: ")
        facturaNum = input("Ingrese numero de factura: ")
        MostrarProveedorXrubro()
        IdProveedor = input("ID de Proveedor: ")
        precioFinal = input("Precio Final: $")
        MostrarSector()
        IdTipo = input("Id de Tipo de compra: ")
        descripcion = input("Descripcion de articulo comprado: ").upper()
        c.execute(SQL_SUBIR_COMPRA.format(fecha,facturaNum,IdProveedor,precioFinal,IdTipo,descripcion))
        bd.commit()
        comfirmar = input("Quiere volver a subir mas compras?".upper())
        if not comfirmar == "SI":
            resp = False

def BajaProveedor():
    nombre = input("Ingrese el nombre del proveedor que quiere dar de baja: ").upper()
    c.execute(SQL_BAJA_PROVEEDOR.format(nombre))
    bd.commit()

def BajaCompra():
    idCompra = int(input("Seleccione ID de la compra que quiera borrar: "))
    c.execute(SQL_BAJA_COMPRA.format(idCompra))
    bd.commit()
    print("Se borro una compra de IP n°{}".format(idCompra))

def MostrarCompraXsector():
    print("Que sector quiere filtrar?")
    tipo = int(input("Sector ID de compra es: "))
    c.execute(SQL_MOSTRAR_TIPO.format(tipo))
    resp = c.fetchall()
    for i in resp:
        print('{} - {} - {} - {} - {} - {} - {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

def MostrarCompraXproveedor():
    proveedor = int(input("ID de proveedor: "))
    c.execute(SQL_COMPRA_PROVEEDOR.format(proveedor))
    resp = c.fetchall()
    for i in resp:
        print('{} - {} - {} - {} - {} - {} - {}'.format(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))

def MostrarProveedorXrubro():
    rubro = input("Que tipo de Proveedor busca? Elija un Rubro: ").upper()
    c.execute(SQL_PROVEEDOR_RUBRO.format(rubro))
    resp = c.fetchall()
    print("LISTA DE PROVEEDORES POR RUBRO ELEGIDO")
    print("ID - NOMBRE")
    for i in resp:
        print(' {} - {}'.format(i[0],i[1]))

def MostrarCompras():
    print("Todas las compras realizadas hasta la fecha")
    c.execute(SQL_COMPRAS_TOTAL)
    resp = c.fetchall()
    for i in resp:
        print('{} - {} - {} - {} - {} - {} - {}'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6]))

def MostrarProveedor():
    print("Se mostraran todos los proveedores")
    c.execute(SQL_PROVEEDOR_TOTAL)
    resp = c.fetchall()
    for i in resp:
        print('{} - {} - {} - {} - {}'.format(i[0],i[1],i[2],i[3],i[4]))

def ModificarCompras():
    lista = ("FECHA","ID","FACTURA_N°","ID_PROVEEDOR","PRECIO_FINAL","ID_TIPO","DESCRIPCION")

    print("Se le mostrara las compras que puede modificar")
    MostrarCompras()
    print(lista)
    numColumna = int(input("Ingrese el numero de columna que quiere modificar "))-1
    print("Quiere modificar en la columna: {}".format(lista[numColumna]))
    idDatoAmodificar = int(input("Numero de fila: "))
    datoNuevo = str(input("Que dato quiere ingresar en {} fila N°{} ?".format(lista[numColumna],idDatoAmodificar)))
    c.execute(SQL_MODIFICAR_COMPRA.format(lista[numColumna],datoNuevo,idDatoAmodificar))
    bd.commit()

def ModificarProveedor():
    campos = ("ID_PROV","NOMBRE","RUBRO","TELEFONO","DIRECCION")
    print("Tabla de Proveedores")
    MostrarProveedor()
    print(campos)
    numColumna = int(input("Ingrese el numero de columna que quiere modificar ")) - 1
    print("Quiere modificar en la columna: {}".format(campos[numColumna]))
    idDatoAmodificar = int(input("Numero de fila: "))
    datoNuevo = str(input("Que dato quiere ingresar en {} fila N°{} ?".format(campos[numColumna], idDatoAmodificar)))
    c.execute(SQL_MODIFICAR_PROVEEDOR.format(campos[numColumna],datoNuevo,idDatoAmodificar))

def ComprasAcciones():
    diccionarioAcciones = {1 : SubirCompra,
                           2 : BajaCompra,
                           3 : MostrarCompras,
                           4 : ModificarCompras}
    valor = True
    while valor:
        print("1 - Subir Compra\n"
              "2 - Bajar Compra\n"
              "3 - Mostrar Compras\n"
              "4 - Modificar Compras\n"
              "5 (o distinto) - Salir del menu")
        valor = OpcionElegida(diccionarioAcciones)

def ProveedorAcciones():
    diccionarioAcciones = {1 : AltaProveedor,
                           2 : BajaProveedor,
                           3 : MostrarProveedor,
                           4 : ModificarProveedor}
    valor = True
    while valor:
        print("1 - Alta Proveedor\n"
              "2 - Baja Proveedor\n"
              "3 - Mostrar Proveedor\n"
              "4 - Modificar Proveedor\n"
              "5 (o distinto) - Salir")
        valor = OpcionElegida(diccionarioAcciones)

def TiposDeComprasAcciones():
    acciones = {1 : AltaTipoCompra,
                2 : BajaTipoCompra,
                3 : MostrarSector}
    valor = True
    while valor:
        print("1 - Cargar nuevo sector de Compra\n"
              "2 - Borrar Sector de Compra \n"
              "3 - Mostrar Sector\n"
              "4 (o distinto) - Salir")
        valor = OpcionElegida(acciones)


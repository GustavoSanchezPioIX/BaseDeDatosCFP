import  sqlite3

bd = sqlite3.connect("C:/Users/gusta/Desktop/EjerciciosDB/PLANILLADECOMPRAS.db")
c = bd.cursor()

def AltaProveedor ():
    nombre = input("Ingresar Nombre Proveedor: ").upper()
    telefono = int(input("Ingresar numero Telefonico: "))
    rubro = input("Ingresar rubro: ").upper()
    direccion = input("Direccion: ").upper()


    print("Se da de alta a {}".format(nombre))
    c.execute('INSERT INTO PROVEEDORES (NOM_PROV, TELEFONO, RUBRO, DIRECCION) VALUES ("{}",{},"{}","{}");'.format(nombre,telefono,rubro,direccion))
    bd.commit()

def AltaArticulosComprados():
    tipoArticulo = input("Sector al que pertenece la compra: ").upper()
    nombreArticulo = input("Nombre articulo: ").upper()
    unidades = input("Cuantas unidades se compro: ")
    c.execute('INSERT INTO ARTICULOS (TIPOS_ART, NOMBRE, CANTIDAD) VALUES ("{}","{}",{});'.format(tipoArticulo, nombreArticulo, unidades))
    bd.commit()

def CompraPrincipal():
    id_Proveedor = input("ID de Proveedor: ")
    tipoCompra = input("Sector de compra destinada: ").upper()
    numFactura = input("Numero de factura: ")
    precioFinal = input("Precio Final: ")
    c.execute('INSERT INTO COMPRAS_PRINCIPAL (PROVEEDOR_COMPRA, TIPO_COMPRA, FACTURA, PRECIO_FINAL) VALUES ({},"{}",{},{});'
              .format(id_Proveedor,tipoCompra,numFactura,precioFinal))
    bd.commit()

CompraPrincipal()
"""
altaProveedor ()
altaVerdad = input("Quiere dar de alta un articulo? V o F ").upper()
if altaVerdad == "V":
    AltaArticulosComprados()
else:
    print("No se dio de alta nada")

respuestaProveedor = input("Quiere dar de alta algun proveedor? V o F ").upper()
if respuestaProveedor == "V":
    AltaProveedor()
else:
    print("No se dio de alta ningun proveedor")
"""

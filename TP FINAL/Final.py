from CodigoNew import *

funciones = {"1": ComprasAcciones,
             "2": ProveedorAcciones,
             "3": TiposDeComprasAcciones}
def MenuPrincipal():
    respMenu = True
    while respMenu:
        print("Menu de Opciones:  \n"
              "1 - Compras \n" 
              "2 - Proveedor \n"
              "3 - Tipo\n"
              "4 - Salir")
        opcion = str(input("Ingresar opcion: "))
        print(" ")

        if opcion in funciones:
            funciones[opcion]()
        else:
            respMenu = False
            print("Salio del MENU")

MenuPrincipal()

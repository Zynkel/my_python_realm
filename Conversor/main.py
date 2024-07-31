from medidas.longitud import *

def main():

    print("Conversor de unidades Python")
    accion = ""
    #Bucle de acciones
    while accion != "E":
        print ("Eliga entre las conversiones disponibles:")
        print ("1 - Longitud")
        print ("2 - Millas a metros")
        print ("E - Salir")
        accion = input()
        
        if accion == "1":
            Longitud.mainLongitud()   
        elif accion == "2":
            Longitud.millasAmetros()   

main()
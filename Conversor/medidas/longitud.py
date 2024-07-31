#Clase para las medidas de longitud

class Longitud:
    #Nota, las funciones se definen por encima de la principal
    #Realiza conversión de metros a millas, puede definirse el valor métrico en kilómetros
    def metrosAmillas():
        print("Defina el valor métro para conversar a millas, puede definir si se encuentra en kilómetros añadiendo (km) al final del valor")
        metrico = input()
        enKilometros = "km" in metrico

        if enKilometros:
            indiceKm = metrico.index("k")
            valor = metrico[:indiceKm]
            valor = valor.strip()
            kilometrosEnMillas = float(valor) / 0.621371
            print("Resultado: ", kilometrosEnMillas, " millas")
        else:
            metrosEnMillas = float(metrico) / 0.000621371
            print("Resultado: ", metrosEnMillas, " millas")

    def millasAmetros():
        print("Defina el valor millar para conversar a metros, si el valor resultado es superior a 999 metros se extresará en kilómetros")
        millas = input()
        valorEnmetros = float(millas) * 1609.34

        if valorEnmetros >= 1000:
            valorEnkilometros = valorEnmetros / 1000
            print("Resultado: ", valorEnkilometros, " km")
        else:
            print("Resultado:" ,valorEnmetros, " m")

    def mainLongitud():
        print("Medida Longitud. Acciones disponibles:")

        while True:
            print("1- Conversor de metros a millas")
            print("2- Conversor de millas a metros")
            print("B- Volver")

            accion = input()

            if accion == '1':
                Longitud.metrosAmillas()
            elif accion == '2':
                Longitud.millasAmetros()
            elif accion == 'B':
                break

        return


            
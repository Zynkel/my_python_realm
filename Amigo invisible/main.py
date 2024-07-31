
import random

def comenzarSorteo(participantes):
    participantes_dan = participantes.copy()
    participantes_reciben = participantes.copy()

    num_participantes = len(participantes)

    while num_participantes > 0:
        part_da = random.randint(0,num_participantes-1)
        part_a = random.randint(0,num_participantes-1)
        participanteDa = participantes_dan[part_da]
        participanteA = participantes_reciben[part_a]

        while participanteDa == participanteA:
            part_a = random.randint(0,num_participantes-1)
            participanteA = participantes_reciben[part_a]

        print("A " + participanteDa + " le ha tocado a " + participanteA)

        participantes_dan.remove(participanteDa)
        participantes_reciben.remove(participanteA)
        num_participantes -= 1

def main():
    print("Bienvenid@ al sorteo para el amigo invisible.")
    print("A continuación, inserte el nombre de los participantes para el sorteo uno a uno.")
    print("Para finalizar la inserción de los participantes escribir EMPEZAR")

    #Variables
    participantes = list() #Creación de la lista de participantes.
    nombre = ""
    num_participantes = 1

    while nombre != "EMPEZAR":
        print ("Inserta el nombre del participante número " + str(num_participantes) + ". Recuerda, para empezar escribir EMPEZAR.")
        nombre = input()

        if nombre != "EMPEZAR":
            participantes.append(nombre)
            num_participantes += 1
        else:
            comenzarSorteo(participantes)

        
main()
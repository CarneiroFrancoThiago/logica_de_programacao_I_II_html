def altera_aula():
     seg = input("Quais as aulas de segunda? {}, {}, {}, {}, {}".format(input("7:25: "),input("8:15: "),input("9:05: "),input("10:05: "),input("11:50 "),))




seg = print ("quimica")

def escolhe():
    escolha = int(input("Digite {} para ver o horario atual ou {} para altera-lo: ".format(1, 2)))

    if (escolha == 1):
        mostra_horario()
    elif (escolha == 2):
        altera_aula()


def mostra_horario():
    print("As aulas de segunda-feira são:", seg)

mostra_horario()

escolhe()

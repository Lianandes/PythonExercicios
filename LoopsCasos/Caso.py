dia = int(input("Digite o dia: "))

match dia:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case 3:
        print("Terça")
    case 4: 
        print("Quarta")
    case 5:
        print("Quinta")
    case 6:
        print("Sexta")
    case 7:
        print("Sabádo")
    case _:
        print("Esse número não é pertencente a nenhum dia.")
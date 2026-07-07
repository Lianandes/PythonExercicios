dia = int(input("Digite um número: "))

match dia:
    case 1 | 2 | 3 | 4 | 5:
        print("No meio da semana!")
    case 6 | 7 if dia == 6:
        print("Final de semana!")
    case _:
        print("Não quero sair nenhum dia.")
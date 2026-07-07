numero = []

print("Descubra o resultado da potenciação")

numero.append(int(input("Digite o valor da base: ")))
numero.append(int(input("Digite o valor do expoente: ")))
numero.append(numero[0] ** numero[1])

print(f"O resultado é {numero[2]}")
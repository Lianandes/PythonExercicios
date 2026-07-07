numero = []

numero.append(int(input("Digite um número: ")))
numero.append(int(input("Digite outro número: ")))
operacao_desejada = input("Qual operação deseja? ")

numero.append(numero[0] + numero[1])
numero.append(numero[0] - numero[1])
numero.append(numero[0] * numero[1])
numero.append(numero[0] / numero[1])

print(f"A soma: {numero[2]}, Subtração: {numero[3]}, Multiplicação: {numero[4]}, Divisão: {numero[5]}")
print(numero)
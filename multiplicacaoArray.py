numero = []

print("Descubra a multiplicação")

numero.append(int(input("Digite um número: ")))
numero.append(int(input("Digite outro número: ")))
numero.append(numero[0] * numero[1])

print(f"O resultado da multiplicação é: {numero[2]}")
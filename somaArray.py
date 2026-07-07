numero = []

print("Descubra a soma")

numero.append(int(input("Digite um número: ")))
numero.append(int(input("Digite outro número: ")))
numero.append(numero[0] + numero[1])

print(f"O resultado da soma é: {numero[2]}")
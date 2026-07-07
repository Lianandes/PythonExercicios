numero = []

print("Descubra a Divisão")

numero.append(float(input("Digite um número: ")))
numero.append(float(input("Digite outro número: ")))
numero.append(numero[0] / numero[1])

print(f"O resultado é: {numero[2]}")
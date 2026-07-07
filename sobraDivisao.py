numero = []

print("Descubra o resto da divisão")
numero.append(int(input("Digite um número: ")))
numero.append(int(input("Digite outro número: ")))
numero.append(numero[0] % numero[1])

print(f"O resto da divisão é: {numero[2]}")
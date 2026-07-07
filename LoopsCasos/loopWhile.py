contador = 0

while contador < 6:
    contador += 1
    if contador == 3:
        #break: Parao loop quando chega no 3, nem exibi o 3. 
        continue #: Volta para o laço de repetição. Não exibe o 3.
    print(contador)
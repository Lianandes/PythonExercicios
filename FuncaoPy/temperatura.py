print("Descubra os graus celsius com fahrenheit: ")

def temperatura(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

print(f"{temperatura(int(input("Digite a temperatura em °F: ")))}°C")
print(f"{temperatura(77)}°C")
print(f"{temperatura(95)}°C")
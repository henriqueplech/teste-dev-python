def inverter_string(s):
    invertida = ''
    for i in range(len(s) - 1, -1, -1):  # Percorre a string de trás para frente
        invertida += s[i]
    return invertida

# Exemplo:
print(inverter_string("Eu quero essa vaga!"))  # Saída: "!olleH"
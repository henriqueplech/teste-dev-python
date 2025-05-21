def verifica_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

# Entrada do usuário
numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci!")
else:
    print(f"O número {numero_informado} NÃO pertence à sequência de Fibonacci.")
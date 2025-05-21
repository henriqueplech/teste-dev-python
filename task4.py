faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())

print("Representação percentual por estado:")
print("-" * 30)
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    print(f"{estado.ljust(6)} → {percentual:6.2f}%")
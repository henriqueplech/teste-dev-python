import json

def calcular_estatisticas_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)
    
    faturamentos = [dia['valor'] for dia in dados['faturamento_diario'] if dia['valor'] > 0]
    
    menor = min(faturamentos)
    maior = max(faturamentos)
    media = sum(faturamentos) / len(faturamentos)
    
    dias_acima_media = sum(1 for valor in faturamentos if valor > media)
    
    return menor, maior, dias_acima_media

# Exemplo de uso
arquivo_json = 'faturamento.json'
menor, maior, dias_acima_media = calcular_estatisticas_faturamento(arquivo_json)

print(f"Menor faturamento diário: R${menor:.2f}")
print(f"Maior faturamento diário: R${maior:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
import json
import time

def salvar_parametros_em_json(pivo, porcentagem, duracao, tamanho, hora_inicio, hora_termino, nome_arquivo):
    # Tenta ler os dados existentes do arquivo, se o arquivo existir
    try:
        with open(nome_arquivo, 'r') as arquivo_existente:
            dados_existentes = json.load(arquivo_existente)
    except FileNotFoundError:
        dados_existentes = {}

    # Adiciona os novos dados aos dados existentes
    dados_existentes.update({
        "PIVO": pivo,
        "PORCENTAGEM": porcentagem,
        "DURACAO": duracao,
        "TAMANHO": tamanho,
        "HORA_INICIO": hora_inicio,
        "HORA_TERMINO": hora_termino
    })

    # Escreve os dados atualizados de volta para o arquivo
    with open(nome_arquivo, 'w') as arquivo_json:
        json.dump(dados_existentes, arquivo_json, indent=2)
    

# Exemplo de uso
pivo = 42
porcentagem = 0.75
duracao = 10
tamanho = 100
hora_inicio = time.strftime("%H:%M:%S")  # Hora atual no formato HH:MM:SS
# Simulando uma hora de término 1 hora depois da hora de início
hora_termino = (time.strptime(hora_inicio, "%H:%M:%S").tm_hour + 1) % 24
hora_termino = time.strftime("%H:%M:%S", time.strptime(str(hora_termino), "%H"))

nome_arquivo = "parametros.json"

salvar_parametros_em_json(pivo, porcentagem, duracao, tamanho, hora_inicio, hora_termino, nome_arquivo)

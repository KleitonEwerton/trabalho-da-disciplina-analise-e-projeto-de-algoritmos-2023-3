import random
import random
import os
import matplotlib.pyplot as plt

def lista_aleatoria_array(n):
    lista = list()
    for _ in range(n):
        lista.append(random.randint(0, n))
    
    lista.sort()
    return lista

def trocar_porcentagem(array, porcentagem):
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 e 100.")

    n = len(array)
    num_trocas = int(n * porcentagem / 100)

    for _ in range(num_trocas):
        index_a, index_b = random.sample(range(n), 2)
        array[index_a], array[index_b] = array[index_b], array[index_a]

def plotar_e_salvar_grafico(tempo, tamanho, titulo, nome_arquivo):
    # Verifica se as listas têm o mesmo tamanho
    if len(tempo) != len(tamanho):
        raise ValueError("As listas de tempo e tamanho devem ter o mesmo tamanho")

    # Cria uma nova figura a cada iteração para mostrar apenas a linha atual
    plt.figure()

    # Plota a linha atual com escala logarítmica apenas no eixo X (base 10)
    plt.semilogx(tamanho, tempo, marker='o')

    # Adiciona título e rótulos aos eixos
    plt.title(titulo)
    plt.xlabel('Tamanho do Array (log10)')
    plt.ylabel('Tempo de Execução (s)')

    # Marca todos os pontos no gráfico
    for i, txt in enumerate(tempo):
        plt.annotate(f'{txt:.6f}', (tamanho[i], tempo[i]), textcoords="offset points", xytext=(0,5), ha='center')

    # Verifica se a pasta 'grafico' existe, se não, cria
    if not os.path.exists('grafico'):
        os.makedirs('grafico')

    # Salva a figura na pasta 'grafico'
    caminho_arquivo = os.path.join('grafico', nome_arquivo)
    plt.savefig(caminho_arquivo)

def calcularMedia(arr, low, high):    
    return (arr[high] +  arr[(high + low) // 2] + arr[low]) // 3
import random
import random
import os
import matplotlib.pyplot as plt

from QuickSort import QuickSort


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

tamanhos_array = [int(1e2), int(1e3), int(1e4), int(1e5), int(1e6), int(1e7), int(1e8)]
porcentagens_troca = [5, 25, 45]
metodos_pivo = [5]
metodos_pivo_nome = ["Primeiro", "Central",
                     "Média", "Randômico", "Mediana", "Acha Pivo"]

if __name__ == "__main__":

    # Criando uma lista aleatória para ordenar
    for metodo_pivo in metodos_pivo:
        for porcentagem_troca in porcentagens_troca:

            tamanhos_na_iteracao = []
            tempo_na_iteracao = []
            titulo = f"Gráfico de Tempo x Tamanho - Pivô '{metodos_pivo_nome[metodo_pivo-1]}' - porcentagem_troca {porcentagem_troca}%"

            for tamanho_array in tamanhos_array:

                lista_aleatoria = list(range(tamanho_array))

                # Embaralhando a lista aleatória
                trocar_porcentagem(lista_aleatoria, porcentagem_troca)
                
                # Criando uma instância da classe QuickSort
                quick_sort = QuickSort(lista_aleatoria.copy())

                # Clonando a lista original para não modificar a original
                lista_copia = lista_aleatoria.copy()
                
                # Ordenando a lista usando o método de escolha de pivô específico
                quick_sort.ordenar(lista_copia, metodo_pivo)
                
                # Lista anterior
                # print(lista_aleatoria)
                # Exibindo o resultado
                print(
                       f"\nPivô '{metodos_pivo_nome[metodo_pivo-1]}', tamanho_array {tamanho_array}, tempo {quick_sort.time}\n\n")
                # print(lista_copia)
                tamanhos_na_iteracao.append(tamanho_array)
                tempo_na_iteracao.append(quick_sort.time)

            print(f"\nTítulo:\n {titulo}",
                  f"\nTamanhos na iteracao:\n {tamanhos_na_iteracao}",
                  f"\nTempos na iteracao:\n {tempo_na_iteracao}")
            plotar_e_salvar_grafico(
                tempo_na_iteracao, tamanhos_na_iteracao, titulo, f"grafico_{titulo}.png")

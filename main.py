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

    # Plota a linha atual
    plt.plot(tamanho, tempo, marker='o')

    # Adiciona título e rótulos aos eixos
    plt.title(titulo)
    plt.xlabel('Tamanho')
    plt.ylabel('Tempo')

    # Verifica se a pasta 'grafico' existe, se não, cria
    if not os.path.exists('grafico'):
        os.makedirs('grafico')

    # Salva a figura na pasta 'grafico'
    caminho_arquivo = os.path.join('grafico', nome_arquivo)
    plt.savefig(caminho_arquivo)

    # Exibe o gráfico
    # plt.show()


tamanhos_array = [10, 100, 1000, 10000, 100000, 1000000]
porcentagens_troca = [20, 40, 60]
metodos_pivo = [1, 2,4, 5]

if __name__ == "__main__":

    # Criando uma lista aleatória para ordenar
    for metodo_pivo in metodos_pivo:
        for porcentagem_troca in porcentagens_troca:
            
            tamanhos_na_iteracao = []
            tempo_na_iteracao = []
            titulo = f"Gráfico de Tempo x Tamanho - Pivô {metodo_pivo} - porcentagem_troca {porcentagem_troca}"
            
            for tamanho_array in tamanhos_array:
                
                lista_aleatoria = list(range(tamanho_array))

                # print("-----------\nLista Original:", lista_aleatoria, "\n----------")
                
                trocar_porcentagem(lista_aleatoria, porcentagem_troca)

                # print(f"Array Após Trocar {porcentagem_troca}% dos Valores:", lista_aleatoria)

                # print(f'Iniciando seleção de lista de tamanho_array n {tamanho_array}')

                # Criando uma instância da classe QuickSort
                quick_sort = QuickSort(lista_aleatoria.copy())

                

                # Clonando a lista original para não modificar a original
                lista_copia = lista_aleatoria.copy()
                quick_sort.lista = lista_copia
                
                # quick_sort.lista = [90, 12, 46, 95, 30, 67, 16, 95, 7, 15]
                
                # print("antes: ", quick_sort.lista)
                
                # Ordenando a lista usando o método de escolha de pivô específico
                quick_sort.ordenar(metodo_pivo)
                
                # print("dps: ", quick_sort.lista)

                # Exibindo o resultado
                # print(f"\nPivô {metodo_pivo}, tamanho_array {tamanho_array}, tempo {quick_sort.time}, {quick_sort.lista}\n\n" )
                # print(f"\nPivô {metodo_pivo}, tamanho_array {tamanho_array}, tempo {quick_sort.time}\n\n" )

                tamanhos_na_iteracao.append(tamanho_array)
                tempo_na_iteracao.append(quick_sort.time)
                
            print(f"Tamanhos na iteracao:\n {tamanhos_na_iteracao}", f"\nTempos na iteracao:\n {tempo_na_iteracao}", f"\nTítulo:\n {titulo}")
            plotar_e_salvar_grafico(tempo_na_iteracao, tamanhos_na_iteracao, titulo, f"grafico_{titulo}.png")
            

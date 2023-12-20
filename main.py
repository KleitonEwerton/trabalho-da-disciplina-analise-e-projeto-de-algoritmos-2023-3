from QuickSort import QuickSort
from mediana import trocar_porcentagem
from util import plotar_e_salvar_grafico

quantidade_iteracoes = 10

tamanhos_array = [int(1e1) , int(1e2), int(1e3), int(1e4), int(1e5), int(1e6), int(1e7)]
tamanhos_array = [int(1e1) , int(1e2), int(1e3), int(1e4), int(1e5)]
# tamanhos_array = [10, 20, 30, 40, 50]

porcentagens_troca = [5, 25, 45]

metodos_pivo = [1, 2, 3, 4, 5, 6]

metodos_pivo_nome = ["Primeiro", "Central",
                     "Média", "Randômico", "Mediana", "Acha Pivo"]

if __name__ == "__main__":

    for metodo_pivo in metodos_pivo:
        for porcentagem_troca in porcentagens_troca:

            tamanhos_na_iteracao = []
            tempo_na_iteracao = []
            titulo = f"Gráfico de Tempo x Tamanho - Pivô '{metodos_pivo_nome[metodo_pivo-1]}' - porcentagem_troca {porcentagem_troca}%"

            for tamanho_array in tamanhos_array:
                
                # Tempo total de execução de todas as iterações para um tamanho de array, metodo de escolha de pivô e porcentagem de troca
                tempo = 0
                
                for iteracao in range(quantidade_iteracoes):
                    
                    # Criando uma lista aleatória para ordenar
                    lista_aleatoria = list(range(tamanho_array))

                    # Embaralhando a lista aleatória
                    trocar_porcentagem(lista_aleatoria, porcentagem_troca)
                    
                    # Criando uma instância da classe QuickSort
                    quick_sort = QuickSort(lista_aleatoria.copy())

                    # Clonando a lista original para não modificar a original
                    lista_ordenada = lista_aleatoria.copy()
                    
                    # Ordenando a lista usando o método de escolha de pivô específico
                    quick_sort.ordenar(lista_ordenada, metodo_pivo)
                    
                    tempo += quick_sort.time
                    
                    print(
                        f"\n\nIteração {iteracao}, Pivô '{metodos_pivo_nome[metodo_pivo-1]}', tamanho_array {tamanho_array}, tempo {quick_sort.time}, porcentagem_troca {porcentagem_troca}%\n")
                    
                    # Lista anterior
                    # print("Lista Desordenada: ", lista_aleatoria)
                    
                    # Exibindo o resultado
                    # print("\nLista Ordenada", lista_ordenada)
                    
                tamanhos_na_iteracao.append(tamanho_array)
                tempo_na_iteracao.append(tempo/quantidade_iteracoes)

            print(f"\nTítulo:\n {titulo}",
                  f"\nTamanhos na iteracao:\n {tamanhos_na_iteracao}",
                  f"\nTempos na iteracao:\n {tempo_na_iteracao}")
            
            plotar_e_salvar_grafico(
                tempo_na_iteracao, tamanhos_na_iteracao, titulo, f"grafico_{titulo}.png")

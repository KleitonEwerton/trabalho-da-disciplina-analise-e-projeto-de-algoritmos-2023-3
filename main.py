import random
from QuickSort import QuickSort

if __name__ == "__main__":

    # Criando uma lista aleatória para ordenar
    tamanho = 10
    print(f'Iniciando seleção de lista de tamanho n {tamanho}')
    lista_aleatoria = [random.randint(1, 10000) for _ in range(tamanho)]

    print("Lista original:", lista_aleatoria)

    # Criando uma instância da classe QuickSort
    quick_sort = QuickSort(lista_aleatoria.copy())

    # Testando diferentes métodos de escolha de pivô
    for metodo_pivo in range(1, 6):
        
        # Clonando a lista original para não modificar a original
        lista_copia = lista_aleatoria.copy()
        quick_sort.lista = lista_copia
        # quick_sort.lista = [90, 12, 46, 95, 30, 67, 16, 95, 7, 15]
        
        # print("antes: ", quick_sort.lista)
        
        # Ordenando a lista usando o método de escolha de pivô específico
        quick_sort.ordenar(metodo_pivo)
        
        # print("dps: ", quick_sort.lista)

        # Exibindo o resultado
        print(f"\nPivô {metodo_pivo}, tamanho {tamanho}, tempo {quick_sort.time}, {quick_sort.lista}\n\n" )
        

import random
tamanho_array = int(1e4)

lista_aleatoria = list(range(tamanho_array))
antiga = lista_aleatoria.copy()

def trocar_porcentagem(array, porcentagem):
    if porcentagem < 0 or porcentagem > 100:
        raise ValueError("A porcentagem deve estar entre 0 e 100.")

    n = len(array)
    num_trocas = int(n * porcentagem / 100)

    for _ in range(num_trocas):
        index_a, index_b = random.sample(range(n), 2)
        array[index_a], array[index_b] = array[index_b], array[index_a]

trocar_porcentagem(lista_aleatoria, 50)

def particao_mediana(L, n1, n2, pivo):
    esq = n1
    dir = n2
    
    while True:
        while L[esq] < pivo:
            esq = esq + 1
        while L[dir] > pivo:
            dir = dir - 1
        
        if esq >= dir:
            return dir  # Retorna o novo valor de p após a partição

        # Troca L[esq] e L[dir]
        L[esq], L[dir] = L[dir], L[esq]

# Função para realizar o quicksort
def quick_sort_mediana(L, n1, n2):
    if n1 < n2:
        pto = median_of_medians(L, (n1 + n2) // 2)
        p = particao_mediana(L, n1, n2, pto)
        quick_sort_mediana(L, n1, p) 
        quick_sort_mediana(L, p + 1, n2)

def median_of_medians(A, i):
    while True:
        # divide A into sublists of len 5
        sublists = [A[j:j+5] for j in range(0, len(A), 5)]
        
        medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]

        if not medians:
            return A[0]  # Se não houver mais medians, retorne o primeiro elemento de A

        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)//2]
        else:
            # the pivot is the median of the medians
            pivot = median_of_medians(medians, len(medians)//2)

        # partitioning step
        low = [j for j in A if j < pivot]
        high = [j for j in A if j > pivot]

        k = len(low)
        m = A.count(pivot)

        if i < k:
            A = low
        elif i < k + m:
            return pivot
        else:
            A = high
            i -= k + m

quick_sort_mediana(lista_aleatoria, 0, len(lista_aleatoria) - 1)
print(lista_aleatoria)
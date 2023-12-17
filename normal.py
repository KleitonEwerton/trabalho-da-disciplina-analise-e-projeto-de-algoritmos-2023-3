import random
tamanho_array = int(1e2)
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
print(lista_aleatoria)

def achaPivo(n1, n2, L):
    esq = n1
    dir = n2
    pos = esq + 1
    pto = 0
    
    while True:
        if pos > dir:
            break
        else:
            if L[pos] >= L[pos - 1]:
                pos = pos + 1
            else:
                pto = pos
                break
    
    # Retornar o ponto de inflexão encontrado
    return pto

def particao(L, n1, n2, pivo):
    esq = n1
    dir = n2
    
    while True:
        while L[esq] < pivo:
            esq = esq + 1
        while L[dir] > pivo:
            dir = dir - 1
        
        if esq > dir:  # Corrigido para esq > dir
            return dir  # Retorna o novo valor de p após a partição

        # Troca L[esq] e L[dir]
        L[esq], L[dir] = L[dir], L[esq]

def quick_sort(L, n1, n2):
    esq = n1
    dir = n2
    
    if n1 < n2:  # Adicionada a condição de parada
        pivo = L[(n1 + n2) // 2]
        p = particao(L, n1, n2, pivo)
        
        quick_sort(L, n1, p) 
        quick_sort(L, p + 1, n2)


quick_sort(lista_aleatoria, 0, len(lista_aleatoria) - 1)
print(lista_aleatoria)
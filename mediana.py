import random
tamanho_array = int(1e5)

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

def quick_sort( A, start, end):
        if start < end:
            # p is pivot, it is now at its correct position
            p = partition(A, start, end)
            quick_sort(A, start, p)  # Corrigido
            quick_sort(A, p+1, end)

def partition( A, start, end):
    
        i = start-1  # left pointer
        array = A[start:end]
        pivot = find_median(array, len(array))
        
        if(pivot == -1):
            pivot = A[start]
                    
        j = end + 1  # right pointer
        while True:
            i += 1
            while (A[i] < pivot):
                i += 1  # move left pointer to right
            j -= 1
            
            while (A[j] > pivot):
                j -= 1  # move right pointer to left
                
            if i >= j:
                return j  # stop, pivot moved to its correct position
            
            A[i], A[j] = A[j], A[i]

 
# a, b = None, None
 
def particion_mediana(arr, l, r) : 
 
    lst = arr[r]; i = l; j = l; 
    while (j < r) :
        if (arr[j] < lst) :
            arr[i], arr[j] = arr[j],arr[i]; 
            i += 1; 
         
        j += 1; 
 
    arr[i], arr[r] = arr[r],arr[i]; 
    return i; 

def random_partition_medina(arr, l, r) :
    n = r - l + 1
    pivot = random.randrange(1, 100) % n
    arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
    return particion_mediana(arr, l, r); 
 
def median_util(arr, l, r, 
                k, a1, b1) : 
 
    global a, b
     
    # if l < r
    if (l <= r) :
      
        partitionIndex = random_partition_medina(arr, l, r)
         
        if (partitionIndex == k) :
            b = arr[partitionIndex]
            if (a1 != -1) :
                return
     
        elif (partitionIndex == k - 1) :
            a = arr[partitionIndex]
            if (b1 != -1) :
                return
  
        if (partitionIndex >= k) :
            return median_util(arr, l, partitionIndex - 1, k, a, b)
             
        else :
            return median_util(arr, partitionIndex + 1, r, k, a, b)
             
    return; 
 
def find_median(arr, n) :
    global a
    global b
    a = -1
    b = -1
     
    if (n % 2 == 1) :
        median_util(arr, 0, n - 1, n // 2, a, b)
        ans = b
         
    else :
        median_util(arr, 0, n - 1, n // 2, a, b)
        ans = (a + b) // 2
         
    return ans
 

quick_sort(lista_aleatoria, 0, len(lista_aleatoria) - 1)
print(lista_aleatoria)
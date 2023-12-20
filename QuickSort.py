import random
import time


class QuickSort:
    def __init__(self, lista):
        self.time = 0

    def ordenar(self, array, metodo_pivo):
        tempo_inicio = time.time()

        if(metodo_pivo == 6):
            self.quick_sort_acha_pivo(array, 0, len(array) - 1)
        else:
            self.quick_sort(array, 0, len(array) - 1, metodo_pivo)

        tempo_fim = time.time()
        self.time = tempo_fim - tempo_inicio

    def seleciona_pivo(self, A, inicio, fim, metodo_pivo):

        # 1 – Pivô fixo na primeira posição da lista
        if metodo_pivo == 1:
            return A[inicio]

        # 2 – Pivô fixo na posição central da lista: [1+n]DIV2
        elif metodo_pivo == 2:
            return A[(inicio + fim) // 2]

        # 3 – Pivô média considerando a média do primeiro , central e último valores da lista.
        elif metodo_pivo == 3:
            a = A[inicio]
            b = A[(inicio + fim) // 2]
            c = A[fim]
            return self.calcula_media(a, b, c)

        # 4 – Pivô randômico
        elif metodo_pivo == 4:
            return A[random.randint(inicio, fim)]

        # 5 – Pivô mediana
        elif metodo_pivo == 5:
            array = A[inicio:fim]
            return self.find_median(array, len(array))
            

    # Function to perform quicksort
    def quick_sort(self, A, start, end, metodo_pivo):
        if start < end:
            # p is pivot, it is now at its correct position
            p = self.partition(A, start, end, metodo_pivo)
            self.quick_sort(A, start, p, metodo_pivo)  # Corrigido
            self.quick_sort(A, p+1, end, metodo_pivo)

    def quick_sort_acha_pivo(self,L, n1, n2):
        esq = n1
        dir = n2
        
        pto = self.achaPivo(n1, n2, L)
        
        if pto != -1:
            p = self.particao_acha_pivo(L, n1, n2, L[pto], pto)
            self.quick_sort_acha_pivo(L, esq, p) 
            self.quick_sort_acha_pivo(L, p + 1, dir)


    def partition(self, A, start, end, metodo_pivo):
        i = start-1  # left pointer
        
        array = A[start:end]
        pivot = self.seleciona_pivo(A, start, end, metodo_pivo)
        
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
    
    def particao_acha_pivo(self, L, n1, n2, pivo, p):
        esq = n1
        dir = n2
        
        while True:
            while L[esq] <= pivo:
                esq = esq + 1
            while L[dir] > pivo:
                dir = dir - 1
            
            if esq >= dir:
                return dir  # Retorna o novo valor de p após a partição

            # Troca L[esq] e L[dir]
            L[esq], L[dir] = L[dir], L[esq]


    def achaPivo(self, n1, n2, L):
        esq = n1
        dir = n2
        pos = esq + 1
        pto = -1
        
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

    def calcula_media(self, a, b, c):
        return (a + b + c) // 3

    def particion_mediana(self, arr, l, r) : 
 
        lst = arr[r]; i = l; j = l; 
        while (j < r) :
            if (arr[j] < lst) :
                arr[i], arr[j] = arr[j],arr[i]; 
                i += 1; 
            
            j += 1; 
    
        arr[i], arr[r] = arr[r],arr[i]; 
        return i; 

    def random_partition_medina(self, arr, l, r) :
        n = r - l + 1
        pivot = random.randrange(1, 100) % n
        arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
        return self.particion_mediana(arr, l, r); 
    
    def median_util(self, arr, l, r, 
                    k, a1, b1) : 
    
        global a, b
        
        # if l < r
        if (l <= r) :
        
            partitionIndex = self.random_partition_medina(arr, l, r)
            
            if (partitionIndex == k) :
                b = arr[partitionIndex]
                if (a1 != -1) :
                    return
        
            elif (partitionIndex == k - 1) :
                a = arr[partitionIndex]
                if (b1 != -1) :
                    return
    
            if (partitionIndex >= k) :
                return self.median_util(arr, l, partitionIndex - 1, k, a, b)
                
            else :
                return self.median_util(arr, partitionIndex + 1, r, k, a, b)
                
        return; 
    
    def find_median(self, arr, n) :
        global a
        global b
        a = -1
        b = -1
        
        if (n % 2 == 1) :
            self.median_util(arr, 0, n - 1, n // 2, a, b)
            ans = b
            
        else :
            self.median_util(arr, 0, n - 1, n // 2, a, b)
            ans = (a + b) // 2
            
        return ans
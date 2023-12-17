import random
import time


class QuickSort:
    def __init__(self, lista):
        self.time = 0

    def ordenar(self, array, metodo_pivo):
        tempo_inicio = time.time()

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
            return self.median_of_medians(A, (inicio + fim) // 2)
            

        elif metodo_pivo == 6:
            return A[self.metodo_acha_pivout(A, inicio, fim)]

    def partition(self, A, start, end, metodo_pivo):
        i = start-1  # left pointer
        
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

    # Function to perform quicksort
    def quick_sort(self, A, start, end, metodo_pivo):
        if start < end:
            # p is pivot, it is now at its correct position
            p = self.partition(A, start, end, metodo_pivo)
            # sort elements to left and right of pivot separately
            if(metodo_pivo == 6):
                self.quick_sort(A, start, p-1, metodo_pivo)  # Corrigido
                self.quick_sort(A, p+1, end, metodo_pivo)
            else:
                self.quick_sort(A, start, p, metodo_pivo)  # Corrigido
                self.quick_sort(A, p+1, end, metodo_pivo)

    def calcula_media(self, a, b, c):
        return (a + b + c) // 3

    def metodo_acha_pivout(self, A, inicio, fim):
        esquerda = inicio
        direita = fim
        
        pos = esquerda + 1
        pto = -1
        
        while True:
            
            if pos > direita:
                break
            else:
                if A[pos] >= A[pos-1]:
                    pos += 1
                else:
                    pto = pos
                    break
        
        return pto

    def median_of_medians(self, A, i):

        #divide A into sublists of len 5
        sublists = [A[j:j+5] for j in range(0, len(A), 5)]
        medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
        if len(medians) <= 5:
            pivot = sorted(medians)[len(medians)//2]
        else:
            #the pivot is the median of the medians
            pivot = self.median_of_medians(medians, len(medians)//2)

        #partitioning step
        low = [j for j in A if j < pivot]
        high = [j for j in A if j > pivot]

        k = len(low)
        if i < k:
            return self.median_of_medians(low,i)
        elif i > k:
            return self.median_of_medians(high,i-k-1)
        else: #pivot = k
            return pivot
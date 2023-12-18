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
            p  = self.median_of_medians(A, (inicio + fim) // 2)
            return p
            

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
        
        if pto != 0:
            p = self.particao_acha_pivo(L, n1, n2, L[pto], pto)
            self.quick_sort_acha_pivo(L, esq, p) 
            self.quick_sort_acha_pivo(L, p + 1, dir)


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
    
    def particao_acha_pivo(self, L, n1, n2, pivo, p):
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


    def achaPivo(self, n1, n2, L):
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

    def calcula_media(self, a, b, c):
        return (a + b + c) // 3

    def median_of_medians(self, A, i):
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
                pivot = self.median_of_medians(medians, len(medians)//2)

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
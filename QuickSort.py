import random
import time

import numpy as np

from util import calcularMedia


class QuickSort:
    def __init__(self, lista):
        self.time = 0

    def ordenar(self, array, metodo_pivo):
        # Inicia o contador de tempo
        tempo_inicio = time.time()

        # Ordena o array
        self.quickSort(array, 0, len(array) - 1, metodo_pivo)

        # Finaliza o contador de tempo
        tempo_fim = time.time()
        
        # Calcula o tempo de execução
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
            return self.buscaMediana(array, len(array))
        
        # 6 – Pivô (Acha pivot)
        elif metodo_pivo == 6:
            return self.achaPivo(inicio, fim, A) 

    def quickSort(self, array, low, high, pivot_type):
        if low >= high:
            return

        # Seleciona o pivô de acordo com o método escolhido
        p = self.selecionaPivo(array, low, high, pivot_type)

        if p is None:
            return

        i = low
        j = high

        while i <= j:
            while array[i] < p:
                i += 1

            while array[j] > p:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if low < j:
            self.quickSort(array, low, j, pivot_type)

        if i < high:
            self.quickSort(array, i, high, pivot_type)

    def selecionaPivo(self, arr, low, high, pivot_type):
        
        if pivot_type == 1:
            return arr[low]

        if pivot_type == 2:
            return arr[(high + low)//2]

        if pivot_type == 3:
            return calcularMedia(arr, low, high)

        if pivot_type == 4:
            return arr[np.random.randint(low, high+1)]

        if pivot_type == 5:
            array = arr[low:high]
            return self.buscaMediana( array, len( array))

        if pivot_type == 6:
            return self.achaPivo(arr, low, high)

    def achaPivo(self, L, n1, n2):
        pos = n1 + 1
        pivo = None
        while True:
            if pos > n2:
                break
            elif L[pos] >= L[pos-1]:
                pos += 1
            else:
                pivo = pos-1
                break

        return L[pivo] if pivo is not None else pivo

    def particaoMediana(self, arr, l, r) : 
 
        lst = arr[r]; i = l; j = l; 
        while (j < r) :
            if (arr[j] < lst) :
                arr[i], arr[j] = arr[j],arr[i]; 
                i += 1; 
            
            j += 1; 
    
        arr[i], arr[r] = arr[r],arr[i]; 
        return i; 

    def particaoAleatorioMediana(self, arr, l, r) :
        n = r - l + 1
        pivot = random.randrange(1, 100) % n
        arr[l + pivot], arr[r] = arr[r], arr[l + pivot]
        return self.particaoMediana(arr, l, r); 
    
    def utilMediana(self, arr, l, r, 
                    k, a1, b1) : 
    
        global a, b
        
        if (l <= r) :
        
            indexDaParticao = self.particaoAleatorioMediana(arr, l, r)
            
            if (indexDaParticao == k) :
                b = arr[indexDaParticao]
                if (a1 != -1) :
                    return
        
            elif (indexDaParticao == k - 1) :
                a = arr[indexDaParticao]
                if (b1 != -1) :
                    return
    
            if (indexDaParticao >= k) :
                return self.utilMediana(arr, l, indexDaParticao - 1, k, a, b)
                
            else :
                return self.utilMediana(arr, indexDaParticao + 1, r, k, a, b)
                
        return; 
    
    def buscaMediana(self, arr, n) :
        global a
        global b
        a = -1
        b = -1
        
        if (n % 2 == 1) :
            self.utilMediana(arr, 0, n - 1, n // 2, a, b)
            ans = b
            
        else :
            self.utilMediana(arr, 0, n - 1, n // 2, a, b)
            ans = (a + b) // 2
            
        return ans
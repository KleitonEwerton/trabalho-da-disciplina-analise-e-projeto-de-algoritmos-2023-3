import random
import time

import numpy as np

from util import calcularMedia


class QuickSort:
    def __init__(self, lista):
        self.time = 0

    def ordenar(self, array, metodo_pivo):
        # Inicia o contador de tempo
        tempo_inicio = time.perf_counter()

        # Ordena o array
        self.quickSort(array, 0, len(array) - 1, metodo_pivo)

        # Finaliza o contador de tempo
        tempo_fim = time.perf_counter()
        
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

    def quickSort(self, array, inicio, fim, tipo_pivo):
        if inicio >= fim:
            return

        # Seleciona o pivô de acordo com o método escolhido
        p = self.selecionaPivo(array, inicio, fim, tipo_pivo)

        if p is None:
            return

        i = inicio
        j = fim

        while i <= j:
            while array[i] < p:
                i += 1

            while array[j] > p:
                j -= 1

            if i <= j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1

        if inicio < j:
            self.quickSort(array, inicio, j, tipo_pivo)

        if i < fim:
            self.quickSort(array, i, fim, tipo_pivo)

    def selecionaPivo(self, arr, inicio, fim, tipo_pivo):
        
        if tipo_pivo == 1:
            return arr[inicio]

        if tipo_pivo == 2:
            return arr[(fim + inicio)//2]

        if tipo_pivo == 3:
            return calcularMedia(arr, inicio, fim)

        if tipo_pivo == 4:
            return arr[np.random.randint(inicio, fim+1)]

        if tipo_pivo == 5:
            array = arr[inicio:fim]
            return self.mediana(array)

        if tipo_pivo == 6:
            return self.achaPivo(arr, inicio, fim)

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

        if pivo is not None:
            return L[pivo]
        else:
            return pivo

    def partitionMediana(self, arr, left, right, pivot):
        pivot_value = arr[pivot]
        arr[pivot], arr[right] = arr[right], arr[pivot]
        store_index = left

        for i in range(left, right):
            if arr[i] < pivot_value:
                arr[i], arr[store_index] = arr[store_index], arr[i]
                store_index += 1

        arr[store_index], arr[right] = arr[right], arr[store_index]
        return store_index


    def quickselectMediana(self, arr, left, right, k):
        if left == right:
            return arr[left]

        pivot = (right + left) // 2
        new_pivot_index = self.partitionMediana(arr, left, right, pivot)
        diff = new_pivot_index - left

        if diff == k:
            return arr[new_pivot_index]
        elif k < diff:
            return self.quickselectMediana(arr, left, new_pivot_index - 1, k)
        else:
            return self.quickselectMediana(arr, new_pivot_index + 1, right, k - diff - 1)


    def mediana(self, arr):
        if not arr:
            return None

        length = len(arr)

        if length % 2 == 1:
            return self.quickselectMediana(arr, 0, length - 1, length // 2)
        else:
            inicioer = self.quickselectMediana(arr, 0, length - 1, length // 2 - 1)
            fimer = self.quickselectMediana(arr, 0, length - 1, length // 2)
            return (inicioer + fimer) / 2.0


    
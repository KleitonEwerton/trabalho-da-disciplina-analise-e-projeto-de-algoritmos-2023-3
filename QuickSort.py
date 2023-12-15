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
            # Calcula a mediana da lista usando a função seleciona_mediana
            mediana_index = self.seleciona_mediana(A,
                                                   inicio, (inicio + fim) // 2, fim)

            # Retorna o índice da mediana como pivô
            return A[mediana_index]

    def partition(self, A, start, end, metodo_pivo):
        i = start-1  # left pointer
        pivot = self.seleciona_pivo(A, start, end, metodo_pivo)
        j = end+1  # right pointer
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
            self.quick_sort(A, start, p, metodo_pivo)
            self.quick_sort(A, p+1, end, metodo_pivo)

    def calcula_media(self, a, b, c):
        return (a + b + c) // 3

    def seleciona_mediana(self, A, inicio, meio, fim):
        a = A[inicio]
        b = A[meio]
        c = A[fim]
        mediana_indice = None  # índice da mediana

        # A sequência de if...else a seguir verifica qual é a mediana
        if a < b:
            if b < c:
                # a < b && b < c
                mediana_indice = meio
            else:
                if a < c:
                    # a < c && c <= b
                    mediana_indice = fim
                else:
                    # c <= a && a < b
                    mediana_indice = inicio
        else:
            if c < b:
                # c < b && b <= a
                mediana_indice = meio
            else:
                if c < a:
                    # b <= c && c < a
                    mediana_indice = fim
                else:
                    # b <= a && a <= c
                    mediana_indice = inicio

        return mediana_indice

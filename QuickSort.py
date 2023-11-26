import random
import time


class QuickSort:
    def __init__(self, lista):
        self.lista = lista
        self.time = 0

    def ordenar(self, metodo_pivo):
        tempo_inicio = time.time()

        self.quick_sort(0, len(self.lista) - 1, metodo_pivo)

        tempo_fim = time.time()
        self.time = tempo_fim - tempo_inicio

    def partition(self, inicio, fim, metodo_pivo):
        # Aqui será o local
        pivot_index = self.seleciona_pivo(inicio, fim, metodo_pivo)

        pivot = self.lista[pivot_index]
        # print("pivot:", pivot, self.lista)

        self.lista[inicio], self.lista[pivot_index] = self.lista[pivot_index], self.lista[inicio]

        i = inicio + 1
        j = fim

        while True:
            while i <= j and self.lista[i] <= pivot:
                i += 1
            while i <= j and self.lista[j] >= pivot:
                j -= 1
            if i <= j:
                self.lista[i], self.lista[j] = self.lista[j], self.lista[i]
            else:
                break

        self.lista[inicio], self.lista[j] = self.lista[j], self.lista[inicio]
        return j

    def seleciona_pivo(self, inicio, fim, metodo_pivo):
        
        #1 – Pivô fixo na primeira posição da lista
        if metodo_pivo == 1:
            return inicio

        # 2 – Pivô fixo na posição central da lista: [1+n]DIV2
        elif metodo_pivo == 2:
            return (inicio + fim) // 2

        # 3 – Pivô média considerando a média do primeiro , central e último valores da lista.
        elif metodo_pivo == 3:
            a = self.lista[inicio]
            b = self.lista[(inicio + fim) // 2]
            c = self.lista[fim]

            media_valor = self.calcula_media(a, b, c)

            # Encontra o índice correspondente à média na lista
            if media_valor not in self.lista:
                media_index = min(range(len(self.lista)), key=lambda i: abs(self.lista[i] - media_valor))
            else:
                media_index = self.lista.index(media_valor)

            # Retorna o índice da média como pivô
            return media_index
        
        # 4 – Pivô randômico
        elif metodo_pivo == 4:
            return random.randint(inicio, fim)
        
        # 5 – Pivô mediana
        elif metodo_pivo == 5:
            # Calcula a mediana da lista usando a função seleciona_mediana
            mediana_index = self.seleciona_mediana(
                inicio, (inicio + fim) // 2, fim)

            # Retorna o índice da mediana como pivô
            return mediana_index

        # 6 – Pivô computado pelo procedimento Acha Pivô
        elif metodo_pivo == 6:
            #aqui é a implementação do outro metodo
            print("Metodo acha pivo")
            return 
    

    def quick_sort(self, inicio, fim, metodo_pivo):
        # Algoritmo de QuickSort usando o primeiro elemento como pivô
        if inicio < fim:
            index_pivot = self.partition(inicio, fim, metodo_pivo)
            self.quick_sort(inicio, index_pivot - 1, metodo_pivo)
            self.quick_sort(index_pivot + 1, fim, metodo_pivo)

    def calcula_media(self, a, b, c):
        return (a + b + c) // 3

    def seleciona_mediana(self, inicio, meio, fim):
        a = self.lista[inicio]
        b = self.lista[meio]
        c = self.lista[fim]
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

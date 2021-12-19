from math import inf as бесконечность
import numpy as np
import sympy



def построить_код(G, информационные_слова):
    V = np.dot(информационные_слова, G)
    V %= 2
    return V


def проверить_код_на_соответствие_подгруппе(V):
    print("Проверка кода на соответсвие подгруппе")
    n = len(V)
    for i in range(n-1):
        for j in range(i+1, n):
            p = (V[i] + V[j]) % 2
            print(p)
            found = False
            for k in range(n):
                if (p == V[k]).all():
                    found = True
            print(found)


def найти_минимальное_расстоянеие(V):
    n = len(V)
    m = len(V[0])
    minimal_dist = бесконечность
    for i in range(n-1):
        for j in range(i+1, n):
            p = (V[i] + V[j]) % 2
            расстояние = 0
            for k in range(m):
                расстояние = расстояние + p[k]
            if расстояние < minimal_dist:
                minimal_dist = расстояние
    return minimal_dist


def найти_минимальный_вес(V):
    n = len(V)
    m = len(V[0])
    минимальный_вес = бесконечность
    for i in range(n):
        вес = 0
        for k in range(m):
            вес += V[i][k]
        if 0 < вес < минимальный_вес:
            минимальный_вес = вес
    return минимальный_вес


def построить_проверочную_матрицу(V, G):
    n = len(V)
    G = sympy.Matrix(G)
    H1 = G.nullspace()
    H = np.zeros((len(H1), len(H1[0])))
    for i in range(len(H1)):
        for j in range(len(H1[0])):
            H[i][j] = H1[i][j] % 2
    return H


def построить_синдром(V, H):
    S = np.dot(V, np.transpose(H))
    S %= 2
    return S


if __name__ == '__main__':
    G = np.array([[0, 1, 1, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1, 1, 1]])
    информационные_слова = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    V = построить_код(G, информационные_слова)
    print('Кодовая матрица')
    print(V)
    проверить_код_на_соответствие_подгруппе(V)
    H = построить_проверочную_матрицу(V, G)
    print(f'Проверочная матрица')
    print(H)
    print('Минимальное расстояние')
    print(найти_минимальное_расстоянеие(V))
    print('Минимальный вес')
    print(найти_минимальный_вес(V))
    print('Синдромы')
    print(построить_синдром(V, H))

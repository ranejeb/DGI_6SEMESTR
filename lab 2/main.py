import sympy as smp
from prettytable import PrettyTable
from sympy.parsing.sympy_parser import parse_expr


def получить_полиномы_до_степени(n):
    полиномы = [0, 1, x, x+1, x**2, x**2 + 1, x**2 + x, x**2 + x + 1,
                x**3, x**3 + 1, x**3 + x, x**3 + x + 1, x**3 + x**2, x**3 +
                x**2 + 1, x**3 + x**2 + x, x**3 + x**2 + x + 1,
                x ** 4, x ** 4 + 1, x ** 4 + x, x ** 4 + x + 1,
                x ** 4 + x ** 2, x ** 4 + x ** 2 + 1, x ** 4 + x ** 2 + x,
                x ** 4 + x ** 2 + x + 1, x ** 4 + x ** 3,
                x ** 4 + x ** 3 + 1, x ** 4 + x ** 3 + x,
                x ** 4 + x ** 3 + x + 1, x ** 4 + x ** 3 + x ** 2,
                x ** 4 + x ** 3 + x ** 2 + 1, x ** 4 + x ** 3 + x ** 2 + x,
                x ** 4 + x ** 3 + x ** 2 + x + 1]
    return полиномы[:2**n]


def построить_таблицу_сложения(размер_таблицы):
    A = [[0 for i in range(размер_таблицы+1)] for j in range(размер_таблицы+1)]
    A[0][0] = 'add'
    for i in range(1, размер_таблицы+1):
        A[0][i] = i-1
        A[i][0] = i-1
    for i in range(1, размер_таблицы+1):
        for j in range(1, размер_таблицы+1):
            A[i][j] = (A[i][0]+A[0][j]) % размер_таблицы
    return A


def построить_таблицу_умножения(размер_таблицы):
    B = [[0 for i in range(размер_таблицы + 1)]
         for j in range(размер_таблицы + 1)]
    B[0][0] = 'mult'
    for i in range(1, размер_таблицы + 1):
        B[0][i] = i - 1
        B[i][0] = i - 1
    for i in range(1, размер_таблицы+1):
        for j in range(1, размер_таблицы+1):
            B[i][j] = (B[i][0] * B[j][0]) % размер_таблицы
    return B


iter = 0


def привести_к_модулю_два(выражение):
    c_str = str(выражение)

    if c_str == '3':
        return '1'
    elif c_str == '2':
        c_str = '0'
    else:
        c_str = c_str.replace('-', '+')
        c_str = c_str.replace('+ 2', '+ 0')
        c_str = c_str.replace('2*', '0*')
        c_str = c_str.replace('+ 3', '+ 1')
        c_str = c_str.replace('3*', '1*')
    выражение = parse_expr(c_str)
    return выражение


def построить_таблицу_умножения_для_полинома(полином_модуль, размер_таблицы):
    polinoms = получить_полиномы_до_степени(размер_таблицы)
    размер_таблицы = 2**размер_таблицы
    C = [[0 for i in range(размер_таблицы + 1)]
         for j in range(размер_таблицы + 1)]
    C[0][0] = 'добавление'
    for i in range(1, размер_таблицы+1):
        C[0][i] = polinoms[i-1]
        C[i][0] = polinoms[i-1]
    for i in range(1, размер_таблицы+1):
        for j in range(1, размер_таблицы+1):
            sum = C[i][0]+C[0][j]
            C[i][j] = привести_к_модулю_два(
                smp.polys.polytools.pdiv(sum, полином_модуль)[1])
            a = 0*x + 2
    return C


def построить_таблицу_умножения_полиномов(полином_модуль, n):
    polinoms = получить_полиномы_до_степени(n)
    n = 2**n
    C = [[0 for i in range(n + 1)] for j in range(n + 1)]
    C[0][0] = 'умножение'
    for i in range(1, n+1):
        C[0][i] = polinoms[i-1]
        C[i][0] = polinoms[i-1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            mult = C[i][0]*C[0][j]
            print(smp.polys.polytools.pdiv(mult, полином_модуль)[1])
            C[i][j] = привести_к_модулю_два(
                smp.polys.polytools.pdiv(mult, полином_модуль)[1])
    return C


def печать_таблицы(M):
    table = PrettyTable()
    table.field_names = M[0]
    for i in range(1, len(M)):
        table.add_row(M[i])
    print(table)


if __name__ == '__main__':
    A = построить_таблицу_сложения(27)
    print('Таблица сложения по модулю 27')
    печать_таблицы(A)

    B = построить_таблицу_умножения(6)
    print('Таблица умножения по модулю 6')
    печать_таблицы(B)

    x = smp.symbols('x')
    # 11101
    polinom = x ** 4 + x ** 3 + x ** 2 + 1
    print(f"таблица сложения многочленов по молулю {polinom}")
    C = построить_таблицу_умножения_для_полинома(polinom, 3)
    печать_таблицы(C)
    # 1000
    polinom = x**3
    print(f"таблица умножения многочленов по модулю {polinom}")
    C = построить_таблицу_умножения_полиномов(polinom, 3)
    печать_таблицы(C)

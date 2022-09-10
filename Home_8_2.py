# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

import random

size = int(input("Введите размер матрицы: "))

def Create_list(square_size):
    square_list = [0] * square_size
    for i in range(square_size):
        square_list[i] = list(random.randint(1, 10) for i in range(square_size))
    return square_list

def Find_main_sum(square_list):
    main_sum = 0
    for i in range(len(square_list)):
        for j in range(len(square_list[i])):
            if i == j:
                main_sum += square_list[i][j]
    print(main_sum)
    return main_sum

def Find_rows(square_list, main_sum):
    for i in range(len(square_list)):
        row_sum = 0
        for j in range(len(square_list[i])):
            row_sum += square_list[i][j]
        if row_sum > main_sum:
            print(f"Cумма элементов {i} строки составляет {row_sum} и превосходит сумму главной диагонали матрицы {main_sum}")

a = Create_list(size)
for i in a:
    print(i)
sum = Find_main_sum(a)
Find_rows(a, sum)



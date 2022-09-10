# Задача 1. В каждой группе учится от 20 до 30 студентов. По итогам экзамена все оценки заносятся в таблицу. 
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.

import random
import math

col_class = int(input("Введите количество классов: "))

def Create_list(group):
    stud_list = [0] * group
    for i in range(group):
        stud = random.randint(20, 30)
        stud_list[i] = list(random.randint(1, 5) for i in range(stud))
    return stud_list

def find_max_GPA(stud_list):
    max_GPA = 0
    i_max = 0
    for i in range(len(stud_list)):
        sum = 0
        for j in range(len(stud_list[i])):
            sum += a[i][j]
        sum = round(sum/len(stud_list[i]), 4)
        print(sum, i)
        if sum > max_GPA:
            max_GPA = sum 
            i_max = i
    return max_GPA, i_max

a = Create_list(col_class)
for i in a:
    print(i)
max, ind_max = find_max_GPA(a)
print(f"наибольший средний балл {max}")
print(f"Группа с наибольшим средним баллом {ind_max+1}")

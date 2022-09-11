# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. Выведите его даты.

import random

col_months = 5
col_days = [31, 30, 31, 31, 30]
months_name = ['мая', 'июня', 'июля', 'августа', 'сентября']

def Create_list(months, days):
    temp_list = [0] * months
    for i in range(months):
        temp_list[i] = list(random.randint(10, 33) for i in range(days[i]))
    return temp_list

def Create_new_list(temp_list):
    new_temp_list = []
    for i in range(len(temp_list)):
        for j in range(len(temp_list[i])):
            new_temp_list.append(temp_list[i][j])
    return new_temp_list

def Find_max(new_temp_list):
    max_temp = 0
    start_max_day = 0
    finish_max_day = 0
    for i in range(len(new_temp_list)-7):
        sum = 0
        for j in range(i, i+7):
            sum += new_temp_list[j]
        if sum > max_temp:
            max_temp = sum
            start_max_day = i
            finish_max_day = i+7
    print(f"Максимальная температура {max_temp} в период с {start_max_day} по {finish_max_day}")
    return start_max_day, finish_max_day

def Find_min(new_temp_list):
    min_temp = 200000
    start_min_day = 0
    finish_min_day = 0
    for i in range(len(new_temp_list)-7):
        sum = 0
        for j in range(i, i+7):
            sum += new_temp_list[j]
        if sum < min_temp:
            min_temp = sum
            start_min_day = i
            finish_min_day = i+7
    print(f"Минимальная температура {min_temp} в период с {start_min_day} по {finish_min_day}")
    return start_min_day, finish_min_day

def Translate (day, col, moths):
    new_day_of_month = ''
    for i in range(len(col)):
        if day > col[i]: 
            day -= col[i]
        else:
            new_day_of_month = str(day) + ' ' + moths[i]
            break
    return new_day_of_month

temp = Create_list(col_months, col_days)
for i in temp:
    print(i)
new_temp = Create_new_list(temp)
start_max, finish_max = Find_max(new_temp)
start_min, finish_min = Find_min(new_temp)

print(f"Максимальная температура зафиксирована в период с {Translate (start_max, col_days, months_name)} по {Translate (finish_max, col_days, months_name)}")
print(f"Максимальная температура зафиксирована в период с {Translate (start_min, col_days, months_name)} по {Translate (finish_min, col_days, months_name)}")
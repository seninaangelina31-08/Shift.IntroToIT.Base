#INTRO TO IT 2nd COURSE
# Задача 13: Проверить, является ли список отсортированным. 

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
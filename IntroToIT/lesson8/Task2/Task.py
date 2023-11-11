def find_min(lst):
    if not lst:
        return None
    min_num = lst[0]
    for num in lst[1:]:
        if num < min_num:  # изменяем условие на поиск минимума
            min_num = num
    return min_num
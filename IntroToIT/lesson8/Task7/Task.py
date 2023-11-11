#INTRO TO IT 2nd COURSE
def count_occurrences(lst, element):
    count = 0
    for elem in lst:
        if elem == element:
            count += 1  # добавляем инкремент счетчика
    return count

#INTRO TO IT 2nd COURSE
def squares_dict(n):
    return {i: i ** 2 for i in range(1, n + 1)}  # исправляем границу интервала

print(squares_dict(5))  # выведет {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
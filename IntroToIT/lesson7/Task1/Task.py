# Функция для сложения двух чисел
def add_numbers(a, b):      
    result = a + b
    return result


# Функция для умножения двух чисел
def multiply_numbers(a, b):
    result = a * b
    return result


# Функция для нахождения максимального числа в списке
def find_max_number(numbers):
    max_number = max(numbers)
    return max_number


# Функция для вычисления факториала числа
def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Функция для определения четности числа
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


# Определение чисел и вызов функций
num1 = 10
num2 = 5
sum_result = add_numbers(num1, num2)
product_result = multiply_numbers(num1, num2)
numbers_list = [3, 8, 1, 6, 12]
max_num = find_max_number(numbers_list)
factorial_result = calculate_factorial(5)
is_even_num = is_even(7)

# Вывод результатов
print(f"Сумма чисел {num1} и {num2} равна {sum_result}")
print(f"Произведение чисел {num1} и {num2} равно {product_result}")
print(f"Наибольшее число в списке {numbers_list} - {max_num}")
print(f"Факториал числа 5 равен {factorial_result}")

# Проверка четности числа
if is_even_num:
    print("Число 7 - четное.")
else:
    print("Число 7 - нечетное.")
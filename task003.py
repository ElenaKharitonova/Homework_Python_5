# Задача 3. Задайте список случайных чисел от 1 до 10.
# Посчитайте, сколько всего совпадающих элементов есть 
# в списке. Удалите все повторяющиеся элементы.

import random

numbers = list(random.randint(1,10) for _ in range (random.randint(5,12)))
print(f'Список случайных чисел: {numbers}')
result = list(filter(lambda x:numbers.count(x) > 1, numbers))
print(f'Совпадающие элементы: {numbers}')
quantity = len(result)
print(f'Количество совпадающих элементов в списке {quantity}')
print(f'Список уникальных значений: {set(numbers)}')
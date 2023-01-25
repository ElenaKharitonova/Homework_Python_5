# Задача 2. Дан список случайных чисел. Создайте список, 
# в который попадают числа, описывающие возрастающую
# последовательность. Порядок элементов менять нельзя.

import random

numbers = list(random.randint(1,100) for _ in range (random.randint(5,15)))
print(f'Список случайных чисел: {numbers}')

size = len(numbers)
index = random.randint(0, size-1)
result = [numbers[index]]
while index < size:
    index = random.randint(index, size)
    if index != size and numbers[index] > result[-1]:
        result.append(numbers[index])
print(f'Случайная возрастающая последовательность: {result}')
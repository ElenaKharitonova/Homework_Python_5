# Задача 1. Задайте список случайных чисел 
# от 1 до 10,выведите все элементы больше 5.
# Используйте для решения лямбда-функцию.

import random

digit=int(input('Задайте натуральное число до 100:  '))
numbers = list(random.randint(1,100) for _ in range (random.randint(3,15)))
print(f'Список случайных чисел: {numbers}')
result = list(filter(lambda x: x > digit, numbers))
print(f'Элементы больше {digit}: {result}')

# Написать программу, которая:
# 1.Создает двумерную матрицу произвольного размера от 4 до 8 во высоте и ширине, заполненную значениями из списка **[-3, -5, -2, -12, 0, 15, 4, 7, 2]**
# 2.Выводит данную матрицу в форматированном виде.
# 3. Выводит сумму всех четных элементов
import random # Импорт библиотеки рандома
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2] # Список значений для заполнения матрицы
while True:
    rows = int(input("Введите количество строк (от 4 до 8): "))
    cols = int(input("Введите количество столбцов (от 4 до 8): "))
    if 4 <= rows <= 8 and 4 <= cols <= 8:
        break
    else:
        print("Пожалуйста, введите числа в диапазоне от 4 до 8.")
matrix = [[random.choice(values) for _ in range(cols)] for _ in range(rows)] # Создание и заполнение матрицы случайными значениями из списка
print("Сгенерированная матрица:") # Вывод матрицы в форматированном виде
for row in matrix:
    print(" ".join(f"{element:4}" for element in row)) # Выводит матрицу в форматированном виде
even_sum = sum(element for row in matrix for element in row if element % 2 == 0) # Проверка на четность и подсчет суммы четных чисел
print("Сумма всех чётных элементов:", even_sum) # Вывод 

# Задание №2 по варианту : `Динамическое программирование №1`

## Вариант 19

## Задание 2

Дан примитивный калькулятор, который может выполнять следующие три операции с текущим числом x: умножить x на 2,
умножить x на 3 или прибавить 1 к x. Дано положительное целое число n, найдите минимальное количество операций,
необходимых для получения числа n, начиная с числа 1.

## Input / Output

| Input | Output                                                             |
|-------|--------------------------------------------------------------------|
| 1     | 0<br/>1                                                            |
| 5     | 3<br/>1 2 4 5                                                      |
| 96234 | 14<br/>1 3 9 10 11 22 66 198 594 1782 5346 16038 16039 32078 96234 |

## Ограничения по времени и памяти

- Ограничение по времени. 1 сек.
- Ограничение по памяти. 256 мб.

## Запуск проекта

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MatoiDev/AlgoLabs.ITMO.git
   ```

2. Перейдите в папку с любой задачей:
   ```bash
   cd AlgoLabs.ITMO/lab7/task<N>/src
   ```

3. Запустите программу:
   ```bash
   python Solution.py
   ```

## Тестирование

Для запуска тестов выполните:

   ```bash
   pytest -s Tests.py
   ```
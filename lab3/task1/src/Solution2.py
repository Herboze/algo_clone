import random
from lab3.utils import read, write


def randomized_partition3(arr, low, high):
    """
    Случайное разбиение для улучшенной версии QuickSort.
    Выбираем случайный опорный элемент и перемещаем его в конец.
    """
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition3(arr, low, high)


def partition3(arr, low, high):
    """
    Трехстороннее разбиение:
    Разделение на элементы меньше, равные и больше опорного.
    """
    pivot = arr[high]
    lt = low
    i = low
    gt = high
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1
    return lt, gt


def randomized_quick_sort_3way(arr, low, high):
    """
    Улучшенная версия QuickSort для обработки
    массивов с несколькими уникальными элементами.
    Используется случайный выбор опорного элемента.
    """
    stack = [(low, high)]

    while stack:
        low, high = stack.pop()
        if low < high:
            lt, gt = randomized_partition3(arr, low, high)
            stack.append((low, lt - 1))  # левая часть массива
            stack.append((gt + 1, high))  # правая часть массива


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

    randomized_quick_sort_3way(array, 0, n - 1)
    file.close()

    write('../txtf/output.txt', ' '.join(map(str, array)))

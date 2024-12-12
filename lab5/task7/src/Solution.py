from lab5.utils import read, write


def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Проверяем, есть ли левый сын и он больше текущего
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Проверяем, есть ли правый сын и он больше текущего
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если находим большее значение, чем текущее, меняем местами
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)  # Рекурсивно восстанавливаем кучу


def build_max_heap(arr):
    n = len(arr)
    # Строим кучу начиная с последнего не-листового узла
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)


def function(arr):
    n = len(arr)
    build_max_heap(arr)

    # Извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами максимальный элемент с последним
        max_heapify(arr, i, 0)  # Восстанавливаем кучу для оставшихся элементов
    return arr


def max_heapify(arr, n, i):
    """Итеративная версия Max-Heapify"""
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Проверяем, есть ли левый сын и он больше текущего
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Проверяем, есть ли правый сын и он больше текущего
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Если находим большее значение, чем текущее, меняем местами
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest  # Обновляем индекс, чтобы продолжить спускать по дереву
        else:
            break  # Если куча уже верна, выходим из цикла


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline())
    arr = list(map(int, file.readline().split()))
    file.close()

    res = function(arr)

    print(f"\nINPUT: {n, arr}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', ' '.join(map(str, arr)) + '\n')

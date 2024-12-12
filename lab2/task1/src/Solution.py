from lab2.utils import read, write

def function_merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * (n1 + 1)  # Создаем массив L длиной n1 + 1
    R = [0] * (n2 + 1)  # Создаем массив R длиной n2 + 1

    # Заполняем массив L
    for i in range(n1):
        L[i] = A[p + i]

    # Заполняем массив R
    for j in range(n2):
        R[j] = A[q + j + 1]

    L[n1] = float('inf')
    R[n2] = float('inf')

    i, j = 0, 0  # Индексы для L и R

    # Слияние массивов
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def function_merge_no_sentinel(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1  # Создаем массив L длиной n1
    R = [0] * n2  # Создаем массив R длиной n2

    # Заполняем массив L
    for i in range(n1):
        L[i] = A[p + i]

    # Заполняем массив R
    for j in range(n2):
        R[j] = A[q + j + 1]

    i, j, k = 0, 0, p  # Индексы для L, R и A

    # Слияние массивов
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    # Копируем оставшиеся элементы из L, если есть
    while i < n1:
        A[k] = L[i]
        i += 1
        k += 1

    # Копируем оставшиеся элементы из R, если есть
    while j < n2:
        A[k] = R[j]
        j += 1
        k += 1


def function_merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2  # Находим средний индекс
        function_merge_sort(A, p, q)  # Сортируем левую половину
        function_merge_sort(A, q + 1, r)  # Сортируем правую половину
        function_merge_no_sentinel(A, p, q, r)  # Объединяем отсортированные половины

if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

    function_merge_sort(array, 0, len(array) - 1)
    file.close()

    write('../txtf/output.txt', ' '.join(map(str, array)))

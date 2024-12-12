from lab2.utils import read, write


def majority_element(arr, left, right):
    # Базовый случай, если массив состоит из одного элемента
    if left == right:
        return arr[left]

    # Разделение массива на две половины
    mid = (left + right) // 2
    left_candidate = majority_element(arr, left, mid)
    right_candidate = majority_element(arr, mid + 1, right)

    # Если оба кандидата одинаковы, возвращаем одного из них
    if left_candidate == right_candidate:
        return left_candidate

    # Подсчет количества каждого кандидата
    left_count = sum(1 for i in range(left, right + 1) if arr[i] == left_candidate)
    right_count = sum(1 for i in range(left, right + 1) if arr[i] == right_candidate)

    # Проверка, является ли левый кандидат элементом большинства
    if left_count > (right - left + 1) // 2:
        return left_candidate
    # Проверка, является ли правый кандидат элементом большинства
    elif right_count > (right - left + 1) // 2:
        return right_candidate
    else:
        return None


def function(arr):
    n = len(arr)
    candidate = majority_element(arr, 0, n - 1)

    if candidate is None:
        return 0

    count = arr.count(candidate)
    return 1 if count > n // 2 else 0


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    arr = list(map(int, file.readline().strip().split()))
    file.close()

    result = function(arr)

    write('../txtf/output.txt', str(result) + '\n')

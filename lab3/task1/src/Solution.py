from lab3.utils import read, write
import random


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_partition(arr, low, high):
    rand_pivot = random.randint(low, high)
    arr[high], arr[rand_pivot] = arr[rand_pivot], arr[high]
    return partition(arr, low, high)


def randomized_quick_sort(arr, low, high):
    """
    Используется случайный выбор опорного элемента,
    чтобы улучшить производительность на случайных данных.
    """
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1)
        randomized_quick_sort(arr, pi + 1, high)


def main():
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

    randomized_quick_sort(array, 0, n - 1)
    file.close()

    write('../txtf/output.txt', ' '.join(map(str, array)))


if __name__ == "__main__":
    main()

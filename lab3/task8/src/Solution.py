from lab3.utils import read, write


def distance_squared(point):
    """Функция для расчета квадрата расстояния до начала координат."""
    x, y = point
    return x * x + y * y


def quicksort(points, low, high):
    stack = [(low, high)]

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_index = partition(points, left, right)
            # Добавляем левую и правую подзадачи в стек
            stack.append((left, pivot_index - 1))
            stack.append((pivot_index + 1, right))


def partition(points, left, right):
    """Разделение массива относительно опорного элемента."""
    pivot = distance_squared(points[right])
    i = left - 1
    for j in range(left, right):
        if distance_squared(points[j]) <= pivot:
            i += 1
            points[i], points[j] = points[j], points[i]
    points[i + 1], points[right] = points[right], points[i + 1]
    return i + 1


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n, K = map(int, file.readline().split())
    points = [tuple(map(int, file.readline().split())) for _ in range(n)]
    file.close()

    quicksort(points, 0, len(points) - 1)

    closest_points = points[:K]

    write("../txtf/output.txt", ",".join([f"[{x},{y}]" for (x, y) in closest_points]))

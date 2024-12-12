from lab5.utils import read, write, PriorityQueue


def function(operations):
    queue = PriorityQueue()
    result = []

    for i, operation in enumerate(operations):
        if operation[0] == "A":
            _, x = operation
            queue.push(int(x))  # Добавляем элемент
        elif operation[0] == "X":
            result.append(queue.pop())  # Извлекаем минимальный элемент
        elif operation[0] == "D":
            _, x, y = operation
            queue.decrease(int(x) - 1, int(y))  # Обновляем элемент

    return result


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    operations = [line.strip().split() for line in file.readlines()]
    file.close()

    res = function(operations)

    print(f"\nINPUT: {n, operations}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', "\n".join(map(str, res)))

from lab6.utils import read, write


def function(operations):
    my_set = set()
    results = []

    for operation in operations:
        parts = operation.split()
        command = parts[0]
        value = int(parts[1])

        if command == "A":  # Добавить элемент
            my_set.add(value)
        elif command == "D":  # Удалить элемент
            my_set.discard(value)
        elif command == "?":  # Проверить наличие элемента
            results.append("Y" if value in my_set else "N")

    return "\n".join(results)


if __name__ == "__main__":
    # Чтение входных данных
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    operations = file.readlines()
    file.close()

    res = function(operations)

    print(f"\nINPUT: {n, operations}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', res)

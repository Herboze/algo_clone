from lab5.utils import read, write, MinHeap


def function(n, task_times):
    # Инициализация кучи потоков
    heap = MinHeap()
    for i in range(n):
        heap.push((0, i))  # Все потоки свободны в начале

    result = []
    for task_time in task_times:
        free_time, thread_index = heap.pop()  # Извлекаем поток с минимальным временем освобождения
        result.append((thread_index, free_time))
        heap.push((free_time + task_time, thread_index))  # Обновляем поток и возвращаем в кучу

    return result


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n, _ = map(int, file.readline().split())
    task_times = list(map(int, file.readline().split()))
    file.close()

    res = function(n, task_times)
    print(f"\nINPUT: {n, task_times}")
    print(f"OUTPUT:\n{res}")
    write('../txtf/output.txt', "\n".join(f"{e[0]} {e[1]}" for e in res))

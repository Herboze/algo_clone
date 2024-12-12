class MinHeap:
    def __init__(self):
        self.data = []

    def push(self, item):
        """Добавить элемент в кучу."""
        self.data.append(item)
        self._sift_up(len(self.data) - 1)

    def pop(self):
        """Извлечь минимальный элемент из кучи."""
        self._swap(0, len(self.data) - 1)
        item = self.data.pop()
        self._sift_down(0)
        return item

    def _sift_up(self, idx):
        """Поднять элемент наверх для сохранения свойства кучи."""
        parent = (idx - 1) // 2
        if idx > 0 and self.data[idx] < self.data[parent]:
            self._swap(idx, parent)
            self._sift_up(parent)

    def _sift_down(self, idx):
        """Опустить элемент вниз для сохранения свойства кучи."""
        left = 2 * idx + 1
        right = 2 * idx + 2
        smallest = idx

        if left < len(self.data) and self.data[left] < self.data[smallest]:
            smallest = left
        if right < len(self.data) and self.data[right] < self.data[smallest]:
            smallest = right
        if smallest != idx:
            self._swap(idx, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.data[i], self.data[j] = self.data[j], self.data[i]


class PriorityQueue:
    def __init__(self):
        self.queue = []  # Список для хранения элементов

    def push(self, value):
        """Добавляем элемент в очередь."""
        self.queue.append(value)
        self.queue.sort()  # Сортируем список, чтобы элементы были в порядке возрастания

    def pop(self):
        """Извлекаем минимальный элемент из очереди."""
        if self.queue:
            return self.queue.pop(0)  # Извлекаем первый элемент (минимальный)
        else:
            return "*"  # Если очередь пуста, возвращаем "*"

    def decrease(self, index, new_value):
        """Обновляем элемент в очереди на новый с меньшим значением."""
        # Мы ищем элемент по индексу и уменьшаем его значение
        old_value = self.queue[index]
        self.queue[index] = new_value
        self.queue.sort()  # Сортируем список после изменения значения элемента


def measuring_time_and_memory(task_func, *args):
    import time
    import memory_profiler

    start_time = time.monotonic_ns()
    result = task_func(*args)
    end_time = time.monotonic_ns() - start_time

    memory = memory_profiler.memory_usage((task_func, args))
    human_read_input = f"Input: {args}"[:100] + "..." if len(f"Input: {args}") > 100 else f"Input: {args}"
    human_read_result = f"Result: {result}"[:100] + "..." if len(f"Result: {result}") > 100 else f"Result: {result}"

    # print(f"\n{human_read_input}")
    # print(human_read_result)
    # print(f"Execution time: {end_time / 1e3:} microseconds")
    # print(f"Peak memory usage: {memory[0]:.2f} bytes\n\n")

    return result, end_time / 1e9, memory[0] / (1024 * 1024)


def read(path: str):
    return open(path, 'r')


def write(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

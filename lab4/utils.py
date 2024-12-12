from typing import Optional


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self, *elements):
        self._container: list[int] = list(elements)

    def pop(self) -> Optional[int]:
        if self.is_empty():
            return None
        res = self._container[0]
        self._container = self._container[1:]
        return res

    def push(self, element):
        self._container.append(element)

    def min(self) -> int:
        if self.is_empty():
            return 0
        return min(self._container)

    def is_empty(self) -> bool:
        return len(self._container) == 0


class Stack:
    def __init__(self, *args):
        self._container: list[int | str] = list(args)

    def push_back(self, element):
        self._container.append(element)

    def face(self) -> Optional[str | int]:
        if not self.is_empty():
            return self._container[-1]
        return None

    def pop(self) -> Optional[str | int]:
        if not self.is_empty():
            return self._container.pop()
        return None

    def is_empty(self) -> bool:
        return len(self._container) == 0


class Deque:
    def __init__(self):
        self.elements = []

    def append(self, value):
        self.elements.append(value)

    def appendleft(self, value):
        self.elements.insert(0, value)

    def pop(self):
        if self.elements:
            return self.elements.pop()
        return None

    def popleft(self):
        if self.elements:
            return self.elements.pop(0)
        return None

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

    def __bool__(self):
        return bool(self.elements)


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


def generate_random_array(size):
    import random
    return random.sample(range(-10 ** 9, 10 ** 9), size)


def read(path: str):
    return open(path, 'r')


def write(path, data):
    file = open(path, 'w')
    file.write(data)
    file.close()

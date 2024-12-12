from unittest import TestCase
import lab0.task1.src.Solution as Solution


def measuring(task_func, *args):
    import time
    import memory_profiler

    start_time = time.monotonic_ns()
    result = task_func(*args)
    end_time = time.monotonic_ns() - start_time

    memory = memory_profiler.memory_usage((task_func, args))
    print(f"\nInput: {args}")
    print(f"Result: {result}")
    print(f"Execution time: {end_time / 1e3:} microseconds")
    print(f"Peak memory usage: {memory[0]:.2f} bytes\n\n")

    return result


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        a = -1e9
        b = -1e9
        result = measuring(Solution.function, a, b)
        self.assertEqual(a + b, result)

    def test_should_task_with_upper_bound(self):
        a = 1e9
        b = 1e9
        result = measuring(Solution.function, a, b)
        self.assertEqual(a + b, result)

    def test_should_task_with_input1(self):
        a = 12
        b = 25
        result = measuring(Solution.function, a, b)
        self.assertEqual(a + b, result)

    def test_should_task_with_input2(self):
        a = 130
        b = 61
        result = measuring(Solution.function, a, b)
        self.assertEqual(a + b, result)

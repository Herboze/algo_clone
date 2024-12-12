from unittest import TestCase
from lab5.utils import measuring_time_and_memory
import lab5.task5.src.Solution as Solution


class TestSolution(TestCase):
    def test_should_with_input_1(self):
        # given
        n = 4
        task_times = list(map(int, "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1".split()))
        expected_result = [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (1, 1), (2, 1), (3, 1), (0, 2), (1, 2), (2, 2),
                           (3, 2),
                           (0, 3), (1, 3), (2, 3), (3, 3), (0, 4), (1, 4), (2, 4), (3, 4)]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, task_times)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_input_2(self):
        # given
        n = 2
        task_times = list(map(int, "1 2 3 4 5".split()))
        expected_result = [(0, 0), (1, 0), (0, 1), (1, 2), (0, 4)]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, task_times)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        n = 1
        task_times = [0]
        expected_result = [(0, 0)]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, task_times)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 100_000
        m = 100_000
        task_times = [10 ** 5] * m
        # Результат формируется динамически для проверки
        expected_result = [(i % n, i // n * 10 ** 5) for i in range(m)]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, task_times)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

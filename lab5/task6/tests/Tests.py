from unittest import TestCase
from lab5.utils import measuring_time_and_memory
import lab5.task6.src.Solution as Solution


class TestSolution(TestCase):
    def test_should_with_input_1(self):
        # given
        operations = [
            ("A", 3),
            ("A", 4),
            ("A", 2),
            ("X",),
            ("D", 2, 1),
            ("X",),
            ("X",),
            ("X",)
        ]
        expected_result = [2, 1, 3, "*"]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        operations = [
            ("A", 10),
            ("X",)
        ]
        expected_result = [10]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10000  # 100000 операций
        operations = [("A", i) for i in range(1, n + 1)] + [("X",) for _ in range(n)]
        expected_result = list(range(1, n + 1))  # Результат будет от 1 до 100000

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_operations(self):
        # given
        operations = [
            ("A", 5),
            ("A", 2),
            ("A", 8),
            ("A", 1),
            ("X",),
            ("D", 3, 0),
            ("X",)
        ]
        expected_result = [1, 0]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

from unittest import TestCase
from lab5.utils import measuring_time_and_memory
import lab5.task1.src.Solution as Solution


class TestSolution(TestCase):
    def test_should_with_input_1(self):
        # given
        n = 5
        arr = [1, 0, 1, 2, 0]
        expected_result = "NO"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr, n)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_input_2(self):
        # given
        n = 5
        arr = [1, 3, 2, 5, 4]
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr, n)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        n = 1
        arr = [1]
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr, n)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10 ** 6
        arr = list(range(1, n + 1))  # A valid non-decreasing heap
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr, n)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

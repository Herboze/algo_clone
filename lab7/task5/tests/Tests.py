from unittest import TestCase
from lab7.utils import measuring_time_and_memory
import lab7.task5.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_example1(self):
        # given
        a = [1, 2, 3]
        b = [2, 1, 3]
        c = [1, 3, 5]
        expected_result = 2  # Общая подпоследовательность: [1, 3]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, a, b, c)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_example2(self):
        # given
        a = [8, 3, 2, 1, 7]
        b = [8, 2, 1, 3, 8, 10, 7]
        c = [6, 8, 3, 1, 4, 7]

        expected_result = 3  # Общая подпоследовательность: [8, 3, 7]

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, a, b, c)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_no_common_subsequence(self):
        # given
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [7, 8, 9]
        expected_result = 0  # Нет общей подпоследовательности

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, a, b, c)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_large_case(self):
        # given
        a = [1] * 100
        b = [1] * 100
        c = [1] * 100
        expected_result = 100  # Все элементы совпадают

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, a, b, c)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

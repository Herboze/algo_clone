from unittest import TestCase
from lab5.utils import measuring_time_and_memory
import lab5.task7.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_lower_bound(self):
        # given
        arr = [42]
        expected_result = [42]  # Массив с одним элементом должен остаться таким же

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_random_input_1_000(self):
        # given
        import random
        arr = random.sample(range(1, 1001), 1000)  # Массив случайных чисел от 1 до 10^3
        expected_result = sorted(arr)  # Ожидаем отсортированный массив по убыванию

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_random_input_10_000(self):
        # given
        import random
        arr = random.sample(range(1, 10001), 10000)  # Массив случайных чисел от 1 до 10^4
        expected_result = sorted(arr)  # Ожидаем отсортированный массив по убыванию

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_random_input_100_000(self):
        # given
        import random
        arr = random.sample(range(1, 100001), 100000)  # Массив случайных чисел от 1 до 10^5
        expected_result = sorted(arr)  # Ожидаем отсортированный массив по убыванию

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, arr)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

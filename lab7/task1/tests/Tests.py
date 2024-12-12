from unittest import TestCase
from lab7.utils import measuring_time_and_memory
import lab7.task1.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_example1(self):
        # given
        money = 2
        coins = [1, 3, 4]
        expected_result = 2  # (1 + 1)

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, money, coins)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_example2(self):
        # given
        money = 34
        coins = [1, 3, 4]
        expected_result = 9  # 34 = (4 * 8 + 2)

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, money, coins)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_impossible_case(self):
        # given
        money = 7
        coins = [2, 4]  # Невозможно набрать 7
        expected_result = -1

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, money, coins)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_large_case(self):
        # given
        money = 1000
        coins = [1, 5, 10, 25, 50, 100]
        expected_result = 10  # 1000 = 10 * 100

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, money, coins)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

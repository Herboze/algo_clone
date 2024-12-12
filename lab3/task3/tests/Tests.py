from unittest import TestCase
import lab3.task3.src.Solution as Solution
from lab3.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        # given
        n = 1
        k = 1
        sizes = [5]
        expected_output = "ДА"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, k, sizes)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_upper_bound(self):
        # given
        n = 10 ** 5
        k = 2
        sizes = list(range(1, 100001))
        expected_output = "ДА"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, k, sizes)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input1(self):
        # given
        n = 3
        k = 2
        sizes = [2, 1, 3]
        expected_output = "НЕТ"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, k, sizes)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input2(self):
        # given
        n = 5
        k = 3
        sizes = [1, 5, 3, 4, 1]
        expected_output = "ДА"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, k, sizes)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

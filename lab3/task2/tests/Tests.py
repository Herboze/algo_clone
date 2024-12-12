from unittest import TestCase
import lab3.task2.src.Solution as Solution
from lab3.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        # given
        n = 1
        expected_output = [1]

        # when
        result, time, memory = measuring_time_and_memory(Solution.anti_quick_sort, n)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_upper_bound(self):
        # given
        n = 10 ** 6

        # when
        result, time, memory = measuring_time_and_memory(Solution.anti_quick_sort, n)

        # then
        self.assertEqual(len(result), n)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input1(self):
        # given
        n = 3
        expected_output = [1, 3, 2]

        # when
        result, time, memory = measuring_time_and_memory(Solution.anti_quick_sort, n)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input2(self):
        # given
        n = 5
        expected_output = [1, 4, 5, 3, 2]

        # when
        result, time, memory = measuring_time_and_memory(Solution.anti_quick_sort, n)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

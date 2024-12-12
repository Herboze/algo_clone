from unittest import TestCase
import lab1.task10.src.Solution as Solution
from lab1.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        result = measuring_time_and_memory(Solution.function, 1, "A")
        self.assertEqual(result, "A")

    def test_should_task_with_upper_bound(self):
        test_string = "A" * 100000
        result = measuring_time_and_memory(Solution.function, 100000, test_string)
        self.assertEqual(result, "A" * 100000)

    def test_should_task_with_input(self):
        result = measuring_time_and_memory(Solution.function, 7, "AABBCCC")
        self.assertEqual(result, "ABCCCBA")

    def test_should_task_with_mixed_input(self):
        result = measuring_time_and_memory(Solution.function, 9, "AAABBBCCC")
        self.assertEqual(result, "ABCCCBA")

    def test_should_task_with_all_odd_frequencies(self):
        result = measuring_time_and_memory(Solution.function, 5, "ABCDE")
        self.assertEqual(result in "ABCDE", True)

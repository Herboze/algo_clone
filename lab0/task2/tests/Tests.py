from unittest import TestCase
import lab0.task2.src.Solution as Solution
from lab0.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        a = -1e9
        b = -1e9
        result = measuring_time_and_memory(Solution.function, a, b)
        self.assertEqual(a + b * b, result)

    def test_should_task_with_upper_bound(self):
        a = 1e9
        b = 1e9
        result = measuring_time_and_memory(Solution.function, a, b)
        self.assertEqual(a + b * b, result)

    def test_should_task_with_input1(self):
        a = 12
        b = 25
        result = measuring_time_and_memory(Solution.function, a, b)
        self.assertEqual(a + b * b, result)

    def test_should_task_with_input2(self):
        a = 130
        b = 61
        result = measuring_time_and_memory(Solution.function, a, b)
        self.assertEqual(a + b * b, result)

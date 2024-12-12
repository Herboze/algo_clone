from unittest import TestCase
import lab2.task5.src.Solution as Solution
from lab2.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        a = [0]
        result = measuring_time_and_memory(Solution.function, a)
        self.assertEqual(Solution.function(a), result)

    def test_should_task_with_upper_bound(self):
        from random import randint
        n = 10 ** 5
        a = [randint(0, 10 ** 9) for _ in range(n)]
        result = measuring_time_and_memory(Solution.function, a)
        self.assertEqual(Solution.function(a), result)

    def test_should_task_with_input1(self):
        a = [2, 3, 9, 2, 2]
        result = measuring_time_and_memory(Solution.function, a)
        self.assertEqual(1, result)

    def test_should_task_with_input2(self):
        a = [1, 2, 3, 4]
        result = measuring_time_and_memory(Solution.function, a)
        self.assertEqual(0, result)

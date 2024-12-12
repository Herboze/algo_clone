from unittest import TestCase
import lab1.task5.src.Solution as Solution
from lab1.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        n = 1
        a = [0]
        result = measuring_time_and_memory(Solution.function, n, a)
        self.assertEqual([0], result)

    def test_should_task_with_upper_bound(self):
        from random import randint
        n = 1000
        a = [randint(0, 10 ** 9) for _ in range(n)]
        result = measuring_time_and_memory(Solution.function, n, a)
        self.assertEqual(sorted(a), result)

    def test_should_task_with_input(self):
        n = 6
        a = [31, 41, 59, 26, 41, 58]
        result = measuring_time_and_memory(Solution.function, n, a)
        self.assertEqual(sorted(a), result)

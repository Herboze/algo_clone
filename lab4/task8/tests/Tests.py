from unittest import TestCase
import lab4.task8.src.Solution as Solution
from lab4.utils import measuring_time_and_memory


class TestSolution(TestCase):

    def test_should_with_lower_bound(self):
        # given
        n = 1
        line = "7".split()

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, line)

        # then
        self.assertEqual(result, 7)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10 ** 6
        line = ("1 " * 10 ** 6).strip().split()

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, line)

        # then
        self.assertEqual(result, 1)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

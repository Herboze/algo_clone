from unittest import TestCase
from lab6.utils import measuring_time_and_memory
import lab6.task8.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_input1(self):
        # given
        n, x, a, b = 10, 5, 1, 2
        ac, bc, ad, bd = 2, 3, 4, 5
        expected_result = (50770515369608, 41, 52)

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, x, a, b, ac, bc, ad, bd)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 5, "Execution time exceeded 5 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        n, x, a, b = 1, 0, 0, 0
        ac, bc, ad, bd = 0, 0, 1, 1
        expected_result = (1, 1, 1)

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, x, a, b, ac, bc, ad, bd)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 5, "Execution time exceeded 5 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10 ** 7
        x, a, b = 10 ** 14, 10 ** 2, 10 ** 10
        ac, bc, ad, bd = 999, 10 ** 14, 500, 10 ** 14
        expected_result_length = 3

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n, x, a, b, ac, bc, ad, bd)

        # then
        self.assertEqual(len(result), expected_result_length, "Output length mismatch")
        self.assertLessEqual(time, 5, "Execution time exceeded 5 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

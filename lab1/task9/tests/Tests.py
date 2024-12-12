from unittest import TestCase
import lab1.task9.src.Solution as Solution
from lab1.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        cases = {
            "1001": ["100", "101"],
            "10": ["1", "1"],
            "1": ["0", "1"],
            "0": ["0", "0"]
        }
        for case in cases.keys():
            A, B = cases[case]
            result = measuring_time_and_memory(Solution.function, A, B)
            self.assertEqual(case, result)

    def test_should_task_with_upper_bound(self):
        A, B = bin(1000)[2:], bin(1000)[2:]
        res = bin(2000)[2:]
        result = measuring_time_and_memory(Solution.function, A, B)
        self.assertEqual(res, result)

    # def test_should_task_with_random_numbers(self):
    #     from random import randint
    #
    #     for _ in range(10):
    #         A, B = randint(0, 1000), randint(0, 1000)
    #         res = A + B
    #
    #         maxlen = max(len(bin(A)), len(bin(B))) - 2
    #
    #         result = measuring(Solution.function, str.zfill(bin(A)[2:], maxlen), str.zfill(bin(B)[2:], maxlen))
    #         self.assertEqual(bin(res)[2:], result)

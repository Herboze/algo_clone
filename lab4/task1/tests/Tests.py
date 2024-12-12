from unittest import TestCase
from lab4.utils import measuring_time_and_memory
from random import randint
import lab4.task1.src.Solution as Solution


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.stack: Solution.Stack = Solution.Stack()

    def tearDown(self) -> None:
        self.stack = None

    def to_test(self, n) -> tuple[list[str], list[str]]:
        expected: list[str] = []
        res: list[str] = []
        array: list[int] = []
        for line in range(n):
            value, operand = randint(0, 10 ** 9), "-" if randint(0, 1) else "+"
            if operand == "+":
                self.stack.push_back(value)
                array.append(value)
            else:
                if len(array) == 0: continue
                res.append(str(self.stack.pop()))
                expected.append(str(array.pop()))
        return expected, res

    def test_should_with_lower_bound(self):
        # given
        n = 1

        # when
        expect_and_result, time, memory = measuring_time_and_memory(self.to_test, n)

        # then
        self.assertEqual(expect_and_result[0], expect_and_result[1])
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 1000000

        # when
        expect_and_result, time, memory = measuring_time_and_memory(self.to_test, n)

        # then
        self.assertEqual(expect_and_result[0], expect_and_result[1])
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

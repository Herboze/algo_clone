from unittest import TestCase
from lab4.utils import measuring_time_and_memory
import lab4.task6.src.Solution as Solution
from random import randint


class TestSolution(TestCase):

    def setUp(self) -> None:
        self.queue: Solution.Queue = Solution.Queue()

    def tearDown(self) -> None:
        self.queue = None

    def to_test(self, n) -> tuple[list[str], list[str]]:
        expected: list[str] = []
        res: list[str] = []
        array: list[int] = []
        for i in range(n):
            num, operand = randint(0, 10 ** 9), randint(1, 3)
            match operand:
                case 1:  # -
                    if len(array) == 0: continue
                    self.queue.pop()
                    array = array[1:]
                case 2:  # ?
                    if len(array) == 0: continue
                    res.append(str(self.queue.min()))
                    expected.append(str(min(array)))
                case 3:  # +
                    self.queue.push(num)
                    array.append(num)
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
        n = 100000

        # when
        expect_and_result, time, memory = measuring_time_and_memory(self.to_test, n)

        # then
        self.assertEqual(expect_and_result[0], expect_and_result[1])
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

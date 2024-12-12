from unittest import TestCase
import lab4.task7.src.Solution as Solution
from lab4.utils import measuring_time_and_memory
from random import randint


class TestSolution(TestCase):
    def setUp(self) -> None:
        self.dequeue: Solution.Deque = Solution.Deque()

    def tearDown(self) -> None:
        self.dequeue = None

    def to_test(self, n, array, m) -> tuple[list[str], list[str]]:
        expected: list[str] = []

        for i in range(n - m + 1):
            expected.append(str(max(array[i:i + m])))

        max_values = Solution.sliding_window_maximum(n, array, m)
        res: list[str] = list(map(str, max_values))

        return expected, res

    def test_should_with_lower_bound(self):
        # given
        n = 1
        array = [1, 2, 3]
        m = 2

        # when
        expect_and_result, time, memory = measuring_time_and_memory(self.to_test, n, array, m)

        # then
        self.assertEqual(expect_and_result[0], expect_and_result[1])
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10000
        array = [randint(0, 10 ** 9) for _ in range(n)]
        m = randint(1, n + 1)

        # when
        expect_and_result, time, memory = measuring_time_and_memory(self.to_test, n, array, m)

        # then
        self.assertEqual(expect_and_result[0], expect_and_result[1])
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

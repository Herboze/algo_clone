from unittest import TestCase
import lab3.task4.src.Solution as Solution
from lab3.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        # given
        s = 1
        p = 1
        segments = [(0, 10)]
        points = [5]
        expected_output = "1"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, s, p, segments, points)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_upper_bound(self):
        # given
        s = 50000
        p = 50000
        segments = [(50000, 50000) for _ in range(50000)]
        points = [50000 for _ in range(50000)]
        expected_output = " ".join(["50000" for _ in range(50000)])

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, s, p, segments, points)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input1(self):
        # given
        s = 2
        p = 3
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected_output = "1 0 0"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, s, p, segments, points)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input2(self):
        # given
        s = 1
        p = 3
        segments = [(-10, 10)]
        points = [-100, 100, 0]
        expected_output = "0 0 1"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, s, p, segments, points)

        # then
        self.assertEqual(result, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

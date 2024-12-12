from unittest import TestCase
import lab3.task8.src.Solution as Solution
from lab3.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        # given
        points = [(1, 1)]
        k = 1
        expected_output = [(1, 1)]

        # when
        _, time, memory = measuring_time_and_memory(Solution.quicksort, points, 0, len(points) - 1)
        closest_points = points[:k]

        # then
        self.assertEqual(closest_points, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_upper_bound(self):
        # given
        points = [(i, i) for i in range(1000)]
        k = 10

        # when
        _, time, memory = measuring_time_and_memory(Solution.quicksort, points, 0, len(points) - 1)
        closest_points = points[:k]

        # then
        self.assertEqual(len(closest_points), k)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input1(self):
        # given
        points = [(1, 3), (-2, 2)]
        n, k = 2, 1
        expected_output = [(-2, 2)]

        # when
        _, time, memory = measuring_time_and_memory(Solution.quicksort, points, 0, n - 1)
        closest_points = points[:k]

        # then
        self.assertEqual(closest_points, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input2(self):
        # given
        points = [(3, 3), (5, -1), (-2, 4)]
        n, k = 3, 2
        expected_output = [(3, 3), (-2, 4)]

        # when
        _, time, memory = measuring_time_and_memory(Solution.quicksort, points, 0, len(points) - 1)
        closest_points = points[:k]

        # then
        self.assertEqual(closest_points, expected_output)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

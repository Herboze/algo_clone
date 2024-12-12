from unittest import TestCase
from lab7.utils import measuring_time_and_memory
import lab7.task2.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_input1(self):
        # given
        n = 1
        expected_ops = 0
        expected_sequence_len = 1

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n)

        # then
        self.assertEqual(expected_ops, result[0])
        self.assertEqual(expected_sequence_len, len(list(result[1])))
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_input2(self):
        # given
        n = 5
        expected_ops = 3
        expected_sequence_len = 4

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n)

        # then
        self.assertEqual(expected_ops, result[0])
        self.assertEqual(expected_sequence_len, len(list(result[1])))
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_input3(self):
        # given
        n = 96234
        expected_ops = 14
        expected_sequence_len = 15

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n)

        # then
        self.assertEqual(expected_ops, result[0])
        self.assertEqual(expected_sequence_len, len(list(result[1])))
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        n = 1
        expected_ops = 0
        expected_sequence_len = 1

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n)

        # then
        self.assertEqual(expected_ops, result[0])
        self.assertEqual(expected_sequence_len, len(list(result[1])))
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        n = 10 ** 6
        expected_sequence_len = 20

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, n)

        # then
        self.assertEqual(expected_sequence_len, len(list(result[1])))
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

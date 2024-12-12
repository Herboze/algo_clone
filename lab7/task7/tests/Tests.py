from unittest import TestCase
from lab7.utils import measuring_time_and_memory
import lab7.task7.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_match(self):
        # given
        pattern_and_string = ('k?t*n', 'kitten')
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, pattern_and_string)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_not_match(self):
        # given
        pattern_and_string = ('k?t?n', 'kitten')
        expected_result = "NO"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, pattern_and_string)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_empty_pattern(self):
        # given
        pattern_and_string = ('', '')
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, pattern_and_string)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_empty_string(self):
        # given
        pattern_and_string = ('*', '')
        expected_result = "YES"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, pattern_and_string)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

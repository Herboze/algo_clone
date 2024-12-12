from unittest import TestCase
import lab4.task4.src.Solution as Solution
from lab4.utils import measuring_time_and_memory


class TestSolution(TestCase):

    def test_should_task_with_input_1(self):
        # given
        sequence = "[]"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "Success")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_2(self):
        # given
        sequence = "{}[]"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "Success")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_3(self):
        # given
        sequence = "[()]"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "Success")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_4(self):
        # given
        sequence = "(())"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "Success")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_5(self):
        # given
        sequence = "{"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "1")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_6(self):
        # given
        sequence = "{[}"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "3")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_7(self):
        # given
        sequence = "foo(bar);"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "Success")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_task_with_input_8(self):
        # given
        sequence = "foo(bar[i);"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, sequence)

        # then
        self.assertEqual(result, "10")
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

from unittest import TestCase
import lab0.task6.src.Solution as Solution
from lab0.utils import measuring_time_and_memory, updateFileWithData

class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        n = 1
        updateFileWithData("../txtf/input.txt", f"{n}")

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            n = int(input_file.readline().rstrip())
            result = measuring_time_and_memory(Solution.function, n)
            updateFileWithData("../txtf/output.txt", f"{result}")

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(1, output_result)

    def test_should_task_with_upper_bound(self):
        n = 999999
        updateFileWithData("../txtf/input.txt", f"{n}")

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            n = int(input_file.readline().rstrip())
            result = measuring_time_and_memory(Solution.function, n)
            updateFileWithData("../txtf/output.txt", f"{result}")

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(6, output_result)

    def test_should_task_with_input1(self):
        n = 331
        updateFileWithData("../txtf/input.txt", f"{n}")

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            n = int(input_file.readline().rstrip())
            result = measuring_time_and_memory(Solution.function, n)
            updateFileWithData("../txtf/output.txt", f"{result}")

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(9, output_result)

    def test_should_task_with_input2(self):
        n = 327305
        updateFileWithData("../txtf/input.txt", f"{n}")

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            n = int(input_file.readline().rstrip())
            result = measuring_time_and_memory(Solution.function, n)
            updateFileWithData("../txtf/output.txt", f"{result}")

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(5, output_result)

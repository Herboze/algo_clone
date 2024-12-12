from unittest import TestCase
import lab0.task3.src.Solution as Solution
from lab0.utils import measuring_time_and_memory, updateFileWithData

class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        a = int(-1e9)
        b = int(-1e9)
        updateFileWithData("../txtf/input.txt", f"{a} {b}")  # Записываем input

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            a, b = list(map(int, input_file.readline().rstrip().split()))
            result = measuring_time_and_memory(Solution.function, a, b)  # Проводим вычисления
            updateFileWithData("../txtf/output.txt", f"{result}")  # Результат записываем в output

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(a + b, output_result)

    def test_should_task_with_upper_bound(self):
        a = int(1e9)
        b = int(1e9)
        updateFileWithData("../txtf/input.txt", f"{a} {b}")  # Записываем input

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            a, b = list(map(int, input_file.readline().rstrip().split()))
            result = measuring_time_and_memory(Solution.function, a, b)  # Проводим вычисления
            updateFileWithData("../txtf/output.txt", f"{result}")  # Результат записываем в output

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(a + b, output_result)

    def test_should_task_with_input1(self):
        a = 12
        b = 25
        updateFileWithData("../txtf/input.txt", f"{a} {b}")  # Записываем input

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            a, b = list(map(int, input_file.readline().rstrip().split()))
            result = measuring_time_and_memory(Solution.function, a, b)  # Проводим вычисления
            updateFileWithData("../txtf/output.txt", f"{result}")  # Результат записываем в output

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(a + b, output_result)

    def test_should_task_with_input2(self):
        a = 130
        b = 61
        updateFileWithData("../txtf/input.txt", f"{a} {b}")  # Записываем input

        with open("../txtf/input.txt", "r") as input_file, open("../txtf/output.txt", "r") as output_file:
            a, b = list(map(int, input_file.readline().rstrip().split()))
            result = measuring_time_and_memory(Solution.function, a, b)  # Проводим вычисления
            updateFileWithData("../txtf/output.txt", f"{result}")  # Результат записываем в output

            output_result = int(output_file.readline().rstrip())
            self.assertEqual(a + b, output_result)

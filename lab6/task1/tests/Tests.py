from unittest import TestCase
from lab6.utils import measuring_time_and_memory
import lab6.task1.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_input1(self):
        # given
        operations = ['A 2\n', 'A 5\n', 'A 3\n', '? 2\n', '? 4\n', 'A 2\n', 'D 2\n', '? 2\n']
        expected_result = "Y\nN\nN"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_lower_bound(self):
        # given
        operations = ['? 42\n']  # Минимальная входная последовательность
        expected_result = "N"  # Элемента нет в множестве

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_should_with_upper_bound(self):
        # given
        N = 500000
        # Генерируем операции
        operations = ['A {}\n'.format(i) for i in range(1, N // 2)] + \
                     ['D {}\n'.format(i) for i in range(1, N // 4)] + \
                     ['? {}\n'.format(i) for i in range(1, N // 4)]
        # Прогнозируем результат только для операций '?'
        expected_result = "\n".join(["Y" if i in range(N // 4, N // 2) else "N" for i in range(1, N // 4)])

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

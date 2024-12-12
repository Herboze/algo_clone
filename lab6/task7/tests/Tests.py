from unittest import TestCase
from lab6.utils import measuring_time_and_memory
import lab6.task7.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_input1(self):
        # given
        S = "abacaba"
        pairs = [('a', 'a')]  # Массив с одним элементом должен остаться таким же
        expected_result = 6

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, S, pairs)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_input2(self):
        # given
        S = "abacaba"
        pairs = [('a', 'b'), ('a', 'c'), ('b', 'b')]  # Массив с одним элементом должен остаться таким же
        expected_result = 7

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, S, pairs)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_lower_bound(self):
        # given
        S = "a"  # Минимальная строка
        pairs = [('a', 'a')]  # Единственная возможная пара
        expected_result = 0  # Невозможно создать пару из одной буквы

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, S, pairs)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_upper_bound(self):
        # given
        S = "a" * 100000  # Максимально длинная строка из одного символа
        pairs = [('a', 'a')]  # Единственная возможная пара
        # Количество пар в строке длины n = n * (n - 1) / 2
        expected_result = (100000 * 99999) // 2

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, S, pairs)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 1, "Execution time exceeded 1 second")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

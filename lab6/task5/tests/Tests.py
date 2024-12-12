from unittest import TestCase
from lab6.utils import measuring_time_and_memory
import lab6.task5.src.Solution as Solution


class TestSolution(TestCase):

    def test_should_with_input1(self):
        # given
        input_data = [
            "McCain 10\n",
            "McCain 5\n",
            "Obama 9\n",
            "Obama 8\n",
            "McCain 1\n"
        ]
        expected_result = "McCain 16\nObama 17"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, input_data)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_input2(self):
        # given
        input_data = [
            "ivanov 100\n",
            "ivanov 500\n",
            "ivanov 300\n",
            "petr 70\n",
            "tourist 1\n",
            "tourist 2\n"
        ]
        expected_result = "ivanov 900\npetr 70\ntourist 3"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, input_data)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_lower_bound(self):
        # given
        input_data = ["bur 1\n"]
        expected_result = "bur 1"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, input_data)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

    def test_should_with_upper_bound(self):
        # given
        N = 500000
        input_data = [f"candidate{i % 1000} {i % 100}\n" for i in range(N)]
        # Подсчитаем ожидаемый результат
        vote_count = {}
        for i in range(N):
            name = f"candidate{i % 1000}"
            count = i % 100
            if name in vote_count:
                vote_count[name] += count
            else:
                vote_count[name] = count
        expected_result = "\n".join(f"{name} {count}" for name, count in sorted(vote_count.items()))

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, input_data)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 64, "Memory usage exceeded 64 MB")

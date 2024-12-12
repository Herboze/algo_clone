from unittest import TestCase
import lab3.task1.src.Solution as Solution
import lab3.task1.src.Solution2 as Solution2
from time import time
from lab3.utils import generate_random_array
from memory_profiler import memory_usage


def measure_sorting_algorithms(array):
    array1 = array.copy()
    array2 = array.copy()

    # Measure time and memory for randomized_quick_sort_3way
    start_time = time()
    mem_usage_3way = memory_usage((Solution2.randomized_quick_sort_3way, (array1, 0, len(array) - 1)), max_usage=True)
    time1 = time() - start_time

    # Measure time and memory for randomized_quick_sort
    start_time = time()
    mem_usage_plain = memory_usage((Solution.randomized_quick_sort, (array2, 0, len(array2) - 1)), max_usage=True)
    time2 = time() - start_time

    return array1, time2, time1, mem_usage_plain, mem_usage_3way


class TestSolution(TestCase):
    def test_should_sort_with_1000_args(self):
        # given
        size = 1000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        # when
        array, improved, plain, mem_plain, mem_3way = measure_sorting_algorithms(random_array_sorted_desc)
        print(
            f"Size: {size} | Default: {plain:.5f} sec, {mem_plain:.2f} MB | Improved (3rd way): {improved:.5f} sec, {mem_3way:.2f} MB")

        # then
        self.assertEqual(sorted(random_array), array)
        self.assertLessEqual(plain, 2, "Default sort exceeded time limit")
        self.assertLessEqual(improved, 2, "Improved sort exceeded time limit")
        self.assertLessEqual(mem_plain, 256, "Default sort exceeded memory limit")
        self.assertLessEqual(mem_3way, 256, "Improved sort exceeded memory limit")

    def test_should_sort_with_10000_args(self):
        # given
        size = 10000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        # when
        array, improved, plain, mem_plain, mem_3way = measure_sorting_algorithms(random_array_sorted_desc)
        print(
            f"Size: {size} | Default: {plain:.5f} sec, {mem_plain:.2f} MB | Improved (3rd way): {improved:.5f} sec, {mem_3way:.2f} MB")

        # then
        self.assertEqual(sorted(random_array), array)
        self.assertLessEqual(plain, 2, "Default sort exceeded time limit")
        self.assertLessEqual(improved, 2, "Improved sort exceeded time limit")
        self.assertLessEqual(mem_plain, 256, "Default sort exceeded memory limit")
        self.assertLessEqual(mem_3way, 256, "Improved sort exceeded memory limit")

    def test_should_sort_with_100000_args(self):
        # given
        size = 100000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        # when
        array, improved, plain, mem_plain, mem_3way = measure_sorting_algorithms(random_array_sorted_desc)
        print(
            f"Size: {size} | Default: {plain:.5f} sec, {mem_plain:.2f} MB | Improved (3rd way): {improved:.5f} sec, {mem_3way:.2f} MB")

        # then
        self.assertEqual(sorted(random_array), array)
        self.assertLessEqual(plain, 2, "Default sort exceeded time limit")
        self.assertLessEqual(improved, 2, "Improved sort exceeded time limit")
        self.assertLessEqual(mem_plain, 256, "Default sort exceeded memory limit")
        self.assertLessEqual(mem_3way, 256, "Improved sort exceeded memory limit")

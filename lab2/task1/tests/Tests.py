from unittest import TestCase
import lab2.task1.src.Solution as Solution
import time
from lab2.utils import insertion_sort, generate_random_array


def measure_sorting_algorithms(array):
    merge_array = array.copy()
    insertion_array = array.copy()

    start_time = time.time()
    Solution.function_merge_sort(merge_array, 0, len(array) - 1)
    merge_time = time.time() - start_time

    if len(array) < 100000:
        start_time = time.time()
        insertion_sort(insertion_array)
        insertion_time = time.time() - start_time

        return merge_array, merge_time, insertion_time
    return merge_array, merge_time


class TestSolution(TestCase):
    def test_should_sort_with_1000_args(self):
        size = 1000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        array, merge_time, insertion_time = measure_sorting_algorithms(random_array_sorted_desc)
        print(f"Size: {size} | Merge Sort Time: {merge_time:.5f} | Insertion Sort Time: {insertion_time:.5f}")
        self.assertEqual(sorted(random_array), array)

    def test_should_sort_with_10000_args(self):
        size = 10000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        array, merge_time, insertion_time = measure_sorting_algorithms(random_array_sorted_desc)
        print(f"Size: {size} | Merge Sort Time: {merge_time:.5f} | Insertion Sort Time: {insertion_time:.5f}")
        self.assertEqual(sorted(random_array), array)

    def test_should_sort_with_100000_args(self):
        size = 100000
        random_array = generate_random_array(size)
        random_array_sorted_desc = sorted(random_array, reverse=True)

        array, merge_time = measure_sorting_algorithms(random_array_sorted_desc)
        print(f"Size: {size} | Merge Sort Time: {merge_time:.5f} | Insertion Sort Time: Overload")
        self.assertEqual(sorted(random_array), array)

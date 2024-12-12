from unittest import TestCase
from lab6.utils import measuring_time_and_memory
import lab6.task2.src.Solution as Solution

class TestSolution(TestCase):

    def test_example1(self):
        # given
        operations = [
            'add 911 police\n',
            'add 76213 Mom\n',
            'add 17239 Bob\n',
            'find 76213\n',
            'find 910\n',
            'find 911\n',
            'del 910\n',
            'del 911\n',
            'find 911\n',
            'find 76213\n',
            'add 76213 daddy\n',
            'find 76213\n'
        ]
        expected_result = "Mom\nnot found\npolice\nnot found\nMom\ndaddy"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 6, "Execution time exceeded 6 seconds")
        self.assertLessEqual(memory, 512, "Memory usage exceeded 512 MB")

    def test_example2(self):
        # given
        operations = [
            'find 3839442\n',
            'add 123456 me\n',
            'add 0 granny\n',
            'find 0\n',
            'find 123456\n',
            'del 0\n',
            'del 0\n',
            'find 0\n'
        ]
        expected_result = "not found\ngranny\nme\nnot found"

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 6, "Execution time exceeded 6 seconds")
        self.assertLessEqual(memory, 512, "Memory usage exceeded 512 MB")

    def test_large_input(self):
        # given
        N = 100000
        operations = ['add {} person{}\n'.format(i, i) for i in range(1, N//2)] + \
                     ['del {}\n'.format(i) for i in range(1, N//4)] + \
                     ['find {}\n'.format(i) for i in range(1, N//4)]
        expected_result = "\n".join(["not found" if i < N//4 else f"person{i}" for i in range(1, N//4)])

        # when
        result, time, memory = measuring_time_and_memory(Solution.function, operations)

        # then
        self.assertEqual(expected_result, result)
        self.assertLessEqual(time, 6, "Execution time exceeded 6 seconds")
        self.assertLessEqual(memory, 512, "Memory usage exceeded 512 MB")

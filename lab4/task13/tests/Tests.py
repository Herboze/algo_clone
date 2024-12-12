from unittest import TestCase
import lab4.task13.src.Solution as Solution
from lab4.utils import measuring_time_and_memory


class TestStack(TestCase):
    def setUp(self):
        self.stack = Solution.Stack()

    def tearDown(self) -> None:
        self.stack = None

    def test_isEmpty_on_empty_stack(self):
        # given
        # an empty stack

        # when
        result, time, memory = measuring_time_and_memory(self.stack.isEmpty)

        # then
        self.assertTrue(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_push_and_isEmpty(self):
        # given
        self.stack.push(1)

        # when
        result, time, memory = measuring_time_and_memory(self.stack.isEmpty)

        # then
        self.assertFalse(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_push_and_pop(self):
        # given
        def execute():
            self.stack.push(1)
            self.stack.push(2)
            self.stack.push(3)

            return (self.stack.pop(), self.stack.pop(), self.stack.pop())

        # when
        result, time, memory = measuring_time_and_memory(execute)

        # then
        self.assertEqual(result, (3, 2, 1))
        self.assertTrue(self.stack.isEmpty())
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_pop_on_empty_stack(self):
        # given
        # an empty stack

        # when
        result, time, memory = measuring_time_and_memory(self.stack.pop)

        # then
        self.assertIsNone(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_display(self):
        # given
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)

        # when
        result, time, memory = measuring_time_and_memory(self.stack.display)

        # then
        self.assertIn("3 -> 2 -> 1 -> None", result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")


class TestQueue(TestCase):
    def setUp(self) -> None:
        self.queue = Solution.Queue()

    def tearDown(self) -> None:
        self.queue = None

    def test_isEmpty_on_empty_queue(self):
        # given
        # an empty queue

        # when
        result, time, memory = measuring_time_and_memory(self.queue.isEmpty)

        # then
        self.assertTrue(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_Enqueue_and_isEmpty(self):
        # given
        self.queue.Enqueue(1)

        # when
        result, time, memory = measuring_time_and_memory(self.queue.isEmpty)

        # then
        self.assertFalse(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_Enqueue_and_Dequeue(self):
        # given
        def execute():
            self.queue.Enqueue(1)
            self.queue.Enqueue(2)
            self.queue.Enqueue(3)

            return (self.queue.Dequeue(), self.queue.Dequeue(), self.queue.Dequeue())

        # when
        result, time, memory = measuring_time_and_memory(execute)

        # then
        self.assertEqual(result, (1, 2, 3))
        self.assertTrue(self.queue.isEmpty())
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_Dequeue_on_empty_queue(self):
        # given
        # an empty queue

        # when
        result, time, memory = measuring_time_and_memory(self.queue.Dequeue)

        # then
        self.assertIsNone(result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

    def test_display(self):
        # given
        self.queue.Enqueue(1)
        self.queue.Enqueue(2)
        self.queue.Enqueue(3)

        # when
        result, time, memory = measuring_time_and_memory(self.queue.display)

        # then
        self.assertIn("1 -> 2 -> 3 -> None", result)
        self.assertLessEqual(time, 2, "Execution time exceeded 2 seconds")
        self.assertLessEqual(memory, 256, "Memory usage exceeded 256 MB")

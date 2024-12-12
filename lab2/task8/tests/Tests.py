from unittest import TestCase
import lab2.task6.src.Solution as Solution
from lab2.utils import measuring_time_and_memory


class TestSolution(TestCase):
    def test_should_task_with_lower_bound(self):
        # Тест для случая, когда у нас всего одна цена
        prices = [100]
        buy_day, sell_day, max_profit = measuring_time_and_memory(Solution.function, prices)
        self.assertEqual(buy_day, 0)
        self.assertEqual(sell_day, 0)
        self.assertEqual(max_profit, 100)

    def test_should_task_with_upper_bound(self):
        # Тест для случая, когда у нас много цен, все они возрастают
        prices = list(range(1, 10 ** 5))
        buy_day, sell_day, max_profit = measuring_time_and_memory(Solution.function, prices)
        self.assertEqual(buy_day, 0)
        self.assertEqual(sell_day, len(prices) - 1)
        self.assertEqual(max_profit, sum(prices))  # Сумма всех цен

    def test_should_task_with_all_negative_prices(self):
        prices = [-1, -2, -3, -4]
        buy_day, sell_day, max_profit = measuring_time_and_memory(Solution.function, prices)
        self.assertEqual(buy_day, 0)
        self.assertEqual(sell_day, 0)
        self.assertEqual(max_profit, -1)  # Максимальная цена -1

    def test_should_task_with_zero_prices(self):
        # Тест для случая, когда все цены равны нулю
        prices = [0, 0, 0, 0]
        buy_day, sell_day, max_profit = measuring_time_and_memory(Solution.function, prices)
        self.assertEqual(buy_day, 0)
        self.assertEqual(sell_day, 0)
        self.assertEqual(max_profit, 0)

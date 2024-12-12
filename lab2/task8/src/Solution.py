from lab2.utils import read, write


def function(prices):
    max_profit = float('-inf')
    current_profit = 0
    buy_day = 0
    best_buy_day = 0
    best_sell_day = 0

    for i in range(len(prices)):
        # Пересчитываем профит
        current_profit += prices[i]

        # Обновляем профит если он привысил максимальный к текущему моменту
        if current_profit > max_profit:
            max_profit = current_profit
            best_buy_day = buy_day
            best_sell_day = i

        # Пропускаем день, если нам это в убыток
        if current_profit < 0:
            current_profit = 0
            buy_day = i + 1

    return best_buy_day, best_sell_day, max_profit


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    lines = file.readlines()

    dates = []
    prices = []

    file.close()

    for line in lines[1:]:
        date, price = line.strip().split(',')
        dates.append(date)
        prices.append(int(price))

    buy_day, sell_day, max_profit = function(prices)

    write('../txtf/output.txt', f"Фирма: Примерная Фирма\n")
    write('../txtf/output.txt', f"Срок: {dates[0]} — {dates[-1]}\n")
    write('../txtf/output.txt', f"Дата покупки: {dates[buy_day]}\n")
    write('../txtf/output.txt', f"Дата продажи: {dates[sell_day]}\n")
    write('../txtf/output.txt', f"Максимальная прибыль: {max_profit}\n")

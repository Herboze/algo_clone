from lab7.utils import read, write


def function(money, coins):
    dp = [float('inf')] * (money + 1)
    dp[0] = 0  # 0 монет нужно для суммы 0

    for coin in coins:
        for x in range(coin, money + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[money] if dp[money] != float('inf') else -1


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    lines = file.readlines()
    file.close()

    first_line = list(map(int, lines[0].split()))
    money, k = first_line[0], first_line[1]
    coins = list(map(int, lines[1].split()))

    result = function(money, coins)

    print(f"\nINPUT: {money, coins}")
    print(f"OUTPUT:\n{result}")

    write('../txtf/output.txt', str(result))

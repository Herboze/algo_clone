from lab7.utils import read, write


def function(n):
    # Массив для хранения минимального числа операций
    dp = [0] * (n + 1)
    # Массив для восстановления пути
    prev = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2

        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    # Восстановление пути
    sequence = []
    current = n
    while current > 0:
        sequence.append(current)
        current = prev[current]
    sequence.reverse()

    return dp[n], sequence


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    n = int(file.readline().strip())
    file.close()

    min_ops, sequence = function(n)

    print(f"\nINPUT: {n}")
    print(f"OUTPUT:\n{min_ops, sequence}")
    write('../txtf/output.txt', str(min_ops) + '\n' + ' '.join(map(str, sequence)))

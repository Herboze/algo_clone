from lab7.utils import read, write


def function(a, b, c):
    n, m, l = len(a), len(b), len(c)

    # Создаем 3D-массив для динамического программирования
    dp = [[[0] * (l + 1) for _ in range(m + 1)] for __ in range(n + 1)]

    # Заполняем таблицу DP
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1
                else:
                    dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k], dp[i][j][k - 1])

    return dp[n][m][l]


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    lines = file.readlines()
    file.close()

    n = int(lines[0].strip())
    a = list(map(int, lines[1].split()))
    m = int(lines[2].strip())
    b = list(map(int, lines[3].split()))
    l = int(lines[4].strip())
    c = list(map(int, lines[5].split()))

    result = function(a, b, c)

    print(f"\nINPUT: {n}")
    print(f"OUTPUT:\n{result}")

    write('../txtf/output.txt', str(result))

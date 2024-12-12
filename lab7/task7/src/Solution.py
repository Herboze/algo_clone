from lab7.utils import read, write


def function(pattern_and_string):
    pattern, string = pattern_and_string
    n, m = len(pattern), len(string)

    # Создаем DP таблицу
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True

    # Инициализация для пустой строки
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]

    # Заполнение таблицы
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == string[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif pattern[i - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

    return "YES" if dp[n][m] else "NO"


if __name__ == "__main__":
    # Чтение входных данных
    file = read('../txtf/input.txt')
    pattern = file.readline().strip()
    string = file.readline().strip()
    file.close()

    res = function((pattern, string))

    print(f"\nINPUT: {pattern, string}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', res)

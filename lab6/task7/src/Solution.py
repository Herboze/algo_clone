from lab6.utils import read, write


def function(S, pairs):
    # Преобразуем красивые пары в множество для быстрого поиска
    beautiful_pairs = set(pairs)

    # Словарь для подсчета количества символов
    char_count = {}
    total_pairs = 0

    # Проходим по строке и считаем пары
    for char in S:
        # Проверяем, с какими символами char образует красивые пары
        for prev_char, count in char_count.items():
            if (prev_char, char) in beautiful_pairs:
                total_pairs += count  # Увеличиваем счетчик красивых пар

        # Обновляем словарь для текущего символа
        char_count[char] = char_count.get(char, 0) + 1

    return total_pairs


if __name__ == "__main__":
    file = read('../txtf/input.txt')
    lines = file.readlines()
    file.close()

    _, k = map(int, lines[0].split())
    S = lines[1].strip()
    pairs = [tuple(line.strip()) for line in lines[2:2 + k]]

    res = function(S, pairs)

    print(f"\nINPUT: {k, S, pairs}")
    print(f"OUTPUT:\n{res}")

    write('../txtf/output.txt', str(res))

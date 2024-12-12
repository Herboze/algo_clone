def function(_, s):
    from collections import Counter
    freq = Counter(s)  # частота вхождения каждой буквы

    left_part = []  # заведу список для симметричной части (левая половина)
    center = ""  # Символ для центра (если есть нечетные)

    # сртирую буквы для выбора минимального палиндрома в словарном порядке
    for char in sorted(freq.keys()):
        count = freq[char]
        if count % 2 == 1:
            # если количество нечетное, один символ идет в центр
            center = char
            count -= 1  # остальное в симметричные части
        left_part.append(char * (count // 2))  # добавляю символ в левую часть

    # формирую левую часть, центр и правую часть
    left_part = ''.join(left_part)  # объединяю список в строку
    res = left_part + center + left_part[::-1]  # строим палиндром

    return res


if __name__ == "__main__":
    input = open("../txtf/input.txt", "r")
    output = open("../txtf/output.txt", "w")

    n = int(input.readline().strip())
    a = input.readline().strip()

    res = function(n, a)

    output.write(res)
